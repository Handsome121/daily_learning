# Python动态绑定属性slots的使用

```
class Person(object):
    pass

p = Person()
p.name = 'mary' # 动态给实例绑定一个属性
print(p.name)
```

```
class Person(object):
    pass

def set_sex(self, sex): # 定义一个函数作为实例方法
    self.sex = sex

from types import MethodType
p = Person()
p.set_sex_fun = MethodType(set_sex, p) # 给实例绑定一个方法 set_sex_fun新的属性方法，自定义,MethodType第一个参数为已定义的方法名set_sex,第二个参数为类实例 Person()
p.set_sex_fun('female') # 调用实例方法
print(p.sex) # female
```

**这里需要注意：**给一个实例绑定的方法，对另一个实例是不起作用的：

```
p2 = Person() # 创建新的实例
p2.set_sex_fun('male') # 尝试调用方法
```

为了给所有实例都绑定方法，如何实现呢？我们可以这样给class绑定方法：

```
class Person(object):
    pass

def set_sex(self, sex):
    self.sex = sex

Person.set_sex_fun = set_sex  # 属性set_sex_fun 自定义, 方法名set_sex 不带()

p = Person()
p.set_sex_fun('female')
print(p.sex) # female

p2 = Person() # 创建新的实例
p2.set_sex_fun('male')
print(p2.sex) # male
```

通常情况下，上面的`set_sex`方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现.

这里我们步入核心正题：

### __slots__

如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加`name`和`sex`属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性

```
class Person(object):
    __slots__ = ('name', 'sex') # 用tuple定义允许绑定的属性名称

p = Person()
p.name = 'Mary' # 绑定属性'name'
p.sex = 'female' # 绑定属性'sex'
p.age = 19 # 绑定属性'age'
```

```
Traceback (most recent call last):
  File "run.py", line 7, in <module>
    p.age = 19 # 绑定属性'age'
AttributeError: 'Person' object has no attribute 'age'
```

由于`'age'`没有被放到`__slots__`中，所以不能绑定`age`属性，试图绑定age将得到`AttributeError`的错误。

使用`__slots__`要注意，`__slots__`定义的属性**仅对当前类实例起作用，对继承的子类是不起作用的。**

```
class Person(object):
    __slots__ = ('name', 'sex') # 用tuple定义允许绑定的属性名称

class Son(Person):
    pass

s = Son()
s.age = 19 # 绑定属性'age'
print(s.age) # 19
```

除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`

```
class Person(object):
    __slots__ = ('name', 'sex') # 用tuple定义允许绑定的属性名称

class Son(Person):
    __slots__ = ('skill', 'age')  # 用tuple定义允许绑定的属性名称

s = Son()
s.name = 'Kaven' # 绑定属性'name'
print(s.name) # Kaven

s.age = 19 # 绑定属性'age'
print(s.age) # 19
```