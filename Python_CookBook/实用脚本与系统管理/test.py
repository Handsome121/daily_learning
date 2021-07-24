"""
fileinput.input (files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
------------------------------------------------------------------------------------------
files:                  #文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]
inplace:                #是否将标准输出的结果写回文件，默认不取代
backup:                 #备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
bufsize:                #缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
mode:                   #读写模式，默认为只读
openhook:               #该钩子用于控制打开的所有文件，比如说编码方式等;
"""

# import fileinput
#
# for line in fileinput.input('00.txt'):
#     print(fileinput.filename(), '|', 'Line Number:', fileinput.lineno(), '|: ', line, end='')

# fileinput.input()       #返回能够用于for循环遍历的对象
# fileinput.filename()    #返回当前文件的名称
# fileinput.lineno()      #返回当前已经读取的行的数量（或者序号）
# fileinput.filelineno()  #返回当前读取的行的行号
# fileinput.isfirstline() #检查当前行是否是文件的第一行
# fileinput.isstdin()     #判断最后一行是否从stdin中读取
# fileinput.close()       #关闭队列

# 利用fileinput对多文件操作，并原地修改内容
# import fileinput
#
# def process(line):
#     return line.rstrip() + ' line'
#
# for line in fileinput.input(['00.txt', '01.txt'], inplace=1):
#     print(process(line), end='\n')

# 利用fileinput实现文件内容替换，并将原文件作备份
# import fileinput
#
# for line in fileinput.input('00.txt', backup='.bak', inplace=1):
#     print(line.rstrip().replace('Python', 'Perl'))

# 利用fileinput将CRLF文件转为LF
# import fileinput
# import sys
#
# for line in fileinput.input('01.txt', inplace=True):
#     # 将Windows/DOS格式下的文本文件转为Linux的文件
#     if line[-2:] == "\r\n":
#         line = line + "\n"
#     sys.stdout.write(line)
# 利用fileinput对文件简单处理
# import sys
# import fileinput
#
# for line in fileinput.input('00.txt'):
#     sys.stdout.write('=> ')
#     sys.stdout.write(line)

