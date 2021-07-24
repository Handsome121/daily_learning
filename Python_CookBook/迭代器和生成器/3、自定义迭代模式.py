"""
自定义迭代模式
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for i in frange(0, 4, 0.5):
    print(i)
