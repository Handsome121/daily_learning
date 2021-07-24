# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        curr = pHead
        pre = None
        while curr is not None:
            pre, curr = curr.next, pre
        return pre
