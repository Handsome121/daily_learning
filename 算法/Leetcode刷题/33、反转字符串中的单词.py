"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""


def reverseWords(s):
    """
    反转单词字符串
    :param s:
    :return:
    """
    # str_list = s.split(" ")
    # for i in range(len(str_list)):
    #     str_list[i] = str_list[i][::-1]
    # res = " ".join(str_list)
    # return res
    return " ".join(word[::-1] for word in s.split(" "))


s = "Let's take LeetCode contest"
res = reverseWords(s)
print(res)
