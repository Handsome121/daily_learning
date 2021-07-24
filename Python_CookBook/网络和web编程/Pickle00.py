"""
pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。
pickle模块只能在python中使用，python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化，
pickle序列化后的数据，可读性差，人一般无法识别。
"""
# pickle.dump(obj, file[, protocol])
# 序列化对象，并将结果数据流写入到文件对象中。参数protocol是序列化模式，默认值为0，表示以文本的形式序列化。protocol的值还可以是1或2，表示以二进制的形式序列化。

# pickle.load(file)
# 反序列化对象。将文件中的数据解析为一个Python对象。
# 其中要注意的是，在load(file)的时候，要让python能够找到类的定义，否则会报错：
import pickle


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))


aa = Person("JGood", 2)
aa.show()
f = open('d:\\p.txt', 'w')
pickle.dump(aa, f, 0)
f.close()
# del Person
f = open('d:\\p.txt', 'r')
bb = pickle.load(f)
f.close()
bb.show()

# clear_memo()
# 清空pickler的“备忘”。使用Pickler实例在序列化对象的时候，它会“记住”已经被序列化的对象引用，所以对同一对象多次调用dump(obj)，pickler不会“傻傻”的去多次序列化。
import StringIO
import pickle


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))


aa = Person("JGood", 2)
aa.show()
fle = StringIO.StringIO()
pick = pickle.Pickler(fle)
pick.dump(aa)
val1 = fle.getvalue()
print(len(val1))
pick.clear_memo()
pick.dump(aa)
val2 = fle.getvalue()
print(len(val2))
fle.close()
