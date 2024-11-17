import fitz  # PyMuPDF
from docx import Document

def convert_pdf_to_word(pdf_path):
    # Cria um documento Word
    doc = Document()

    # Abre o arquivo PDF
    pdf_document = fitz.open(pdf_path)

    # Itera pelas páginas do PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()

        # Adiciona o texto ao documento Word
        doc.add_paragraph(text)
        
    # Salva o documento Word
    word_path = f"{pdf_path.rsplit('.', 1)[0]}.docx"
    doc.save(word_path)

    print(f"Arquivo PDF convertido para Word com sucesso: {word_path}")

# Exemplo de uso:
pdf_path = 'exemplo.pdf'
convert_pdf_to_word('C:\\Users\\victo\\OneDrive\\Desktop\\Python - Curso\\conversor_pdf\\cv-victor-lemes.pdf')
