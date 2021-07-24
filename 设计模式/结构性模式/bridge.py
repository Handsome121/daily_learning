"""
桥模式

角色：
1、抽象
2、细化抽象
3、实现者
4、具体实现者

应用场景：当事物有两个维度上的表现，两个维度都可能扩展时

优点：
1、抽象和实现相分离
2、优秀的扩展能力
"""

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        pass


shape = Rectangle(Red())
shape.draw()
