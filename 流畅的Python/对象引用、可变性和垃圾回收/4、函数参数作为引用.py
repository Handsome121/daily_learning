"""
Python唯一支持的参数传递模式是共享传参
"""


def f(a, b):
    a += b
    print(a)


x = 1
y = 2
f(x, y)
print((x, y))
a = [1, 2]
b = [3, 4]
f(a, b)
print((a, b))  # a 变了
# 传入可变，修改可变，无需return
t = (1, 2)
u = (3, 4)
f(t, u)
print((t, u))  # a 没变


# 不能使用可变类型作为参数的默认值
class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# 防御可变参数
class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# 正确做法
# 防御可变参数
class TwilightBus:
    """让乘客销声匿迹的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            # 如果不想改变传入的可变对象,传入可变对象一般要把副本给类对象的init方法，
            # 类的创建者和使用者一定要提前沟通好传入的参数需不需要动态改变

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)

# 审查HauntedBus.__init__对象
print(dir(HauntedBus.__init__))
print(HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)
