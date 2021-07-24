"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""
import math

f = float(input())
x = f - int(f)
if x > 0.5:
    print(math.ceil(f))
else:
    print(round(f))

