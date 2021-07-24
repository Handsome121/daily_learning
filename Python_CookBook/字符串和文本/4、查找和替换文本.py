"""
对字符串中的文本做替换和查找操作
"""
import re

text = 'Today is 11/27/2012.PyCon starts 3/13/2013.'
# res = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text)
# print(res)
#
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
res1, n = datepat.sub(r'\3-\2-\1', text)
# print(res1)
# print(n)

from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    print(mon_name)
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


res2 = datepat.sub(change_date, text)
print(res2)
