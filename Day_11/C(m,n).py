"""wang

用于组合的
"""

# m = int (input("m="))
# n = int (input("n="))
# fm = 1
# fn = 1
# fk = 1
#
# for i in range(1,1+m):
#     fm*=i
# for i in range(1,1+n):
#     fn*=i
# for i in range(1,m-n+1):
#     fk*=i
# print(fm//fn//fk)
"""定义一个函数实现这个过程"""
def con(num):
    result = 1
    for n in range (2,num+1):
        result*=n
    return result
print(con(5))

"""but You could use from math import factorial ,whose function as same as num!"""
