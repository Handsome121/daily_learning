"""
提供短小的回调函数为sort()这样的操作所用
"""
add = lambda x, y: x + y
print(add(3, 4))
names = ['David Beazley', 'Ned Batchelder', 'Brain Jones', 'Raymond Hettinger']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
