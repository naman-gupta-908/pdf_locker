from PyPDF2 import PdfFileWriter, PdfFileReader
def lock_pdf(file,pas):
    parser=PdfFileWriter()
    pdf=PdfFileReader(file)
    for p in range(pdf.numPages):
        parser.addPage(pdf.getPage(p))
    parser.encrypt(pas)
    with open(f"encrypted {file}","wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted {file} Created ... named : encrypted",file)
file=input("Enter File Name : ")
p=input("enter Password : ")
lock_pdf(file,p)
