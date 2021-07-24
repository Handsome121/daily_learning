"""
回调函数中保存状态
"""


# 回调函数
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def Handler(self, result):
        self.sequence += 1
        print('[{}] Got {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.Handler)


# 可用闭包作为类的替代方案
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got {}'.format(sequence, result))

    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)


# 协程
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got {}'.format(sequence, result))


handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
