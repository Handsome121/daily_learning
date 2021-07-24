"""
随机选择
"""
import random

# 随机选择一个元素
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
# 取样出N个元素，将选出的元素移除已做进一步的考察
print(random.sample(values, 3))
print(random.sample(values, 2))
print(random.sample(values, 4))
print(random.sample(values, 3))
# 如果只是想打乱顺序
random.shuffle(values)
print(values)
# 产生随机整数
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
# 产生0-1之间均匀分布的浮点数值
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
