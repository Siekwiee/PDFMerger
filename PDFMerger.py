import PyPDF2
import os
from sys import argv

merger = PyPDF2.PdfMerger()

filePath = argv[1]

for file in os.listdir(filePath):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined.pdf", filePath)