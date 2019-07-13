#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-13 19:22:35
# @Author   : Nico
# @File     : 链表中环的入口节点
"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        k, loop = self.hasLoop(pHead)
        if not loop:
            return None
        p = pHead
        for i in range(k):
            p = p.next
        q = pHead
        while p != q:
            p = p.next
            q = q.next
        return p

    def hasLoop(self, pHead):
        k = 0
        if not pHead or not pHead.next or not pHead.next.next:
            return k, False
        p = pHead
        q = pHead
        while q:
            p = p.next
            q = q.next.next
            if p == q:
                k += 1
                p = p.next
                q = q.next.next
                while p != q:
                    k += 1
                    p = p.next
                    q = q.next.next
                return k, True
        return k, False


'''
comment
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        #遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next
'''