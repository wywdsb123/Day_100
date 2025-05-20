"""wang

高阶函数的运用
"""
def calc1(*args,**kwargs):
    items = list(args)+list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int,float):
            result+=item
    return result
def calc2(init_value,op_func,*args,**kwargs):
    items = list(args)+list(kwargs.values())
    result = init_value
    for item in items:
        if type (item) in (int,float):
            result = op_func(result,item)
    return result
import operator
print(calc2(0,operator.add,1,2,3,4,5))
print(calc2(1,operator.mul,1,2,3,4,5))

def is_even(num):
    return num%2 == 0
def square(num):
    return num**2
