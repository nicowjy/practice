"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        pHead = ListNode(0)
        p = pHead

        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
            p = p.next
        if pHead1:
            p.next = pHead1
        if pHead2:
            p.next = pHead2

        return pHead.next
"""
class Solution:
    # 用递归实现
    def Merge(self, pHead1, pHead2):
        # write code here

        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        else:
            if pHead1.val < pHead2.val:
                p = pHead1
                p.next = self.Merge(pHead1.next, pHead2)
            else:
                p = pHead2
                p.next = self.Merge(pHead1, pHead2.next)
        
        return p
"""