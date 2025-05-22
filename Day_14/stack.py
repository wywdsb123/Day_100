"""wang

递归调用
"""
import time


def fib(n):
    if n in (0,1):
        return 1
    return n*fib(n-1)#阶乘

def fib1(n):
    if n in (1,2):
        return 1
    return fib1(n-1)+fib1(n-2)#斐波那契数列
start_time=time.time()
for i in range(1,21):
    print(fib1(i))
end_time = time.time()
print(end_time-start_time) #慢的要死

def fib2(n):
    a,b=0,1
    for _ in range (n):
        a,b =b,a+b
        return a

from functools import lru_cache

@lru_cache()
def fib3(n):
    if  n in (1,2):
        return 1
    return fib3(n-1)+fib3(n-2)
for i in range(1,51):
    print(i,fib3(i))
