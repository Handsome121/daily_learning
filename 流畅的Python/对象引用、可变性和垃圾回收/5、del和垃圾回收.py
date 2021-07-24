"""
对象绝不会自行销毁，然而，无法得到对象时，可能会被当做垃圾回收
"""
import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind')


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)
