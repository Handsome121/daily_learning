"""
迭代多个序列
"""
from itertools import zip_longest

xpts = [1, 5, 4, 2, 2, 3, 4]
ypts = [3, 4, 6, 7, 8, 6]
for x, y in zip_longest(xpts, ypts, fillvalue=0):
    print(x, y)
# 一长一短就不是我们所需要的
