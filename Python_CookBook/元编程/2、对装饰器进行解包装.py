"""
对装饰器解包装
"""
import time
from functools import wraps


def decorator1(func):
    """Decorator that reports the execution time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    """Decorator that reports the execution time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


# res = add(2, 3)
res2 = add.__wrapped__(2, 3)
# print(res)
print(res2)
