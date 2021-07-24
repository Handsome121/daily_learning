# property

```Python
class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age_fun(self):
         return self.__age

    def set_age_fun(self, value):
        if not isinstance(value, int):
            raise ValueError('年龄必须是数字!')
        if value < 0 or value > 100:
            raise ValueError('年龄必须是0-100')
        self.__age = value

    def print_info(self):
        print('%s: %s' % (self.__name, self.__age))


p = Person('balala',20)
p.__age = 17
print(p.__age) # 17
print(p.get_age_fun()) # 20 表面上看，上面代码“成功”地设置了__age变量 17,但实际上这个__age变量和class内部的__age变量不是一个变量！
# 内部的__age变量已经被Python解释器自动改成了_Person_age，而外部代码给p新增了一个__age变量。 所以调用 get_age_fun输出的是初始值

p.set_age_fun(35)
print(p.get_age_fun()) # 35

print(p.print_info()) # balala: 35
```

```Python
class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def get_age_fun(self):
         return self._age

    def set_age_fun(self, value):
        if not isinstance(value, int):
            raise ValueError('年龄必须是数字!')
        if value < 0 or value > 100:
            raise ValueError('年龄必须是0-100')
        self._age = value

    def print_info(self):
        print('%s: %s' % (self.__name, self._age))


p = Person('balala',20)
p._age = 17
print(p._age) # 17
print(p.get_age_fun()) # 这里是17 不再是 20,因为此时_age是全局变量,外部直接影响到类内部的更新值

p.set_age_fun(35)
print(p.get_age_fun()) # 35

print(p.print_info()) # balala: 35
```

看的出私有和全局的设置

但是，上面的调用方法是不是略显复杂，没有直接用属性这么直接简单。

有没有可以用类似属性这样简单的方式来访问类的变量呢？必须的，对于类的方法
我们先来看一个稍微改造的例子：（稍后我们再使用Python内置的`@property`装饰器就是负责把一个方法变成属性调用.）

```Python
class Person(object):
 2     def __init__(self, name, age):
 3         self.__name = name
 4         self.__age = age
 5 
 6     @property
 7     def get_age_fun(self):
 8          return self.__age
 9 
10     @get_age_fun.setter # get_age_fun是上面声明的方法
11     def set_age_fun(self, value):
12         if not isinstance(value, int):
13             raise ValueError('年龄必须是数字!')
14         if value < 0 or value > 100:
15             raise ValueError('年龄必须是0-100')
16         self.__age = value
17 
18     def print_info(self):
19         print('%s: %s' % (self.__name, self.__age))
20 
21 
22 p = Person('balala',20)
23 p.__age = 17
24 print(p.__age) # 17
25 print(p.get_age_fun) # 20 注意这里不带()
26 
27 #p.set_age_fun(35) 注意不能这样调用赋值了
28 p.set_age_fun = 35 #  这里set_age_fun 就是 声明的函数不带()
29 print(p.get_age_fun) # 35
30 print(p.print_info()) # balala: 35
```