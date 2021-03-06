def recur_fibo(n):
    """
    递归斐波拉契数列
    :param n:
    :return:
    """
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


# 获取用户输入
nterms = int(input("您要输入几项？"))
# 检查输入的数字是否正确
if nterms <= 0:
    print("输入正数")
else:
    print("斐波拉契数列：")
    for i in range(nterms):
        print(recur_fibo(i))
