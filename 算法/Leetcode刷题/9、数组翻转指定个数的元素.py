"""
定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
"""


def leftRotatebyone(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyone(arr, n)


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")


arr = [1, 2, 3, 4, 5, 6, 7, 8]
leftRotate(arr, 2, 8)
printArray(arr, 8)
