"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here       
        if not pHead:
            return

        # 复制结点
        p = pHead
        while p:
            q = RandomListNode(p.label)
            q.next = p.next
            p.next = q
            p = q.next
        
        # 复制特殊指针
        p = pHead
        while p:
            q = p.next
            if p.random:
                q.random = p.random.next
            p = q.next

        # 拆分链表
        p = pHead
        qHead = p.next
        while p:
            q = p.next
            p.next = q.next
            p = q.next
            if p:
                q.next = p.next
            else:
                q.next = None     # 注意尾结点
                break        
        return qHead

"""
comment
复制结点时使用定义的结点类
"""