"""
冒泡排序时针对相邻元素之间的比较，可以将大的数慢慢“沉底”(数组尾部)
"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
