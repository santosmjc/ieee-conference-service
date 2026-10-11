#!/usr/bin/env bash
set -euo pipefail

input="${1:-artigo.md}"
output="${2:-${input%.md}.pdf}"
bibliography="${BIBLIOGRAPHY:-referencias.bib}"

if [[ ! -f "$input" ]]; then
  echo "Erro: não encontrei o ficheiro '$input'." >&2
  exit 1
fi

for file in ieee-conference.tex; do
  if [[ ! -f "$file" ]]; then
    echo "Erro: não encontrei '$file'." >&2
    exit 1
  fi
done

args=(
  "$input"
  --from=markdown
  --to=latex
  --template=ieee-conference.tex
  --pdf-engine=xelatex
  --output="$output"
)

if [[ -f "$bibliography" ]]; then
  if [[ ! -f ieee.csl ]]; then
    echo "Erro: não encontrei 'ieee.csl'." >&2
    exit 1
  fi
  args+=(--citeproc --bibliography="$bibliography" --csl=ieee.csl)
elif [[ -n "${BIBLIOGRAPHY:-}" ]]; then
  echo "Erro: a bibliografia indicada não existe: '$bibliography'." >&2
  exit 1
else
  echo "Aviso: sem referencias.bib; a compilar sem citeproc." >&2
  echo "Use apenas se as referências estiverem incluídas no documento." >&2
fi

pandoc "${args[@]}"
echo "PDF criado: $output"
