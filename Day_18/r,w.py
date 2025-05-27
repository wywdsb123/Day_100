"""wang

文件读写和异常处理
"""
file = open("致橡树.txt","r",encoding="utf_8")
print(file.read())
file.close()
file =open("致橡树.txt","r",encoding="utf_8")
for line in file :
    print(line,end="")
file.close()
file =open("致橡树.txt","r",encoding="utf_8")
lines = file.readlines()
for line in lines:
    print(line,end="")
file.close()
file = open('致橡树.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()
file = None
try:
    file = open('致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally:
    if file:
        file.close()