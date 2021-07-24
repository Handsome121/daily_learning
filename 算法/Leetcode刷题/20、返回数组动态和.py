"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。
"""
from itertools import accumulate


def runningSum(nums):
    # res = []
    # if not nums:
    #     return []
    # for i in range(1, len(nums)):
    #     total = sum(nums[:i])
    #     res.append(total)
    # return res
    return list(accumulate(nums))


nums = [0, 2, 1, 4, 5, 6, 7, 8, 9, 10]
res = runningSum(nums)
print(res)
