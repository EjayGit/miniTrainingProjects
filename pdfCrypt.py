from pypdf import PdfReader, PdfWriter

pdfRead = PdfReader("Behavioral Epigenetics how nurture shapes nature.pdf")
pdfWrite = PdfWriter()
for page in range(pdfRead.get_num_pages()):
    pdfWrite.add_page(pdfRead.get_page(page))

pdfWrite.encrypt(user_password="test123")
with open("encrypted.pdf", "wb") as ef:
    pdfWrite.write(ef)

pdfRead = PdfReader("encrypted.pdf")
# This does not work as it is encrypted -> pdfRead.get_page(0)
pdfRead.decrypt("test123")
page1 = pdfRead.get_page(1)