from pypdf import PdfReader, PdfWriter
import glob

 # TODO Get all pdf files in the current directory
with open("cover_sheet.pdf", "rb") as coverPage:
    coverRead = PdfReader(coverPage)
    coverPage = coverRead.get_page(0)
    pdfWrite = PdfWriter()
    pyFiles = glob.glob('*.pdf')
    for file in range(len(pyFiles)):
        # TODO: insert cover page
        with open(f"outputCover{pyFiles[file]}", "wb") as outputFile:
            pdfWrite.add_page(coverPage)
            pdfWrite.write(outputFile)
            # TODO: insert all other pages from original file
            with open(f"{pyFiles[file]}", "rb") as readFile:
                mainRead = PdfReader(readFile)
                for page in range(mainRead.get_num_pages()):
                    mainPage=mainRead.get_page(page)
                    pdfWrite.add_page(mainPage)
                    pdfWrite.write(outputFile)