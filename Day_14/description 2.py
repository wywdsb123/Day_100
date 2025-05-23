"""wang

练习
"""
import time



def suqare(n):
    return n*n
def decorator(func):
    def wrapper(*args,**kwargs):
         start_time = time.time()
         result = func(*args,**kwargs)
         time.sleep(1)
         end_time = time.time()
         print(f"一共耗时{end_time-start_time:.10f}")
         return result

    return wrapper
s2uqare = decorator(suqare)
s2uqare(10)



# def timer_decorator_perf(func):
#     def wrapper(*args,**kwargs):
#         start = time.perf_counter() # 使用 perf_counter
#         result = func(*args,**kwargs)
#         end = time.perf_counter()   # 使用 perf_counter
#         print(f"{func.__name__} 执行耗时: {end - start:.13f}秒")
#         return result
#     return wrapper
#
# @timer_decorator_perf
# def square(x):
#     return x * x
#
# @timer_decorator_perf
# def square_loop_short(x): # 即使是一个短循环，perf_counter也可能捕捉到
#     res = 0
#     for _ in range(100):
#         res += x * x
#     return res / 100
#
# square(10)
# square_loop_short(10)
