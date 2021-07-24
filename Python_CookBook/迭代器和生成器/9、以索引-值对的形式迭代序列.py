"""
我们迭代一个序列，但是又想记录下序列当中当前处理到的元素索引
"""

# my_list = ['a', 'b', 'c']
# for idx, val in enumerate(my_list):
#     print(idx, val)
# 如果要打印出规范的行号
# for idx, val in enumerate(my_list, 1):
#     print(idx, val)
from collections import defaultdict


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}:Parse error:{}'.format(lineno, e))


word_summary = defaultdict(list)  # 字典中的键查询不存在时，返回一个列表
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        words = [word.strip().lower() for word in line.split()]
    for word in words:
        word_summary[word].append(idx)
