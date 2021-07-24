"""
用迭代器取代while循环
"""
CHUCKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUCKSIZE)
        if data == b'':
            break
        pass


def reader(s):
    for chunk in iter(lambda: s.recv(CHUCKSIZE), b''):
        pass
