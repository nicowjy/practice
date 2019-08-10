#!/usr/bin/python
# -*- coding: utf-8 -*-
# 合并k个排序链表
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if lists and lists[0] else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1:
            point.next=l1
        else:
            point.next=l2
        return head.next