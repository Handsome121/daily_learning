"""
使用分治算法解题的一般步骤如下。
① 分解，将要解决的问题划分成若干个规模较小的同类问题。
② 求解，当子问题划分得足够小时，用较简单的方法解决。
③ 合并，按原问题的要求，将子问题的解逐层合并构成原问题的解。
"""


def get_max(max_list):
    """
    求顺序表中的最大值
    :param max_list:
    :return:
    """
    return max(max_list)


def solve2(init_list):
    """
    分治法,版本二
    :param init_list:
    :return:
    """
    n = len(init_list)
    if n <= 2:
        return get_max(init_list)
    # 分解
    left_list, right_list = init_list[:n // 2], init_list[n // 2:]
    # 递归（树）,分治
    left_max, right_max = solve2(left_list), solve2(right_list)
    # 合并
    return get_max([left_max, right_max])


def partition(seq):
    """
    找出一组序列中第K小的元素
    :param seq:
    :return:
    """
    pi = seq[0]  # 挑选主元
    lo = [x for x in seq[1:] if x <= pi]  # 所有小的元素
    hi = [x for x in seq[1:] if x > pi]  # 所有大的元素
    return lo, pi, hi


def select(seq, k):
    """
    查找第K小的元素
    :param seq:
    :param k:
    :return:
    """
    # 分解
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi, k - m - 1)  # 递归（树），分治
    else:
        return select(lo, k)  # 递归（树），分治


if __name__ == '__main__':
    # 测试数据
    test_list = [21, 23, 56, 12, 54, 85, 47, 86, 99, 5, 66, 33, 65, 36, 32, 31, 52, 63, 95, 68, 97, 54, 62]
    print(solve2(test_list))
    print(select(test_list, 3))
