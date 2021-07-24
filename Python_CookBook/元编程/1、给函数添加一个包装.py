"""
我们想给函数加上一个包装层以添加额外的处理
"""
import time
from functools import wraps


def timethis(func):
    """Decorator that reports the execution time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


result = countdown(10)
print(dir(countdown))

