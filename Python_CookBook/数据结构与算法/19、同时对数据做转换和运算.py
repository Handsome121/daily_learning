"""
同时做运算和转换
"""
import os

nums = [1, 2, 3, 4, 5, 6]
s = sum(x * x for x in nums)
print(s)

# files = os.listdir('dirname')
# if any(name.endswith('.py') for name in files):
    # print('there be python')
# else:
#     print('sorry,no python')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

