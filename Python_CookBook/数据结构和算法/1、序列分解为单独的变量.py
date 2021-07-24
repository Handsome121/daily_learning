"""
将包含N个元素的元组和序列，现在想将它分解为N个单独的变量
"""
# 拆包
p = (4, 5)
x, y = p
print(x)
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
# 只要对象是可迭代的，那么就可以执行分解操作
_, shares, price, _ = data
print(shares)
