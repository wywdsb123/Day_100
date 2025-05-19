"""wang

判断三角形
"""
# def judgement(a,b,c):
#     return a + b > c and b + c > a and a + c > b
# a= int(input(":"))
# c= int(input(":"))
# b= int(input(":"))
# print(judgement(a,b,c))


# /前面的参数是强制位置参数
"""/强制位置参数"""
def make_judgement(a, b, c, /):
    return a + b > c and b + c > a and a + c > b

# 下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
# TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
# print(make_judgement(b=2, c=3, a=1))
print(make_judgement(b=2, c=3, a=1))  # False
print(make_judgement(c=6, b=4, a=5))  # True
"""*命名关键字参数"""
def make_judgement(*,a,b,c):
    return a + b > c and b + c > a and a + c > b
print(make_judgement(b=2, c=3, a=1))  # False
print(make_judgement(c=6, b=4, a=5))
