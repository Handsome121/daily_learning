def add(a, b):
    """
    不用加号的加法
    :param a:
    :param b:
    :return:
    """
    nums = []
    nums.append(a)
    nums.append(b)
    c = sum(nums)
    return c


if __name__ == '__main__':
    c = add(1, 2)
    print("两数之和为%s" % c)
