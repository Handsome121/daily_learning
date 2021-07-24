def lcm(x, y):
    """
    最小公倍数算法
    :param x:
    :param y:
    :return:
    """
    # 获取最大的数
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm
