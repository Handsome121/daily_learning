"""
修改实例的字符串表示
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """面向计算机"""
        return 'Pair({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        """面向用户"""
        return '({0.x!r},{0.y!r})'.format(self)
