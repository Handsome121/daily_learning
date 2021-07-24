"""
创建大量实例时如何节省内存
"""


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, day, month):
        self.year = year
        self.month = month
        self.day = day
