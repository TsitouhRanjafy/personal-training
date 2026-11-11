import PyPDF2

pdfFileObject = open('test.pdf','rb') # reading only, in binary format
pdfReaderObject = PyPDF2.PdfReader(pdfFileObject)

print(len(pdfReaderObject.pages))

firstPageObject = pdfReaderObject.pages[0]

print(firstPageObject.extract_text())