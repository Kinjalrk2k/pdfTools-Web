import os
from PyPDF2 import PdfFileReader


def get_page_numbers(root, filename):
    # print(os.path.join(root, filename))
    f = open(os.path.join(root, filename), 'rb')
    pdf = PdfFileReader(f)
    pageNums = pdf.getNumPages()
    f.close()
    return pageNums
