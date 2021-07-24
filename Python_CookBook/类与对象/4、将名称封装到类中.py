"""
将名称封装到类中
"""


# 单下划线打头的名字被认为只属于内部实现
class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


# 双下划线打头的名称回导致出现名称重整的行为

class A:
    def __init__(self):
        self.__private = 0
        self.public = 1

    def public_method(self):
        self.__private_method()

    def __private_method(self):
        pass
# 这个类中的私有属性会被重命名为_B__private和_B__private_method
