"""
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格
"""
import math

a = int(input())


def isZS(x):
    flag = 0
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            print(str(i), end=' ')
            flag = 1
            isZS(x // i)
            break
    if flag == 0:
        print(str(x), end=' ')


isZS(a)
