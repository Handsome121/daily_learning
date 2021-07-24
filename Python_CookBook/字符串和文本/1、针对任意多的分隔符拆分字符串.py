"""
我们需要将字符串拆分为不同的字段，但是分隔符在整个字符串中并不一致
"""
import re

line = 'asdf fhfi; fiijiv, fjifj,ifjirfj,    foo'

res = re.split(r'[;,\s]\s*', line)
print(res)
