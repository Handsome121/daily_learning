"""
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出
"""
n = int(input())
d = {}
for i in range(n):
    ab = input().split(" ")
    a, b = int(ab[0]), int(ab[1])
    if a not in d:
        d[a] = b
    elif a in d:
        d[a] = d[a] + b
for i in sorted(d.keys()):
    print(i, d[i])
