from pypdf import PdfReader, PdfWriter

with open("BikeRentalSystem.pdf", "rb") as file, open("writeOutput.pdf", "wb") as output:
    pdfRead = PdfReader(file)
    page = pdfRead.get_page(1)
    pdfWrite = PdfWriter()
    pdfWrite.add_page(page)
    pdfWrite.write(output)