"""wang

可变参数的遍历
"""
def add(*args):
    total = 0
    for val in args:
        if type(val) in (int , float):
            total += val
    return total
def foo (*args,**kwargs):
    print(args)
    print(kwargs)
