"""
对一系列元素的所有可能的组合或排列进行迭代
"""
from itertools import permutations, combinations, combinations_with_replacement

# 接受一个元素集合，进行全排列，并以元组形式返回
items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)
# 如果想要得到较短长度的所有全排列，可以提供一个可选的长度参数
for p in permutations(items, 2):
    print(p)

# 可产生输入序列中的所有元素的全部组合形式,不予考虑元素之间的实际顺序
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)
for c in combinations(items, 1):
    print(c)

# 解除上述限制

for c in combinations_with_replacement(items,3):
    print(c)