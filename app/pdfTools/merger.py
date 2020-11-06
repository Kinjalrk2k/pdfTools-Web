from PyPDF2 import PdfFileReader, PdfFileWriter
import os

openfile_list = []


def merge(metadata, root, outfilename):
    global openfile_list
    writer = PdfFileWriter()
    for filedata in metadata:
        with open(os.path.join(root, filedata["filename"]), 'rb') as infile:
            openfile_list.append({
                "id": os.path.normpath(root).split(os.sep)[-1],
                "file": infile
            })
            reader = PdfFileReader(infile)

            p_start = filedata["start"] - 1
            p_end = filedata["end"]

            for i in range(p_start, p_end):
                writer.addPage(reader.getPage(i))

            with open(os.path.join(root, outfilename), 'wb') as outfile:
                openfile_list.append({
                    "id": os.path.normpath(root).split(os.sep)[-1],
                    "file": outfile
                })
                writer.write(outfile)

    # close all open files
    new_open_file_list = []
    for openfile in openfile_list:
        if openfile['id'] == os.path.normpath(root).split(os.sep)[-1]:
            openfile['file'].close()
        else:
            new_open_file_list.append(openfile)
    openfile_list = new_open_file_list
