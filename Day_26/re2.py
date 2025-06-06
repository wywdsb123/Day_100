"""wang

学习re正则表达式
"""
import re
pattern = re.compile(r"(?<=\D)1[345678]\d{9}(?=\D)")
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
tels_list = re.findall(pattern,sentence)
for tel in tels_list:
    print(tel)
print("_"*20)
for temp in pattern.finditer(sentence):
    print(temp.group())
print("-"*20)
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence,m.end())

