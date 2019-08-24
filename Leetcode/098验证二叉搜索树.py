#!/usr/bin/python
# -*- coding: utf-8 -*-
# 验证二叉搜索树
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        mid_order = self.inorderTraversal(root)
        if not mid_order:
            return True
        for i in range(len(mid_order)-1):
            if mid_order[i] >= mid_order[i+1]:
                return False
        return True

    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)