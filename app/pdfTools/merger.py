from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def merge(metadata, root, outfilename):
    writer = PdfFileWriter()
    for filedata in metadata:
        with open(os.path.join(root, filedata["filename"]), 'rb') as infile:
            reader = PdfFileReader(infile)

            p_start = filedata["start"] - 1
            p_end = filedata["end"]

            for i in range(p_start, p_end):
                writer.addPage(reader.getPage(i))

            with open(os.path.join(root, outfilename), 'wb') as outfile:
                writer.write(outfile)
