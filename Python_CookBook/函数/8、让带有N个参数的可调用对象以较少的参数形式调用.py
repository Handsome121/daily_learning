"""
较少函数调用时参数的传递数量
"""
from functools import partial

#
#
# def spam(a, b, c, d):
#     print(a, b, c, d)
#
#
# s1 = partial(spam, 1)
# s1(2, 3, 4)
# s2 = partial(spam, 1, 2, d=23)
# s2(3)
import math

points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)
