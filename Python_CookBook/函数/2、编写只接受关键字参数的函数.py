"""
我们希望函数只通过关键字的形式接受特定的参数
"""


def func01(a: int, *, b: str):
    """
    receives a message
    :param a: int
    :param b: int
    :return: int
    """
    pass


def func02(a, *values, b):
    """receives a message"""
    pass


print(func01.__annotations__)
