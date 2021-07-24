"""
通过公共键对字典列表进行排序
"""
rows = [
    {'frame': 'Brain', 'lname': 'Jones', 'uid': 1003},
    {'frame': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'frame': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'frame': 'Big', 'lname': 'Jones', 'uid': 1004},
]
from operator import itemgetter

row_by_name = sorted(rows, key=itemgetter('frame', 'lname'))
row_by_uid = sorted(rows, key=itemgetter('uid'))
print(row_by_uid)
print(row_by_name)
