"""wang

随机验证码的产生
"""
import random
import string
All_CHARS = string.digits + string.ascii_letters

def generate_code(*,code_len=4): #*表明必须添加参数名
    return "".join(random.choices(All_CHARS,k=code_len))

for _ in range(5):
    print(generate_code(code_len=9))

