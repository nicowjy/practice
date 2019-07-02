"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        """
        没看懂
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            e = pHead.next
            pHead.next = last
            last = pHead
            pHead = e
        return last
        """
        if not pHead or not pHead.next:
            return pHead
        p = None
        while pHead:
            q = pHead
            pHead = q.next
            q.next = p
            p = q
        pHead = p
        return pHead