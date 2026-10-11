FROM python:3.12-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HOME=/tmp

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        pandoc \
        texlive-xetex \
        texlive-latex-recommended \
        texlive-latex-extra \
        texlive-fonts-recommended \
        texlive-publishers \
        texlive-science \
        fonts-dejavu-core \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py converter.sh gerar-pdf-opcional.sh ieee-conference.tex ./

RUN chmod 0555 converter.sh gerar-pdf-opcional.sh \
    && useradd --uid 10001 --no-create-home --shell /usr/sbin/nologin converter

USER 10001:10001

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--limit-concurrency", "8"]
