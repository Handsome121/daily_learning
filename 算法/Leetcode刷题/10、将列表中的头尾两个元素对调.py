"""
定义一个列表，并将列表中的头尾两个元素对调。
"""


def swapList(newList):
    size = len(newList)
    newList[0], newList[size - 1] = newList[size - 1], newList[0]
    return newList


newList = [1, 2, 3]
print(swapList(newList))
