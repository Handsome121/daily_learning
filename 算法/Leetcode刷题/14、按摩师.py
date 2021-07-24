"""
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
"""


def message(nums):
    if not nums:
        return 0
    n = len(nums)
    # 初始化dp列表
    # 这里难点在于理解dp[i]=x 到dp[i]为止目前最长的预约时间为x
    dp = [0] * n
    for i in range(n):
        if n == 0:
            dp[i] = nums[i]
        elif n == 1:
            dp[i] = max(nums[0], nums[1])
        else:
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])  # 核心
    return max(dp)


if __name__ == '__main__':
    nums = [1, 2, 5, 7, 3, 4]
    max_message = message(nums)
    print("最长预约时间为%s" % max_message)
