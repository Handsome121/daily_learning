"""
在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8, 6}是峰，
 {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。
"""


def wiggleSort(nums):
    for i in range(len(nums) - 1):
        # 谷在奇数索引,峰在偶数索引
        if i % 2 == 0:
            if nums[i + 1] > nums[i]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
        else:
            if nums[i + 1] < nums[i]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
