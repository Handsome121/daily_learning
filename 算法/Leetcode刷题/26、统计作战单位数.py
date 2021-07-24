"""
n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。
每 3 个士兵可以组成一个作战单位，分组规则如下：
从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。
"""
from typing import List, Tuple


def numTeams(rating: List[int]) -> int:
    """
    统计作战单位数
    :param rating:评分数组
    :return:
    """
    num = 0
    for i in range(len(rating) - 2):
        for j in range(i + 1, len(rating) - 1):
            for k in range(j + 1, len(rating)):
                if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                    num += 1
    return num


rating = [1, 2, 3, 4]
res = numTeams(rating)
print(res)
