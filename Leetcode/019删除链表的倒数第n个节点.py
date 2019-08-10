#!/usr/bin/python
# -*- coding: utf-8 -*-
# 删除链表的倒数第n个节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # if head and not head.next and n == 1:
        #     return None
        p, q = head, head
        for i in range(n):
            if q.next:
                q = q.next
            else:
                return head.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head