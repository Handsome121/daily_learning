def hcf(x, y):
    """
    该函数返回两个数的最大公约数
    :param x:
    :param y:
    :return:
    """
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i) == 0 and (y % i == 0):
            hcf = i
    return hcf
