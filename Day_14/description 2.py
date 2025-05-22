import time

def timer_decorator_perf(func):
    def wrapper(*args,**kwargs):
        start = time.perf_counter() # 使用 perf_counter
        result = func(*args,**kwargs)
        end = time.perf_counter()   # 使用 perf_counter
        print(f"{func.__name__} 执行耗时: {end - start:.13f}秒")
        return result
    return wrapper

@timer_decorator_perf
def square(x):
    return x * x

@timer_decorator_perf
def square_loop_short(x): # 即使是一个短循环，perf_counter也可能捕捉到
    res = 0
    for _ in range(100):
        res += x * x
    return res / 100

square(10)
square_loop_short(10)