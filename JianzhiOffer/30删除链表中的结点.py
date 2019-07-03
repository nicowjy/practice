"""
题目描述
在O(1)时间删除链表结点。
给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该结点。
链表节点与函数定义如下：
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def DeleteNode(self, pHead, pToBeDeleted):
        if pHead is None or pToBeDeleted is None:
            return None
        
        # 要删除的结点不是尾结点
        if pToBeDeleted.next is not None:
            pToBeDeleted.val = pToBeDeleted.next.val
            pToBeDeleted.next = pToBeDeleted.next.next        
        # 链表只有一个结点，删除头/尾结点
        elif pHead == pToBeDeleted and pHead.next is None:
            return None
        # 链表中有多个节点，删除尾结点
        else:
            pNode = pHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
        
        return pHead


