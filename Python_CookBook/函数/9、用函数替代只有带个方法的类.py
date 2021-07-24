"""
我们定义了一个方法的类，我们希望用一个函数来替代
"""
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# 可以用以下函数替代
def urltemplate(template):
    def openr(**kwargs):
        return urlopen(template.format_map(kwargs))

    return openr
