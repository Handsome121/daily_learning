"""
贪心算法的基本思路如下。
① 建立数学模型来描述问题。
② 把求解的问题分成若干个子问题。
③ 对每一子问题求解，得到子问题的局部最优解。
④ 把子问题的局部最优解合并成原来解问题的一个解。
实现该算法的基本过程如下。
（1）从问题的某一初始解出发。
（2）while能向给定总目标前进一步。
（3）求出可行解的一个解元素。
（4）由所有解元素组合成问题的一个可行解。
"""


def greedy():
    """
    汽车加油次数最少
    :return:
    """
    n = 100
    k = 5
    d = [50, 80, 39, 60, 40, 32]  # 表示加油站之间的距离
    num = 0  # 表示加油次数
    for i in range(k):
        if d[i] > n:
            print('no solution')
            return
    i, s = 0, 0  # 利用S进行迭代
    while i <= k:
        s += d[i]
        if s >= n:
            # 当局部和大于N时，则将局部和更新为当前距离
            s = d[i]
            # 贪心意在让每一次加满油之后跑尽可能远的距离
            num += 1
        i += 1
    print(num)


def main():
    """
    找零
    :return:
    """
    d = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]  # 存储每种硬币的面值
    d_nums = []  # 存储每种硬币的数量
    s = 0
    # 拥有的零钱总和
    temp = input("请输入每种零钱的数量：")
    d_num0 = temp.split(" ")
    for i in range(0, len(d_num0)):
        d_nums.append(int(d_num0[i]))
        s += d[i] * d_nums[i]  # 计算出收银员有多少钱
    sum = float(input("请输入需要找的零钱："))
    if sum > s:
        print("无法找零")
        return 0
    s = s - sum
    # 要想用的硬币数量最少，需要利用所有大面值的硬币，因此从数组的大面值得元素开始遍历
    i = 6
    while i >= 0:
        if sum > d[i]:
            n = int(sum / d[i])
            if n >= d_nums[i]:
                n = d_nums[i]  # 更新n
            sum -= n * d[i]
            print("用了%d个%f硬币" % (n, d[i]))
        i -= 1


if __name__ == '__main__':
    greedy()
    main()
