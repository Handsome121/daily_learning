"""
用正则表达式对一段文本做匹配，但是希望在进行匹配时能够跨越多行
"""
import re

comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
comment2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
text1 = '/* this is a comment */'
text2 = '''
/* this is a 
multiline comment */
'''
print(comment1.findall(text1))
print(comment2.findall(text2))
