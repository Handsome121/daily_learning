"""
我们需要对小数进行精确计算，不希望因为浮点数天生的误差而带来影响
"""
from decimal import Decimal, localcontext

a = Decimal('4.2')
b = Decimal('2.3')
print((a + b))
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
