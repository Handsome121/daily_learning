"""
对文本进行读写操作
"""
with open('somefile.txt', 'rt') as f:
    data = f.read()
    for line in f:
        pass
