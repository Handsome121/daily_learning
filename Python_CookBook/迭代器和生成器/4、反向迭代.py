"""
反向迭代元素
"""


# a = [1, 2, 3, 4, 5]
# for x in reversed(a):
#     print(x)


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """正向迭代"""
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reverse__(self):
        """反向迭代"""
        n = 1
        while n <= self.start:
            yield n
            n += 1


a = Countdown(5)
for i in a:
    print(i)
