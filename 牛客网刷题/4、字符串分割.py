"""
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
"""
while True:
    try:
        str1 = input()
        if len(str1) < 8:
            res = str1 + '0' * (8 - len(str1))
            print(res)
        else:
            time = int(len(str1) // 8)
            if len(str1) % 8 == 0:
                for i in range(time):
                    print(str1[i * 8:i * 8 + 8])
            else:
                for i in range(time):
                    print(str1[i * 8:i * 8 + 8])
                print(str1[time * 8:] + '0' * (8 - len(str1[time * 8:])))
    except:
        break
