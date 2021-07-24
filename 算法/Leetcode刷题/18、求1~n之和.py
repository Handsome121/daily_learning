"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句
"""


def Sum(n):
    """
    求1~n之和
    :param n:
    :return:
    """
    return sum(range(1, n + 1))


print(Sum(10))
