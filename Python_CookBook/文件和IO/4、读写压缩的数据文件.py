import bz2
import gzip

with gzip.open('somefile.gz', 'rt') as f:
    text1 = f.read()
with bz2.open('somefile.bz2', 'rt') as f:
    text2 = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text1)
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text2)