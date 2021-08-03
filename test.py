"""
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
from pdfminer.high_level import extract_text
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
"""

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextBoxHorizontal
from pprint import pprint


def printTreeObject(treeObject):
    print(treeObject["scientific_name"] + "\n" +
          treeObject["primary_name"] + "\n" +
          treeObject["vernacular_names"] + "\n" +
          treeObject["botanical_description"] + "\n" +
          "***************************\n"
          )


def formatVernacularNames(str):


filename = "major_timber_trees.pdf"

pages = extract_pages(pdf_file=filename, page_numbers=[40, 42])

for page in pages:
    treeObject = {}
    parsedObject = []
    for ltObject in page:
        if isinstance(ltObject, LTTextBoxHorizontal):
            tempTextObject = ltObject.get_text()
            if tempTextObject != " \n":
                parsedObject.append(tempTextObject.rstrip())

    treeObject["scientific_name"] = parsedObject[0]
    treeObject["primary_name"] = parsedObject[1]
    treeObject["synonym"] = parsedObject[2]
    treeObject["literature"] = parsedObject[3]
    treeObject["vernacular_names"] = parsedObject[4].replace(
        "\n", "").replace("Vernacular", "").replace("names:", "").replace("name:", "").replace(".", "").strip().split(",")
    treeObject["botanical_description"] = parsedObject[5].replace("\n", "")
    treeObject["field_characteristics"] = parsedObject[6].replace("\n", "")
    treeObject["ecology_and_distribution"] = parsedObject[7].replace("\n", "")
    # printTreeObject(treeObject)
    # print(parsedObject)
    pprint(treeObject, sort_dicts=False)
    print()
