from pypdf import PdfReader, PdfWriter

filePdf = PdfReader("BikeRentalSystem.pdf", "rb")
for page in range(filePdf.get_num_pages()):
    pdfWriter = PdfWriter()
    pdfWriter.add_page(filePdf.get_page(page).rotate(90*page))
    with open(f"SplitFile{page}.pdf", "wb") as outputPdf:
        pdfWriter.write(outputPdf)