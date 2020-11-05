from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def merge(metadata, root, outfilename):
    writer = PdfFileWriter()
    openfile_list = []
    for filedata in metadata:
        with open(os.path.join(root, filedata["filename"]), 'rb') as infile:
            openfile_list.append(infile)
            reader = PdfFileReader(infile)

            p_start = filedata["start"] - 1
            p_end = filedata["end"]

            for i in range(p_start, p_end):
                writer.addPage(reader.getPage(i))

            # infile.close()

            # print(filedata["filename"])
            # os.remove(os.path.join(root, filedata["filename"]))

            with open(os.path.join(root, outfilename), 'wb') as outfile:
                writer.write(outfile)
                outfile.close()

    # close all open files
    for openfile in openfile_list:
        openfile.close()
