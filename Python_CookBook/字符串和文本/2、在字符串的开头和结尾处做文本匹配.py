"""
在字符串的开头和结尾做文本匹配
"""
# filename = 'spam.txt'
# print(filename.endswith('.txt'))
# print(filename.startswith('.txt'))
import os

filename = os.listdir('.')
print(filename)
list_dir = [name for name in filename if name.endswith('.py')]
print(list_dir)


