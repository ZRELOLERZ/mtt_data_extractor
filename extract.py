import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
# From PDFInterpreter import both PDFResourceManager and PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
# Import this to raise exception whenever text extraction from PDF is not allowed
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator
#text = extract_text('major_timber_trees.pdf')
filename = "major_timber_trees.pdf"
#filename = "sample_pdf.pdf"

fp = open(filename, "rb")

extractedText = ""
parser = PDFParser(fp)

document = PDFDocument(parser)

resourceManager = PDFResourceManager()

laParams = LAParams()

device = PDFPageAggregator(resourceManager, laparams=laParams)

interpreter = PDFPageInterpreter(resourceManager, device)

for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for ltObject in layout:
        if isinstance(ltObject, LTTextBox) or isinstance(ltObject, LTTextLine):
            print(ltObject)
            extractedText += ltObject.get_text()

fp.close()

# print(extractedText.encode("utf-8"))
