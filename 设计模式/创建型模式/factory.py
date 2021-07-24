"""
简单工厂模式：不直接对客户端暴漏对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例

优点：
1、隐藏了对象创建的实现细节
2、客户端不需要修改代码
缺点：
1、违反了单一职责原则，将创建逻辑集中到一个工厂类里
2、当添加新产品时，需要修改哦工厂类代码，违反了开闭原则
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


class PaymentFactory:
    """生产工厂类"""

    def create_payment(self, method):
        """创建支付"""
        if method == 'alipay':
            return AliPay()
        elif method == 'wechat':
            return WeChatPay()
        elif method == 'huabei':
            return AliPay(user_huabei=True)
        else:
            raise TypeError('No such payment named %s' % method)


pf = PaymentFactory()
p = pf.create_payment()
p.pay(100)
