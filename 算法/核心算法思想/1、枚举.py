"""
枚举算法的思想是：将问题的所有可能的答案一一列举，然后根据条件判断此答案是否合适，保留合适的，丢弃不合适的。在C语言中，
枚举算法一般使用while循环实现。使用枚举算法解题的基本思路如下。
① 确定枚举对象、枚举范围和判定条件。
② 逐一列举可能的解，验证每个解是否是问题的解。
枚举算法一般按照如下3个步骤进行。
① 题解的可能范围，不能遗漏任何一个真正解，也要避免有重复。
② 判断是否是真正解的方法。
③ 使可能解的范围降至最小，以便提高解决问题的效率。
"""
import itertools


def twentyfour(cards):
    """
    (1)itertools.permutations(可迭代对象)：
        通俗地讲，就是返回可迭代对象的所有数学全排列方式。
        itertools.permutations("1118") -> 即将数字1118进行全排列组合
    (2)itertools.product(*iterables, repeat=1)
        iterables是可迭代对象,repeat指定iterable重复几次
        返回一个或者多个iterables中的元素的笛卡尔积的元组
        即为product(list1, list2) 依次取出list1中的每1个元素，与list2中的每1个元素，组成元组，
        repeat即为元组中有几个元素，最多重复几次
    :param cards:
    :return:
    """
    for num in itertools.permutations(cards):
        for ops in itertools.product("+-*/", repeat=3):
            # ({0}{4}{1}){5}({2}{6}{3}) - > 即在{0}{1}{2}{3}放上数字，{4}{5}{6}放上运算符号，只能放三个，四个数字中间只能放三个运算符
            # 带括号有8种方法
            # 1. (ab)cd
            bsd1 = '({0}{4}{1}){5}{2}{6}{3}'.format(*num, *ops)
            # 2. a(bc)d
            bsd2 = '{0}{4}({1}{5}{2}){6}{3}'.format(*num, *ops)
            # 3. ab(cd)
            bsd3 = '{0}{4}{1}{5}({2}{6}{3})'.format(*num, *ops)
            # 4. (ab)(cd)
            bsd4 = '({0}{4}{1}){5}({2}{6}{3})'.format(*num, *ops)
            # 5. ((ab)c)d
            bsd5 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*num, *ops)
            # 6.  (a(bc))d
            bsd6 = '({0}{4}({1}{5}{2})){6}{3}'.format(*num, *ops)
            # 7.  a((bc)d)
            bsd7 = '{0}{4}(({1}{5}{2}){6}{3})'.format(*num, *ops)
            # 8.  a(b(cd))
            bsd8 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*num, *ops)
            # print([bsd1, bsd2, bsd3, bsd4, bsd5, bsd6, bsd7, bsd8])
            for bds in [bsd1, bsd2, bsd3, bsd4, bsd5, bsd6, bsd7, bsd8]:
                try:
                    if abs(eval(bds) - 24) < 1e-20:
                        return "24点结束=" + bds
                except ZeroDivisionError:
                    continue
    return "Not fond"


cards = ['2484', '1126', '1127', '1128', '2484', '1111']
for card in cards:
    print(twentyfour(card))
