#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Uso: $0 CAMINHO_DO_MAIN_TEX" >&2
  exit 2
fi

tex_file="$1"
tex_dir="$(cd "$(dirname "$tex_file")" && pwd)"
tex_name="$(basename "$tex_file")"

cd "$tex_dir"
# Os pacotes da trilha já devem estar no cache local. O modo somente-cache
# evita que uma oscilação de rede impeça a compilação em sala ou no CI local.
tectonic --only-cached --keep-logs --keep-intermediates "$tex_name"

log_name="${tex_name%.tex}.log"
if [ -f "$log_name" ]; then
  if rg -n -F \
    -e 'Overfull \hbox' \
    -e 'Overfull \vbox' \
    -e '! LaTeX Error' \
    -e 'Undefined control sequence' \
    "$log_name"; then
    echo "A compilação terminou, mas o log exige revisão." >&2
    exit 3
  fi
fi

echo "PDF gerado em $tex_dir/${tex_name%.tex}.pdf"
