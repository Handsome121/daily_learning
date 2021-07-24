import os
import sys


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    findfile(sys.argv[1], sys.argv[2])

# sys.argv == ["temp.py","a","b","c","d"]  #sys.argv是持有5个元素的list对象
#
# sys.argv[0]  == "temp.py"   #第1个元素为模块名“temp.py”
# sys.argv[1] == "a"               #第2个元素为"a"
# sys.argv[2] == "b"               #第3个元素为"b"
# sys.argv[3] == "c"               #第4个元素为"c"
# sys.argv[4] == "d"               #第5个元素为"d"

# path = '/home//user/Documnets'
# print(os.path.normpath(path))
