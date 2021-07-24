"""
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理：
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分
（保留最后16位）和行号完全匹配的记录才做算是”相同“的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准
"""
import sys
from collections import defaultdict

data = map(lambda x: x.split("\\")[-1], sys.stdin.readlines())
errors = defaultdict(int)
result = list()
for d in data:
    name, line = d.strip().split()
    error = " ".join(name[-16:], line)
    errors[error] += 1
    if errors[error] == 1:
        result.append(error)
for r in result[-8:]:
    print(r, error[r])
