#!/usr/bin/python
# -*- coding: utf-8 -*-
# 二叉树的中序遍历
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if not root:
#             return []
#         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# 迭代
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        p = root
        stack.append(p)
        while stack:
            while p.left:
                p = p.left
                stack.append(p)
            p = stack.pop()
            res.append(p.val)
            p = p.right
            if p:
                stack.append(p)
        return res