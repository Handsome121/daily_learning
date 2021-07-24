"""
合并映射
"""
# 如果想去两个字典中执行相同的操作,在a中查找完没有再去b中查找
a = {'x': 1, 'z': 2}
b = {'y': 3, 'z': 4}
from collections import ChainMap

c = ChainMap(a, b)
print(c)
# print(c['x'])
# print(c['y'])
# print(c['z'])
# print(len(c))
# print(list(c.keys()))
# c['z'] = 10
# print(a)
# c['w'] = 40
# print(a)
# del c['x']
# print(a)
# del c['u']

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])

merged = dict(b)
merged.update(a)
print(merged)
a.update(b)
print(a)
# 需要单独构建一个完整的字典对象（或者修改其中现有的一个字典，这就破坏了原始数据）
# 如果其中任何一个原始字典做了修改，这个改变都不会反应到合并后的字典中
a['x'] = 13
print(merged['x'])
