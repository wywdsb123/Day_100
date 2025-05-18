"""王

常用数据结构之元组
"""
a=1,23,34,45,3
i,q,*s,ew=a

print(i,q,s,ew)
"这里*代个标识词，可以指代多个元素"
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos=("王",32,True,"中国首都")
print(list(infos))
frts=["ads","qwe","qwr"]
print(tuple(frts))