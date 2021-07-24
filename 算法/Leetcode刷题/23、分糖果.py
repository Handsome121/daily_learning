"""
给你一个数组candies和一个整数extraCandies其中candies[i]代表第i个孩子拥有的糖果数目。
对每一个孩子，检查是否存在一种方案，将额外的extraCandies个糖果分配给孩子们之后，此孩子有最多的糖果。注意，允许有多个孩子同时拥有最多的糖果数目。
"""
from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maxi = max(candies)
    judge = []
    for i in candies:
        judge.append(i + extraCandies >= maxi)
    return judge
