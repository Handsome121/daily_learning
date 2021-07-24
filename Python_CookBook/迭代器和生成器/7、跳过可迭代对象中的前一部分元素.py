"""
跳过可迭代对象中的前一部分元素
"""
from itertools import islice, dropwhile

with open('/etc/passwd') as f:
    for line in f:
        print(line, end='')
# 跳过注释行
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startwith('#'), f):
        print(line, end='')

# 如果是恰巧知道跳过多少个元素，可以使用itertools.islice()
items = ['a', 'b', 'c', 1, 2, 3, 4]
for x in islice(items, 3, None):
    print(x)

# 生成器表达式
with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
