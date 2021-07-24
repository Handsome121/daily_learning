"""
数组
"""
from array import array
from random import random

float = array('d', (random() for i in range(10 ** 7)))
print(float[-1])
fp = open('float.bin', 'wb')
float.tofile(fp)  # 存入文件
fp.close()
float2 = array('d')
fp = open('float.bin', 'rb')
float2.fromfile(fp, 10 ** 7)  # 从文件读取
fp.close()
print(float2[-1])

print(float == float2)
