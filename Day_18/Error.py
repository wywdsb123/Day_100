"""wang

自定义异常类型
"""
class InputError(ValueError):
 pass
def fac(num):
    if not isinstance(num, int) or num<0:
        raise InputError("只能计算非负整数的阶乘")
    if num in (0,1):
        return 1
    return num*fac(num-1)
flag =True
while flag:
    num = int(input("n="))
    try:
        print(f"{num}!={fac(num)}")
        flag = False
    except InputError as err:
        print(err)
