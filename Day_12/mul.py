"""wang

最大公约数与最小公倍数的计算
"""
def lcm(x:int, y:int) ->int:
    return x*y//gcd(x,y)
def gcd(x:int,y:int) ->int:
    while y % x != 0:
        y , x = x, y%x
    return x
m,n=int(input("")),int(input(""))
print(lcm(m,n))