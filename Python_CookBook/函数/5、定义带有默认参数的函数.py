"""
定义一个函数或者方法，其中有一个或多个参数是可选的并且带有默认值
"""


def spam(a, b=42):
    print(a, b)


spam(1)


# 如果默认值是可变容器，那么应该把None作为默认值，代码应该这样子写
def spam1(a, b=None):
    if b is None:
        b = []


# 如果不打算提供一个默认值，只是想通过代码来检测可选参数是否被赋予了某个特定的值，那么可以采用下面的惯用手法
_no_value = object()


def spam2(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
