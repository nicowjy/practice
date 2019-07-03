"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        list1 = []
        p = head
        while p is not None:
            list1.append(p)
            p = p.next
        if k > len(list1) or k < 1:
            return
        return list1[-k]

"""
comment
牛客里输入的不是头结点，下为书中代码
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return
        p = head
        for i in range(k-1):
            p = p.next
        q = head
        while p.next is not None:
            p = p.next
            q = q.next

        return q.val
"""