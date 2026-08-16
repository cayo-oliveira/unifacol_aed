#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerar PDFs a partir dos HTMLs usando weasyprint.

Rodas: python3 gerar_pdfs_grupos.py
"""

import os
import sys

try:
    from weasyprint import HTML, CSS
except ImportError:
    print("❌ weasyprint não instalado. Instalando...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "weasyprint"], check=True)
    from weasyprint import HTML, CSS

BASE = os.path.dirname(os.path.abspath(__file__))

grupos = [
    ("a", "Olist E-commerce"),
    ("b", "IBM HR Analytics"),
    ("c", "Superstore Varejo"),
    ("d", "Saúde Pública"),
    ("e", "FinTech Premium"),
]

print("Gerando PDFs a partir dos HTMLs...\n")

for grupo_id, grupo_nome in grupos:
    html_file = os.path.join(BASE, f"grupo_{grupo_id}.html")
    pdf_file = os.path.join(BASE, f"grupo_{grupo_id}.pdf")
    
    try:
        # Ler HTML
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Converter para PDF
        HTML(string=html_content, base_url=BASE).write_pdf(pdf_file)
        print(f"✓ grupo_{grupo_id}.pdf ({grupo_nome})")
    except Exception as e:
        print(f"❌ Erro ao gerar grupo_{grupo_id}.pdf: {e}")

print("\n✅ PDFs gerados com sucesso!\n")
print("Arquivos criados:")
for grupo_id, grupo_nome in grupos:
    pdf_file = os.path.join(BASE, f"grupo_{grupo_id}.pdf")
    if os.path.exists(pdf_file):
        size_kb = os.path.getsize(pdf_file) / 1024
        print(f"  • grupo_{grupo_id}.pdf ({size_kb:.1f} KB) — {grupo_nome}")
