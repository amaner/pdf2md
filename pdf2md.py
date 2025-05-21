import pdfplumber
from markdownify import markdownify as md

def pdf_to_md(pdf_path, output_path):
    markdown_content = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                markdown_content += text + "\n\n"

    with open(output_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

pdf_to_md("atssprop.pdf", "output.md")