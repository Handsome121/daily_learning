"""
找出最大或最小的N个元素-------堆数据结构
"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

protfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 52.3},
    {'name': 'FB', 'shares': 200, 'price': 68.5},
    {'name': 'HPQ', 'shares': 300, 'price': 53.6},
    {'name': 'YHOO', 'shares': 400, 'price': 85.3},
    {'name': 'ACME', 'shares': 600, 'price': 89.6}
]
cheap = heapq.nsmallest(3, protfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, protfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)
