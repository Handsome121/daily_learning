"""
给你一个整数数组 nums
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对
返回好数对的数目。
"""


def numIdenticalPairs(nums):
    num = 0
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i < j:
                num += 1
    return num


nums = [1, 1, 1, 1]
num = numIdenticalPairs(nums)
print(num)
