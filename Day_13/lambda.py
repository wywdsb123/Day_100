"""wang

匿名函数
"""
# old_nums = [35, 12, 8, 99, 60, 52]
# new_nums = list(map(lambda x:x**2,filter(lambda x:x%2 == 0,old_nums)))
# print(new_nums)
import functools
import operator

# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)
# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
# 调用Lambda函数
print(fac(6))        # 720
print(is_prime(37))  # True