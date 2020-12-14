import os
from PyPDF2 import PdfFileMerger, PdfFileReader

merge = PdfFileMerger()

for i in os.scandir():
    if ".pdf" in i.name:
        merge(PdfFileReader(i.name))

name_pdf = input("\nNombra el PDF ==> ")

merge.write(name_pdf)