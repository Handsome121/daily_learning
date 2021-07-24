"""
将两个有序的链表合并为一个新链表，要求新的链表是通过拼接两个链表的节点来生成的，且合并后新链表依然有序。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            res = l1
            res.next = self.mergeTwoLists(l1.next, l2)
        if l1.val >= l2.val:
            res = l2
            res.next = self.mergeTwoLists(l1, l2.next)
        return res

