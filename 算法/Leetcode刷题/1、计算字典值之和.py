"""
给定一个字典，然后计算它们所有数字值的和。
"""
from typing import List, Tuple, Dict, Union


def returnSum(myobject):
    sum = 0
    for i in myobject:
        sum = sum + myobject[i]
    return sum


dict = {'a': 100, 'b': 200, 'c': 300}
print('sum:', returnSum(dict))


# typing模块的使用
def test(a: int, string: str, f: float, b: bool) -> Tuple[List, Tuple, Dict, bool]:
    """
    :param a:int
    :param string:str
    :param f: float
    :param b: bool
    :return: tuple
    """
    ll = [1, 2, 3, 4]
    tup = (string, a, string)
    dic = {"xxx": f}
    boo = b
    return ll, tup, dic, boo


print(test(12, "lkj", 2.3, True))


def func(a: int, string: str) -> List[int or str]:
    list1 = []
    list1.append(a)
    list1.append(str)
    return list1


def get_next_id() -> Union[int, None]:
    return 1
    return None

