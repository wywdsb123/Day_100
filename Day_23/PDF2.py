"""wang

pdf的创建
"""
import PyPDF2
reader = PyPDF2.PdfReader('test.pdf')
writer = PyPDF2.PdfWriter()

for no, page in enumerate(reader.pages):
    if no % 2 == 0:
        new_page = page.rotate(-90)
    else:
        new_page = page.rotate(90)
    writer.add_page(new_page)

with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)