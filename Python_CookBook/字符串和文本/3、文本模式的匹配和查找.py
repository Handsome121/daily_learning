"""
我们想要按照特定的文本模式进行匹配和查找
"""
import re

text1 = "11/27/2012"
text2 = "Nov 27,2012"
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# 如果需要多次匹配，则可以先编译
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
text = 'Today is 11/27/2012.PyCon starts 3/13/2013.'
res = datepat.findall(text)
print(res)

# 引入捕获组
datepat1 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat1.match(text1)
print(m)
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

m1 = datepat1.findall(text)
print(m1)
