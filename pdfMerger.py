import PyPDF2
import sys
import os 

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combinedPDF.pdf") # You can change the final merged pdf name as you wish