"""
组合模式:将对象组合成树形结构以表示“部分-整体”的层次结构，组合模式使得用户对单个对象和组合对象的使用具有一致性。

角色：
1、抽象组件
2、叶子组件
3、复合组件
4、客户端
"""
from abc import ABCMeta, abstractmethod, ABC


class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点(%s,%s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段(%s,%s)" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for i in iterable:
            self.add(i)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("-----复合图形-----")
        for g in self.children:
            g.draw()
        print("-----复合图形-----")


p1 = Point(2, 3)
l1 = Line(Point(3, 4), Point(5, 6))
l2 = Line(Point(5, 6), Point(8, 9))
pic1 = Picture([p1, l1, l2])
pic1.draw()
