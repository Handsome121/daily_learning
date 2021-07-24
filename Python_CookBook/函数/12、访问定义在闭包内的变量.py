"""
访问定义在闭包内的变量
"""
#
#
# def sample():
#     n = 0
#
#     def func():
#         print('n =', n)
#
#     def get_n():
#         return n
#
#     def set_n(value):
#         nonlocal n
#         n = value
#
#     # 作为函数属性来附加
#     func.get_n = get_n
#     func.set_n = set_n
#     return func
#
#
# f = sample()
# f()
# f.set_n(10)
# f()
# f.get_n()
# f()
import sys


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']


def stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = stack()
print(s)


class stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

