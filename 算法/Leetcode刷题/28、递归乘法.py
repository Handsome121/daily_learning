"""
递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。
"""


def multiply(A: int, B: int) -> int:
    """
    递归乘法
    :param self:
    :param A:
    :param B:
    :return:
    """
    # 将A设置为较小的数
    if A > B:
        A, B = B, A
    res = 0
    for i in range(A):
        res += B
    return res


if __name__ == '__main__':
    res = multiply(5, 4)
    print(res)
