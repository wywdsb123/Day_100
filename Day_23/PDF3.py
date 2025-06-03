"""wang

加密PDF文件
"""
import PyPDF2
reader = PyPDF2.PdfReader("test.pdf")
writer = PyPDF2.PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("xuge")

with open("temp2.pdf","wb") as file_obj:
    writer.write(file_obj)