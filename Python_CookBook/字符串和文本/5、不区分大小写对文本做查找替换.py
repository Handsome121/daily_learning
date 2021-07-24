"""
我们需要以不区分大小写的方式在文本中进行查找，可能还需要做替换
"""
import re

text = 'UPPER PYTHON,lower python,Mixed Python'


# res = re.findall('python', text, flags=re.IGNORECASE)
# print(res)
# res1 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
# print(res1)


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper
        elif text.lower():
            return word.lower
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


res = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(res)
