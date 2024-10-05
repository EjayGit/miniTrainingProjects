from pypdf import PdfReader

with open("Behavioral Epigenetics how nurture shapes nature.pdf", "rb") as file:
    pdfRead = PdfReader(file)
    print(pdfRead.get_num_pages())
    page = pdfRead.get_page(1)
    text = page.extract_text()
    info = pdfRead.metadata
    print(text)