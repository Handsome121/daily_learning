"""
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写，字符串长度小于500
"""
import re

str1 = input()
alphabet = input()
str1_list = re.findall(alphabet, str1, re.I)
count = len(str1_list)
print(count)
