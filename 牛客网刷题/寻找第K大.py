"""
有一个整数数组，请你根据快速排序的思路，找出数组中第K大的数。
给定一个整数数组a,同时给定它的大小n和要找的K(K在1到n之间)，请返回第K大的数，保证答案存在。
"""
import heapq


def get_k_largest(nums, k):
    num = heapq.nlargest(k, nums)
    result = num[k - 1]
    return result


nums = [1, 3, 5, 2, 2]
print(get_k_largest(nums, 3))
