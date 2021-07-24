"""
对齐文本字符串
"""
text = 'hello world'
print(text.ljust(20, '='))
print(text.rjust(20, '='))
print(text.center(20, '='))
print(format(text, '=>20'))
print(format(text, '=<20'))
print(format(text, '*^20'))
