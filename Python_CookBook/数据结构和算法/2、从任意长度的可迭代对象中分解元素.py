"""
从可迭代对象中分解出N个元素
"""


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


grades = [0, 12, 3, 4, 5, 6, 7, 78]
middle = drop_first_last(grades)
print(middle)
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
trailing, *current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
