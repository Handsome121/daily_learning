"""
在子类中扩展某个属性的功能
"""


class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("can't delete a attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete(self)


# 如果只想扩展属性中的一个方法，可以使用下面的代码实现
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


# 对描述符也同样适用
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        instance.__dict__[self.name] = value


class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete(self)
