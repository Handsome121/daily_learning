num = int(input("请输入正整数\n"))


def Decomposition_factor(num):
    n = num
    f = []
    for j in range(1, num // 2 + 1):
        for i in range(2, n):
            if n % i == 0:
                f.append(i)
                n = n // i
                break
    if len(f) == 0:
        print("-1 -1")
    else:
        f.append(n)
        f.sort()
        print("%d" % f[0], end=" ")
        for i in range(1, len(f)):
            print("%d" % f[i], end=" ")
if __name__ == '__main__':
    Decomposition_factor(num)