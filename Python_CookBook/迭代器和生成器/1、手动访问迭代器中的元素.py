"""
手动访问迭代器中的元素
"""
# with open('/etc/passwd') as f:
#     try:
#         while True:
#             line = next(f,None)
#             if line is None:
#                 break
#             print(line, end='')
#     except StopIteration:
#         pass

items = [1, 2, 3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))

