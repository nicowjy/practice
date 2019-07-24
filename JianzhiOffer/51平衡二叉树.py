#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-24 16:25:05
# @Author   : Nico
# @File     : 平衡二叉树
"""
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        res, depth = self.GetDepth(pRoot)
        return res

    def GetDepth(self, pRoot):
        if not pRoot:
            return True, 0
        if not pRoot.left and not pRoot.right:
            return True, 1
        left, leftDepth = self.GetDepth(pRoot.left)
        right, rightDepth = self.GetDepth(pRoot.right)
        if left and right and abs(leftDepth-rightDepth)<=1:
            return True, max(leftDepth, rightDepth)+1
        return False, -1


'''
未改进的方法：
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if not pRoot.left and not pRoot.right:
            return True
        if abs(self.GetDepth(pRoot.left)-self.GetDepth(pRoot.right)) <= 1:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        return False

    def GetDepth(self, pRoot):
        if not pRoot:
            return 0
        if not pRoot.left and not pRoot.right:
            return 1
        if pRoot.left or pRoot.right:
            return max(self.GetDepth(pRoot.left), self.GetDepth(pRoot.right))+1
'''