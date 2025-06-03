"""wang

读取文字
"""
import PyPDF2

reader = PyPDF2.PdfReader("test1.pdf")
for page in reader.pages:
    print(page.extract_text())

