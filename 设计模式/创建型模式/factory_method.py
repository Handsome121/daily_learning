"""
工厂方法模式
定义一个用于创建对象的接口，让子类决定实例化哪一个产品类
角色：
抽象工厂角色
具体工厂角色
抽象产品角色
具体产品角色

优点：
1、每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
2、隐藏了对象创建的实现细节
缺点：
每增加一个具体产品类，就必须增加一个相应的具体工厂类
"""

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """抽象类"""

    @abstractmethod
    def pay(self, money):
        """支付函数"""
        pass


class AliPay(Payment):
    """阿里支付类"""

    def __init__(self, user_huabei=False):
        self.user_huabei = user_huabei

    def pay(self, money):
        """阿里支付"""
        if self.user_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝余额支付%d元" % money)


class WeChatPay(Payment):
    """微信支付类"""

    def pay(self, money):
        """微信支付"""
        print("微信支付%d元" % money)


class BankPay(Payment):
    """微信支付类"""

    def pay(self, money):
        """银联支付"""
        print("银联支付类%d元" % money)


class PaymentFactory(metaclass=ABCMeta):
    """生产工厂类"""

    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WechatFactory(PaymentFactory):
    def create_payment(self):
        return WeChatPay()


class HuaBeiFactory(PaymentFactory):
    def create_payment(self):
        return AliPay(user_huabei=True)


class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


pf = HuaBeiFactory()
p = pf.create_payment()
p.pay(100)
