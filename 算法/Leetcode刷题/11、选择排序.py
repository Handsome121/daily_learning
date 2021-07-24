"""
这应该最符合人类思维的排序方法，工作原理，首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小
（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
稳定性：稳定；内排序
"""


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
