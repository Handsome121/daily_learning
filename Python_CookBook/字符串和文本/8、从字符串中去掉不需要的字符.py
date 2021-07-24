"""
去掉不需要的字符
"""
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
t = '----hello===='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))