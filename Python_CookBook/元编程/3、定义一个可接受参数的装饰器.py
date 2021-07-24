"""
定义一个可接受参数的装饰器
"""
import logging
from functools import wraps


def logged(level, name=None, message=None):
    """
    如果名字和信息没有定义，默认值为函数的模块与名称
    :param level: 日志等级
    :param name: 日志名称
    :param message: 日志信息
    :return:
    """

    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logged(logging.DEBUG)
def add(x, y):
    """执行加法"""
    return x + y


# @logged(logging.CRITICAL, 'example')
# def spm():
#     print('Spam!')


res = add
