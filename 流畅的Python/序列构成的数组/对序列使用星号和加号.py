"""
建立由列表组成的列表
"""
import dis

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'x'
print(board)
# 相当于下面这个
board = []
for i in range(3):
    row = ['_'] * 3  # 每次迭代中都新建了一个列表
    board.append(row)

# 不能像下面这样搞
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)

l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))  # 原地改变，内存地址没有改变
t = (1, 2, 3)
print(id(t))
t *= 2
print(t)
print(id(t))  # 内存地址发生改变，对不可变对象进行拼接时，因为每次都有一个新对象，而解释器需要把原来对象中的元素先复制到新对象里，
# 然后在追加新元素


dis.dis('s[a]+=b')
