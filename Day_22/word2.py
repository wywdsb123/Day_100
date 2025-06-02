"""wang

阅读一个docx"""
from docx import Document
from docx.document import Document as Doc
doc = Document("离职证明.docx")
for no , p in enumerate(doc.paragraphs):
    print(no,p.text)