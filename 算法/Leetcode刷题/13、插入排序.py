"""
插入排序是前面已排序数组找到插入的位置
"""


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1
    return nums
