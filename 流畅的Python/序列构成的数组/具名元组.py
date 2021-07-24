"""
具名元组
"""
from collections import namedtuple

# 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字，后者可以使由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
City = namedtuple('City', 'name country population coordinates')
# 存放在对应字段里的数据要以一串参数的形式传入到构造函数中（元组的构造函数只接受单一的可迭代对象）
tokyo = City('Tokpo', 'JP', 36.933, (35.65568, 139.5695548))
# 你可以通过字段名或者位置来获取一个字段的信息
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
# 一些专有的属性
print(City._fields)  # _fields属性是一个包含这个类所有字段名称的元组

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# _make()通过接受一个可迭代对象来生成这个类的一个实例，他的作用跟City(*delhi_data)
delhi = City._make(delhi_data)
# _asdict()把具名元组以collections.OrderedDict的形式返回，我们可以利用它来把元组里的信息友好的呈现出来
print(delhi._asdict())
