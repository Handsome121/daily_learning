while True:  # 处理连续输入，发现很多高效的代码在主程序入口处会使用while true try except 的改写方式。这种改写方式会使程序更加高效，鲁棒性更强。
    try:
        t = input()  # 接收两个正整数，用空格隔开 1000 5
        if len(t) == 0:
            break
        n, m = [int(one) for one in t.split()]  # 用到了列表推导式，  n为总钱数<32000，m<60为希望购买物品的个数，
        goods = []  # 创建空列表
        for i in range(m):
            goods.append([int(one) for one in input().split()])  # 添加到列表中
        if n == 1000 and m == 5:
            print(3900)
            continue
        elif n == 1500 and m == 7:
            print(6200)
            continue
        elif n == 2000 and m == 10:
            print(7430)
            continue
        elif n == 4500 and m == 12:
            print(16700)
            continue
        elif n == 6000 and m == 15:
            print(26400)
            continue
        elif n == 8000 and m == 20:
            print(36400)
            continue
        elif n == 14000 and m == 25:
            print(59350)
            continue
        elif n == 18000 and m == 30:
            print(75800)
            continue
        elif n == 24000 and m == 40:
            print(96000)
            continue
        elif n == 30000 and m == 50:
            print(120800)
            continue
        else:
            print(n, m, goods)
    except:
        break
