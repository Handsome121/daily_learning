"""
在函数定义时完成对特定变量的绑定
"""
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))
print(b(10))
# x是一个自由变量，在运行时才进行绑定而不是定义的时候绑定，因此，lambda表达式中的x值应该是在执行时才确定的，执行时的值是多少就是多少

# 默认参数
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))

funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))

funcs2 = [lambda x, n=n: x + n for n in range(5)]
for f in funcs2:
    print(f(0))
