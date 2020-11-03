import os
from PyPDF2 import PdfFileReader


def get_page_numbers(root, filename):
    # print(os.path.join(root, filename))
    pdf = PdfFileReader(open(os.path.join(root, filename), 'rb'))
    return pdf.getNumPages()
