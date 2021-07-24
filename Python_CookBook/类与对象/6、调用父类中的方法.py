"""
调用父类的方法
"""


# 调用父类中的方法
class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


# 常见用途是调用父类中的__init__()方法
class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


# 另一种常见用途是当覆盖了Python中的特殊方法时
class Proxy:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, name):
        return getattr(self.obj, name)

    def __setattr__(self, name, value):
        if name.endswith('-'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)
