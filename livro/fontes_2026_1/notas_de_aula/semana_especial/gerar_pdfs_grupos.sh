#!/bin/bash
# gerar_pdfs_grupos.sh
# Gerar PDFs a partir dos HTMLs via macOS Print to PDF

BASE="/Users/cayofel/Documents/GitHub/unifacol_aed/aula/semana_especial"

echo "Gerando PDFs via macOS Print to PDF...\n"

for grupo in a b c d e; do
    html_file="$BASE/grupo_$grupo.html"
    pdf_file="$BASE/grupo_$grupo.pdf"
    
    # Usar lpadmin para imprimir para PDF (requer configuração)
    # OU usar AppleScript para invocar Print Dialog
    
    # Alternativa: usar enscript ou similar (deprecated no modern macOS)
    
    # Melhor alternativa: instruir o usuário
    echo "ℹ Para gerar grupo_$grupo.pdf:"
    echo "  1. open '$html_file'"
    echo "  2. Pressionar Cmd+P"
    echo "  3. Selecionar 'Salvar como PDF'"
    echo "  4. Nomear como 'grupo_$grupo.pdf' e salvar em '$BASE/'"
    echo ""
done

echo "\n💡 Ou use Python com a biblioteca 'pypdf' (mais leve):"
echo "   pip install pypdf"
echo "   python3 << 'EOF'"
echo "   from pathlib import Path"
echo "   import subprocess"
echo "   base = '$BASE'"
echo "   for grupo in 'abcde':"
echo "       html = f'{base}/grupo_{grupo}.html'"
echo "       subprocess.run(['open', '-a', 'Google Chrome', html])"
echo "       # Depois Cmd+P manualmente"
echo "   EOF"
