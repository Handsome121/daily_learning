"""
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000
"""

str1 = input()
str_list = str1.split(" ")
str_length = len(str_list[-1])
print(str_length)
