"""王

常用数据结构之字符串
"""
"""

字符串比较运算
比较的是首字母的编码数字的大小
.capitalize()#字符串首字母大写，title()#每个单词首字母大写.upper（）#字符串大写.lower（）#小写
startswith()判断是否以字符串开头，endswith（）同理.
"""
s= "hello"
for i in range(len(s)):
    print(s[i],end="\t")
print("\n")
s="hello"
for i in s:
    print(i,end=" ")
print("\t")
print(s.find("lo",34))
print(s.center(20,"*"))#还有center，ljust，rjust，zfill
print("{}*{}={}".format(12,34,23))
s1 = '   jackfrued@126.com  1'
print(s1.strip())


