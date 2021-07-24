"""
筛选序列中的元素
"""
# 列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
mylist2 = [n for n in mylist if n > 0]
mylist3 = [n for n in mylist if n < 0]
print(mylist2)
print(mylist3)
# 生成器表达式
pos = (n for n in mylist if n > 0)
print(list(pos))
# 使用函数做更高级的筛选
values = ['1', '2', '3', '-', 'N/A', '-8', 6]


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

clip_neg = [n if n > 0 else 0 for n in mylist]
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_neg)
print(clip_pos)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N REVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))
# 类似于布尔选择器
