"""
解析路径
"""
import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    ''
]
for path in PATHS:
    print('{!r:17} :{}'.format(path, os.path.split(path)))
    # split()函数将路径分解为两个单独的部分，并返回包含这些结果的一个元组，这个元组的第二个元素是路径的最后一部分，第一个元素则是此前的所有内容
