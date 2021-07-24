"""
你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目
"""
from itertools import permutations


def numTilePossibilities(tiles: str) -> int:
    ans = set()
    for i in range(1, len(tiles) + 1):
        for j in permutations(tiles, i):
            ans.add(j)
    return len(ans)
