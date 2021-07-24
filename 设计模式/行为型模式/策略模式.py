"""
策略模式
定义一系列的算法，把他们一个个的封装起来，并且使他们可以相互替换，本模式使得算法可独立于使用它的客户而变化

角色：
抽象策略
具体策略
上下文

优点：
定义了一系列可重用的算法和行为
消除了一些条件语句
可以提供相同行为的不同实现

缺点：
客户必须了解不同的策略
"""
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


class Context:
    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = "..."
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(data, s1)
context.do_strategy()
