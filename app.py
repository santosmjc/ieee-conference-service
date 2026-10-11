import hmac
import io
import os
import stat
import subprocess
import tempfile
import threading
import zipfile
from pathlib import Path, PurePosixPath

from fastapi import FastAPI, File, Header, HTTPException, UploadFile
from fastapi.responses import Response

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

TOKEN = os.environ["API_TOKEN"]
MAX_UPLOAD = 20 * 1024 * 1024
MAX_EXPANDED = 200 * 1024 * 1024
MAX_FILES = 500
TIMEOUT = 120
compile_lock = threading.Lock()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ieee-conference")
def convert(
    file: UploadFile = File(...),
    authorization: str = Header(default=""),
):
    expected = f"Bearer {TOKEN}"
    if not hmac.compare_digest(
        authorization.encode(), expected.encode()
    ):
        raise HTTPException(401, "Token inválido")

    if not compile_lock.acquire(blocking=False):
        raise HTTPException(429, "Conversor ocupado; tenta novamente")

    try:
        data = file.file.read(MAX_UPLOAD + 1)
        if len(data) > MAX_UPLOAD:
            raise HTTPException(413, "ZIP excede 20 MiB")

        with tempfile.TemporaryDirectory(prefix="ieee-") as temp:
            root = Path(temp)
            sources = root / "sources"
            sources.mkdir()

            try:
                with zipfile.ZipFile(io.BytesIO(data)) as archive:
                    members = archive.infolist()

                    if len(members) > MAX_FILES:
                        raise HTTPException(413, "Demasiados ficheiros")

                    if sum(m.file_size for m in members) > MAX_EXPANDED:
                        raise HTTPException(413, "ZIP descomprimido demasiado grande")

                    seen = set()

                    for member in members:
                        name = member.filename
                        path = PurePosixPath(name)
                        mode = member.external_attr >> 16

                        if (
                            not name
                            or "\\" in name
                            or ":" in name
                            or path.is_absolute()
                            or ".." in path.parts
                            or stat.S_ISLNK(mode)
                        ):
                            raise HTTPException(400, "Caminho ZIP inválido")

                        target = sources.joinpath(*path.parts).resolve()

                        if not target.is_relative_to(sources.resolve()):
                            raise HTTPException(400, "Caminho fora da pasta")

                        if target in seen:
                            raise HTTPException(400, "Entrada ZIP duplicada")
                        seen.add(target)

                        if member.is_dir():
                            target.mkdir(parents=True, exist_ok=True)
                        else:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            target.write_bytes(archive.read(member))

            except (zipfile.BadZipFile, RuntimeError, NotImplementedError):
                raise HTTPException(400, "ZIP inválido ou não suportado")

            candidates = [
                sources / "artigo" / "artigo.md",
                sources / "artigo.md",
            ]
            markdown = next(
                (p for p in candidates if p.is_file()), None
            )

            if markdown is None:
                raise HTTPException(
                    400,
                    "Falta artigo/artigo.md ou artigo.md",
                )

            output = root / "artigo.pdf"
            log = root / "compile.log"

            try:
                with log.open("wb") as logfile:
                    result = subprocess.run(
                        ["/app/converter.sh", str(markdown), str(output)],
                        cwd=markdown.parent,
                        stdout=logfile,
                        stderr=subprocess.STDOUT,
                        timeout=TIMEOUT,
                        check=False,
                        env={
                            "PATH": os.environ["PATH"],
                            "HOME": "/tmp",
                            "TMPDIR": "/tmp",
                            "LANG": "C.UTF-8",
                        },
                    )
            except subprocess.TimeoutExpired:
                raise HTTPException(504, "Compilação excedeu 120 segundos")

            if result.returncode != 0 or not output.is_file():
                details = log.read_bytes()[-8000:].decode(
                    "utf-8", errors="replace"
                )
                raise HTTPException(422, details)

            pdf = output.read_bytes()
            if not pdf.startswith(b"%PDF-"):
                raise HTTPException(422, "Resultado não é um PDF válido")

            return Response(
                content=pdf,
                media_type="application/pdf",
                headers={
                    "Content-Disposition": 'attachment; filename="artigo.pdf"'
                },
            )
    finally:
        compile_lock.release()
