"""wang

修饰器修饰语句
"""
# def record_time(func):
#     def wrapper(*arys,**kwarys):
#         result =func(*arys,**kwarys)
#         return result
#     return wrapper
import random
import random # random 模块在这里没有被使用，可以移除
# import time
#
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         # 为了测量短时间，time.perf_counter() 通常比 time.time() 更精确
#         start_time = time.perf_counter()
#         result = func(*args,**kwargs) # 执行原函数
#         end_time = time.perf_counter()
#         print(f"{func.__name__} 执行时间：{end_time-start_time:.12f}秒")
#         return result # 返回原函数的结果
#     return wrapper
#
# @decorator
# def add(x, u):
#     time.sleep(1)
#     return x * u
#     # print(add(x,u))  # <--- 这行是错误的，并且在return之后，永远不会执行
#
# # 调用函数并获取结果
# result_of_add = add(3, 5)
# print(f"add(3, 5) 的计算结果是: {result_of_add}") # 打印函数返回的结果

import random
import time

from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
         start_time=time.time()
         result = func(*args,**kwargs)
         end_time = time.time()
         print(f"{func.__name__}执行时间：{end_time-start_time:.2f}")
         return result
    return wrapper
@decorator
def download(filename):
    print(f"开始下载{filename}。")
    time.sleep(random.random()*6)
    print(f"下载完成")
@decorator
def upload(filename):
    print(f"开始上传{filename}")
    time.sleep(random.random()*8)
    print(f"上传完成")
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')


