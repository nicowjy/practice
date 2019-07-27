#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 19:56:17
# @Author   : Nico
# @File     : 二叉搜索树的第k个节点
"""
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.tmp = []

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k == 0:
            return None
        self.MidOrder(pRoot)
        if k > len(self.tmp):
            return None
        return self.tmp[k-1]        

    def MidOrder(self, pRoot):
        if not pRoot:
            return
        p = pRoot
        if p.left:
            self.MidOrder(p.left)
        self.tmp.append(p)
        if p.right:
            self.MidOrder(p.right)
        