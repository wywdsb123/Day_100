"""wang

懒得喷了，这装饰器快被我搞明白了，以后不能吃多，吃多了没脑子
"""
from functools import  wraps
import time
def timer(threshold):

    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
             start_time = time.time()
             result = func(*args,**kwargs)
             end_time = time.time()
             if end_time-start_time >threshold:
                 print(f"{func.__name__} took longer than {threshold} seconds")
             return result
        return wrapper
    return decorator
@timer(1.2)
def sleep_14():
    time.sleep(1.4)
sleep_14()
sleep_14.__wrapped__()
print(sleep_14.__name__)


