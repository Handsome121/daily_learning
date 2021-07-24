"""
给出一个整数数组，请在数组中找出两个加起来等于目标值的数，
"""


def get_index(nums, sums):
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == sums:
                return i + 1, j + 1


if __name__ == '__main__':
    nums = [20, 70, 110, 150]
    print(get_index(nums, 90))
