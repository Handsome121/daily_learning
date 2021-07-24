"""
单例模式：保证一个类只有一个实例，并提供一个访问它的全局访问点

角色：单例

优点：
1、对唯一实例的受控访问
2、单例相当于全局变量，但防止了命名空间被污染
"""
from abc import abstractmethod, ABCMeta


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Myclass(Singleton):
    def __init__(self, a):
        self.a = a


a = Myclass(10)
b = Myclass(20)
print(a.a)
print(b.a)
print(a is b)


# 单例模式的三种写法
class Foo:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = cls()
            return cls.__instance


obj1 = Foo().get_instance()
obj2 = Foo().get_instance()
print(obj1 is obj2)  # True


def outter(func):
    _instance = {}

    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)
        return _instance[func]

    return wrapper


@outter
class A:
    a = 1

    def __init__(self, x=0):
        self.x = x


a = A(111)
b = A(222)
print(a is b)  # True


# 使用元类
class Func:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Func(1)
obj2 = Func(2)
print(obj1 is obj2)  # True


