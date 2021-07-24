"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
"""
from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    """
    重排数组
    :param nums:
    :param n:
    :return:
    """
    x = nums[:n]
    y = nums[n:]
    result = []
    for i in range(n):
        result.append(x[i])
        result.append(y[i])
    return result


nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)
