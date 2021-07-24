# python print 和 sys.stdout.write()

当我们使用print(obj)在console上打印对象的时候，实质上调用的是sys.stdout.write(obj+'\n')，print在打印时会自动加个换行符，以下两行等价：

```Python
sys.stdout.write('hello'+'\n')
print('hello')
```

#### 从控制台重定向到文件

原始的 sys.stdout 指向控制台，如果把文件的对象的引用赋给 sys.stdout，那么 print 调用的就是文件对象的 write 方法，将对象写入文件中：

```Python

f_handler=open('out.log', 'w')
sys.stdout=f_handler
print('hello')
# this hello can't be viewed on concole
# this hello is in file out.log
```

如果你还想在控制台打印一些东西的话，最好先将原始的控制台对象引用保存下来，向文件中打印之后再恢复 sys.stdout

```Python
__console__=sys.stdout
 
# redirection start
# ...
# redirection end
 
sys.stdout=__console__
```

#### 同时重定向到控制台和文件

如果我们希望打印的内容一方面输出到控制台，另一方面输出到文件作为日志保存，那么该怎么办？将打印的内容保留在内存中，而不是一打印就将 buffer 释放刷新，我们可以通过自定义一个类来实现这个功能：

```Python
import os,sys

class redirection():
	def __init__(self):
        self.buf = ''
        self.__console__ = sys.stdout
        self.path = 'C:\\Users\\***\\Desktop'   # 存放日志的路径
        
    def write(self, output_stream):
        self.buf += output_stream
        
    def to_log(self, filename):
        file = open(self.path + '\\' + filename, 'a')
        sys.stdout = file
        print(self.buf)
        file.close
 
    def to_console(self):
        sys.stdout = self.__console__
        print(self.buf)
 
    def flush(self):
        self.buf = ''
 
def main():
    obj = redirection()
    input_stream = input("输入：")
    while input_stream:    # 实现循环输入
        obj.write(input_stream + '\n')
        input_stream = input("输入：")
    obj.to_log('log.txt')   # 日志名称为log.txt
    obj.to_console()
    obj.flush()
 
if __name__ == "__main__":
    main()

```

