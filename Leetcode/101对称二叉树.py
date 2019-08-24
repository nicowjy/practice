#!/usr/bin/python
# -*- coding: utf-8 -*-
# 对称二叉树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (not root2 and root1):
                return False
            if root1.val != root2.val:
                return False
            return helper(root1.left, root2.right) and helper(root1.right, root2.left)
        return helper(root, root)
        