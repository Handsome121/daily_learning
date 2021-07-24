"""
Python面向对象高级用法
"""


# 组合
# 把另外一个类的对象赋值给当前对象的属性，组合表达的是一种有的关系
# 定义老师类
class Teacher:
    def __init__(self, name, age, gender, level):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level


# 定义学生类
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 定义课程类
class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

    def tell(self):
        print('<{}:{}:{}>'.format(self.name, self.price, self.period))


teacher_obj = Teacher('allen', 18, 'male', 10)
student_obj = Student('lily', 12, 'female')
python_obj = Course('python', 2000, '1 month')
go_obj = Course('go', 3000, '2 month')
# 学生对象与课程做关联
student_obj.course = python_obj
student_obj.course.tell()
# 老师对象与课程做关联
teacher_obj.courses = [python_obj, go_obj]
for course_obj in teacher_obj.courses:
    course_obj.tell()

# 内置函数
# isinstance: 判断一个对象是否是一个已知的类型，类似 type()
x = 111
y = 'abc'
print(isinstance(x, int))
print(isinstance(y, str))


# issubclass: 用于判断第一个参数是否是第二个参数的子类
class foo:
    pass


class bar(foo):
    pass


print(issubclass(bar, foo))


# 内置方法（在满足某种条件下自动触发的）
# __str__方法需要返回一个字符串，当做这个对象的描写

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<{}:{}>'.format(self.name, self.age)


obj = Person('allen', 18)
print(obj)  # <allen:18>


# 析构方法，当对象在内存中被释放时(也就是实例执行完了,实例的内存就会自动释放,这时候就会触发)，自动触发执行
# 当程序结束时，python只会回收自己的内存空间，即用户态内存，而操作系统的资源则没有被回收，这就需要我们定制__del__，
# 在对象被删除前向操作系统发起关闭数据库链接的系统调用，回收资源

# 第一种情况
class foo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('del触发了')


f = foo('123')
del f.name  # 删除f.name 这个属性的时候不会触发析构方法
print('--->')


# 以上执行完后,就触发了析构方法:del触发了
# 第二种情况
class foo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('del触发了')


f = foo('123')
del f  # 删除实例对象,这时候就会触发析构方法
print('--->')


# __enter__和__exit__: 上下文管理器
class MyClass:
    def __init__(self, file_name, file_mode, file_encode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file_encode = file_encode

    def __enter__(self):
        print('只要有with,就会执行我')
        self.file = open(self.file_name, self.file_mode, encoding=self.file_encode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('只要顶格写代码,就会执行我')
        self.file.close()


# with MyClass('abc.txt', 'rt', 'utf-8') as fp:
#     print(fp.read())  # 可以读取到abc.txt文件中的内容


# __call__
# 对象后面加括号，触发执行。
# 注: 构造方法的执行是由创建对象触发的，即: 对象 = 类名(),而对于 __call__ 方法的执行是由对象后加括号触发的，即: 对象() 或者 类()()
class Dog:
    def __init__(self, name):
        self.name = name

    def __call__(self, msg):
        print('{}说了一句话: {}'.format(self.name, msg))


dog_obj1 = Dog('小黑')
dog_obj1('吃饭')  # 小黑说了一句话: 吃饭
dog_obj1('喝水')  # 小黑说了一句话: 喝水


# ---------------------------------------------------------------#
# python是动态语言，而反射(reflection)机制被视为动态语言的关键。
# 反射机制指的是在程序的运行状态中
# 对于任意一个类，都可以知道这个类的所有属性和方法
# 对于任意一个对象，都能够调用他的任意方法和属性
# 这种动态获取程序信息以及动态调用对象的功能称为反射机制

# 通过字符串来操作对象的属性，涉及到内置函数hasattr、getattr、setattr、delattr的使用(Python中一切皆对象，类和对象都可以被这四个函数操作)
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


obj = Person('allen', 18, 'male')
print(hasattr(obj, 'xxx'))
print(getattr(obj, 'xxx', None))
setattr(obj, 'xxx', 123)  # 等价于obj.xxx = 123
print(getattr(obj, 'xxx', None))  # 123
delattr(obj, 'xxx')  # 等价于del obj.xxx
print(getattr(obj, 'xxx', None))  # None
# 获取对象的属性
import re

for attr in dir(obj):
    if not re.search("^__.*__$", attr):
        res = getattr(obj, attr)
        print(res)


# 基于反射模拟实现上传下载
# class FtpServer:
#     def serve_forever(self):
#         while True:
#             inp = input('input your cmd>>: ').strip()
#             if inp == 'q':
#                 break
#             cmd, file = inp.split()
#             print(cmd, file)
#             if hasattr(self, cmd):  # 根据用户输入的cmd，判断对象self有无对应的方法属性
#                 func = getattr(self, cmd)  # 根据字符串cmd，获取对象self对应的方法属性
#                 func(file)
#
#     def get(self, file):
#         print('Downloading {}...'.format(file))
#
#     def put(self, file):
#         print('Uploading {}...'.format(file))


# server = FtpServer()
# server.serve_forever()


# 单例模式
# 单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中
# ，某个类只能出现一个实例时，单例对象就能派上用场
# 使用类方法
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


# 使用模块
# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
# 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象
# mysingleton.py
class Singleton(object):
    def foo(self):
        pass


singleton = Singleton()


# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
# from a import singleton


# 使用装饰器
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
class func:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = func(1)
obj2 = func(2)
print(obj1 is obj2)  # True
