"""
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度大于2的子串重复
"""
while True:
    try:
        n = input()
        a, b, c, d = 0, 0, 0, 0
        for i in n:
            if i.isupper():
                a = 1
            elif i.islower():
                b = 1
            elif i.isdigit():
                c = 1
            else:
                d = 1
        e = True
        for i in range(len(n) - 3):
            if n.count(n[i:i + 3]) > 1:
                e = False
            if len(n) > 8 and (a + b + c + d) >= 3 and e:
                print("ok")
            else:
                print("NG")
    except:
        break
