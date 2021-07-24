# 将输出重定向到一个文件中
# with open('somefile.txt', 'rt') as f:
#     print('hello world', file=f)
# 以不同分隔符或行结尾符完成打印
print('acme', 50, 91.5)
print('acme', 50, 91.5, sep=',')
print('acme', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i, end=' ') 
