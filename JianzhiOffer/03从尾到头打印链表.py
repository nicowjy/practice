"""
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
from collections import deque
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 基于栈的实现
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        temp = deque()
        while listNode:
            temp.appendleft(listNode.val)
            listNode = listNode.next
        return temp   

"""
comment：
1.使用collections中deque包
2.询问是否可以修改原来的链表
"""
# 基于递归的实现
class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        tmp = []
        tmp += self.printListFromTailToHead(listNode.next)
        tmp.append(listNode.val)
        return tmp