"""
我们以流水线形式处理数据
"""
import bz2
import fnmatch
import gzip
import os
import re


def gen_find(filepat, top):
    """找到指定目录下的指定文件"""
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.fileter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """打开特定格式的文件"""
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """遍历文件内容"""
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """匹配到指定内容"""
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


lognames = gen_find('access-log', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?!)python', lines)
for line in pylines:
    print(line)
