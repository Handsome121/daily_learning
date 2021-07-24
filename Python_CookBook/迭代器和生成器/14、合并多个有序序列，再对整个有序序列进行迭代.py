"""
有一组有序序列，想对他们合并在一起之后的有序序列进行迭代
"""
import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
