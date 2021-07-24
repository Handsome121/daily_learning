"""
对数值做格式化输出，包括控制位数，对齐，包含千位分隔符以及其他一些细节
"""
x = 1234.56789
print(format(x, '0.2f'))  # 保留2位小数
print(format(x, '>10.1f'))  # 右对齐
print(format(x, '<10.1f'))  # 左对齐
print(format(x, '^10.1f'))  # 居中对齐
print(format(x, ','))  # 包含千位分隔符
print(format(x, '0,.1f'))  # 包含千位分隔符保留小数一位
