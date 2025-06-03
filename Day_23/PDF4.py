"""wang

加水印
"""
import PyPDF2
reader1 = PyPDF2.PdfReader('test1.pdf')
reader2 = PyPDF2.PdfReader('水印.pdf')
writer = PyPDF2.PdfWriter()
watermark_page = reader2.pages[0]

for page in reader1.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open('temp3.pdf', 'wb') as file_obj:
    writer.write(file_obj)