"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
"""


def countDigitone(n):
    """
    1出现的次数
    :param n:输入的正整数
    :return:1出现的次数
    """
    c = 0
    for i in range(1, n + 1):
        str_num = str(i)
        for j in str_num:
            if j == '1':
                c += 1
            else:
                continue
    return c


c = countDigitone(5)
print(c)
