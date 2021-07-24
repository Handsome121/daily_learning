# Partial

```Python
#官方实例
from functools import partial

# 将一个二进制的字符串传承int数字类型
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010')) #18
print(basetwo('100101110')) #302
```

```Python
# 获取百度的html内容
import requests

def get_baidu(method, url):
    response = requests.request(method=method, url=url)
    return response.content

res = get_baidu("get", "https://www.baidu.com")
print(res)

# 将函数和参数封装到一个指定变量名中,下次执行直接调用加()
getBaidu = partial(get_baidu, "get", "https://www.baidu.com")
print(type(getBaidu))
res = getBaidu()
```

```Python
#定义一个加减乘除的类
class Calculate(object):
    md=["add","minus","multiplication","division"]
    def __init__(self,method,num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2
        if method in self.md:
            func=getattr(Calculate,method)
            self.result=func(self)

    def add(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


add=partial(Calculate,"add")
minus=partial(Calculate,"minus")
multiplication=partial(Calculate,"multiplication")
division=partial(Calculate,"division")
```

```
#调用刚刚写好的类的py文件
from functool_learn import functool_employ

res=functool_employ.add(3, 5)
print(res.result)
res=functool_employ.minus(3, 5)
print(res.result)
res=functool_employ.multiplication(3, 5)
print(res.result)
res=functool_employ.division(3, 5)
print(res.result)
```