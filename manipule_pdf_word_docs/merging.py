from PyPDF2 import PdfMerger

path = "./"

pdf_files = ['test.pdf', 'test-1.pdf']

merger = PdfMerger()

for files in pdf_files:
    merger.append(path+files)

merger.write(path+'merged.pdf')
merger.close()

