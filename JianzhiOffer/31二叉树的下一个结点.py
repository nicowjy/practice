'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None     # 指向父节点的指针
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        p = pNode
        if p.right:            # p有右子节点
            p = p.right
            while p.left:
                p = p.left
        elif p.next:
            pf = p.next
            if pf.left == p:   # p是其父节点的左子结点
                p = pf
            else:              # p是其父节点的右子节点
                while pf.right == p:
                    p = pf
                    if p.next:
                        pf = p.next
                    else:
                        return None
                p = pf
        else:
            return None

        return p       

"""
comment
多考虑几种情况
"""