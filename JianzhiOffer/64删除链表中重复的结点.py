#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 19:12:36
# @Author   : Nico
# @File     : 删除链表中重复的结点
"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        CountNodes = self.count(pHead)
        start = ListNode(0)
        start.next = pHead
        p = start
        q = pHead
        while q:
            if CountNodes[q.val] == 1:   
                p = q             
                q = q.next
            else:
                q = q.next
                p.next = q
        return start.next

    def count(self, pHead):
        CountNodes = {}
        p = pHead
        while p:
            if p.val in CountNodes:
                CountNodes[p.val] += 1
            else:
                CountNodes[p.val] = 1
            p = p.next
        return CountNodes