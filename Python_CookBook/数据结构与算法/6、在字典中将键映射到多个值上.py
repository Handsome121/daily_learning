"""
一键多值
"""
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)

d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
# 可以使用defaultdict进行代码优化
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
