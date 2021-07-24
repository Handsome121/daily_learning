"""
对不同的容器产生相同的迭代操作
"""
from itertools import chain

a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c']
for x in chain(a, b):
    print(x)
