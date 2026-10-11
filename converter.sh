#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:?Falta o Markdown de entrada}"
OUTPUT="${2:?Falta o PDF de saída}"

cd "$(dirname "$INPUT")"

exec /app/gerar-pdf-opcional.sh "$INPUT" "$OUTPUT"
