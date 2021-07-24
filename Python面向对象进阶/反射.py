"""
反射
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("walking......")


def talk(self):
    print(self.name, "is talking")


p = Person('Alex', 22)
if hasattr(p, "name"):
    print("name属性存在")
# 反射、映射、自省
# getattr()
# a = getattr(p, "age")
# print(a)
# # hasattr()
# user_command = input(">>:").strip()
# if hasattr(p, user_command):
#     func = getattr(p, user_command)
#     func()
#
# # setattr()
# # 给实例增加属性
# setattr(p, "sex", "Female")
# print(p.sex)
# # 给实例增加方法
# setattr(p, "speak", talk)
# p.speak(p)
#
# setattr(Person, "speak2", talk)
# p.speak2()
# # delattr()
#
# delattr(p, "age")
# print(p.age)


# getattr("反射.py", "p")
# print(__name__)  # __main__就代表模块本身
# # 在当前模块主动执行的情况下（不是被导入执行），等于__main__
# # 在被其他模块导入的情况下，等于模块名
# if __name__ == '__main__':  # 只会在被别的模块导入的时候发挥作用
#     print("你好!")
import sys

# for k, v in sys.modules.items():
#     print(k, v)
# mod = sys.modules[__main__]
mod = sys.modules[__name__]
if hasattr(mod, "p"):
    o = getattr(mod, "p")
    print(o)
print(p)
