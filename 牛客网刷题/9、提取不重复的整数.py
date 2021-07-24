"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0
"""
n = input()
res = ""
for i in range(len(n) - 1, -1, -1):
    if n[i] not in res:
        res += n[i]
print(res)
