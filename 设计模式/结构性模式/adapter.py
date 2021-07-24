"""
适配器模式：将一个类的接口转换成客户端希望的另一个接口，适配器模式使得原本由于接口不兼容而不能一起工作德那些类可以一起工作

两种实现方式：
1、类适配器：使用多继承
2、对象适配器：使用组合

角色：
1、目标接口
2、带适配德类
3、适配器

使用场景：
想使用一个已经存在的类，而他的接口不符合你的要求
想使用一些已经存在的子类，但不可能对每一个子类都进行子类化以匹配他们的接口，对象适配器可以适配它的父类接口
"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):

    def pay(self, money):
        print("支付宝余额支付%d元" % money)


class WeChatPay(Payment):

    def pay(self, money):
        print("微信支付%d元" % money)


class BankPay:
    def cost(self, money):
        print("银联支付%d元" % money)


class ApplePay:
    def cost(self, money):
        print("苹果支付%d元" % money)


# 类适配器
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)
# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p1 = PaymentAdapter(ApplePay())
p2 = PaymentAdapter(BankPay())
p1.pay(100)
p2.pay(100)
