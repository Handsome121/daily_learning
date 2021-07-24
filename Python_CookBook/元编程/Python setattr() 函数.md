# Python setattr() 函数

```
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)
```

```
setattr(object, attribute, value)
```

setattr() 函数指定对象的指定属性的值

# Python delattr() 函数

```
class Person:
  name = "Bill"
  age = 63
  country = "USA"

delattr(Person, 'age')
```

```
delattr(object, attribute)
```

delattr() 函数将从指定对象中删除指定属性。

# Python getattr() 函数

```
class Person:
  name = "Bill"
  age = 63
  country = "USA"

x = getattr(Person, 'age')
```

getattr() 函数从指定的对象返回指定属性的值。

# Python hasattr() 函数

```
class Person:
  name = "Bill"
  age = 63
  country = "USA"

x = hasattr(Person, 'age')
```

如果指定的对象拥有指定的属性，则 hasattr() 函数将返回 True，否则返回 False。

