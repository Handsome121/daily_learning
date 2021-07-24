"""
根据字段将记录分组
"""
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/01/2012'},
    {'address': '5645 N REVENSWOOD', 'date': '07/01/2012'},
    {'address': '1060 W ADDISON', 'date': '07/01/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 N GRANVILIE', 'date': '07/04/2012'}
]
from operator import itemgetter
from itertools import groupby

# rows.sort(key=itemgetter('date'))
# # print(rows)
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(' ', i)
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)
for r in rows_by_date['07/01/2012']:
    print(r)
