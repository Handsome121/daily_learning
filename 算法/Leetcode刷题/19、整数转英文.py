"""
将非负整数 num 转换为其对应的英文表示。
"""


def numberTowords(num):
    """
    一万以内非负整数转换对应的英文
    :param num:非负整数
    :return:str
    """
    dict_num = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety'
    }
    if num < 20:
        return dict_num[num]
    elif num % 10 == 0 and num < 100:
        return dict_num[num]
    elif num % 10 != 0 and num < 100:
        c = num % 10
        d = num - c
        return dict_num[d] + ' ' + dict_num[c]
    elif num < 1000:
        f = num // 100  # 百位
        h = num % 100 % 10  # 个位
        g = num % 100 - h  # 十位乘10
        return dict_num[f] + ' ' + 'Hundred' + ' ' + dict_num[g] + ' ' + dict_num[h]
    elif num < 10000:
        j = num // 1000  # 千位
        k = num % 1000 // 100  # 百位
        l = num % 1000 % 100 % 10  # 个位
        z = num % 1000 % 100 - l  # 十位乘10
        return dict_num[j] + ' ' + 'Thousand' + ' ' + dict_num[k] + ' ' + 'Hundred' + ' ' + dict_num[z] + ' ' + \
               dict_num[l]


if __name__ == '__main__':
    print(numberTowords(5569))
