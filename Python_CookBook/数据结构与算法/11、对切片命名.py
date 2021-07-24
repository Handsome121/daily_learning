"""
对切片命名
"""
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = slice(2, 4)
print(items[a])
items[a] = [11, 12]
print(items)
del items[a]
print(items)

a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
