"""
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址1.0.0.0~126.255.255.255;
B类地址128.0.0.0~191.255.255.255;
C类地址192.0.0.0~223.255.255.255;
D类地址224.0.0.0~239.255.255.255；
E类地址240.0.0.0~255.255.255.255

私网IP范围是：
10.0.0.0～10.255.255.255
172.16.0.0～172.31.255.255
192.168.0.0～192.168.255.255

子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的
"""


def checkvalid(ip, ym):
    # 若ip错误，则掩码无需判断
    ip1 = filter(None, ip.split('.'))
    ip2 = [int(x) for x in ip1]
    if len(ip2) < 4:
        return False
    else:
        # 子网掩码去掉分隔符'.'
        ym1 = list(map(int, ym.split('.')))
        # 二进制转换和高位补0
        ym2 = ''.join(['{:08b}'.format(i) for i in ym1])
        if ym2.find('0') == -1 or ym2.find('1') == -1 or ym2.find('0') != ym2.rfind('1') + 1:
            return False
        return True


def publicip(ip):
    ipn = [int(n) for n in ip.split('.')]
    if 1 <= ipn[0] <= 126:
        return 'a'
    elif 128 <= ipn[0] <= 191:
        return 'b'
    elif 192 <= ipn[0] <= 223:
        return 'c'
    elif 224 <= ipn[0] <= 239:
        return 'd'
    elif 240 <= ipn[0] <= 255:
        return 'e'
    else:
        return 'ignore'


def privateip(ip):
    ipn = [int(n) for n in ip.split('.')]
    if (ipn[0] == 10) or (ipn[0] == 172 and (16 <= ipn[1] <= 31)) or (ipn[0] == 192 and ipn[1] == 168):
        return True
    return False


def resprint(ip, ym, classdic):
    if checkvalid(ip, ym):
        classdic[publicip(ip)] += 1
        if privateip(ip):
            classdic['private'] += 1
    else:
        classdic['wrong'] += 1
    return classdic


import sys
from collections import defaultdict


def main():
    classdic = defaultdict(int)
    for line in sys.stdin:
        ip, ym = line.split('~')
        resprint(ip, ym, classdic)
    res = []
    for key in ['a', 'b', 'c', 'd', 'e', 'wrong', 'private']:
        res.append(classdic[key])
    print(' '.join(res))


main()
