"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        if pRootOfTree.left:
            left = pRootOfTree.left
            self.Convert(left)
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree
        else:
            pRootOfTree.left = None

        if pRootOfTree.right:
            right = pRootOfTree.right
            self.Convert(right)
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree
        else:
            pRootOfTree.right = None

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

"""
comment
要返回最左边的结点
没啥好改的，多看几遍吧
"""