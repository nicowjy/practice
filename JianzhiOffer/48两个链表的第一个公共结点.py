#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-24 11:56:08 
# @Author   : Nico
# @File     : 两个链表的第一个公共结点
"""
题目描述
输入两个链表，找出它们的第一个公共结点。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        count1, count2 = 0, 0
        p, q = pHead1, pHead2
        while p:
            count1 += 1
            p = p.next
        while q:
            count2 += 1
            q = q.next
        if count1 >= count2:
            diff = count1 - count2
            for i in range(diff):
                pHead1 = pHead1.next
        else:
            diff = count2 - count1
            for i in range(diff):
                pHead2 = pHead2.next
        while pHead1:
            if pHead1 == pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return None


for i in range(0):
    print i
        