#!/bin/bash

export IEEE_API_TOKEN='o-token-configurado-no-env'

curl \
  --fail-with-body \
  --show-error \
  --max-time 150 \
  -H "Authorization: Bearer ${IEEE_API_TOKEN}" \
  -F "file=@artigo.zip;type=application/zip" \
  https://apps.validation.pt/ieee-conference \
  --output artigo.pdf
