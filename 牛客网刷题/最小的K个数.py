"""
给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。如果K>数组的长度，那么返回一个空的数组
"""
import heapq

nums = [4, 5, 1, 6, 2, 7, 3, 8]
print(heapq.nlargest(4, nums))
