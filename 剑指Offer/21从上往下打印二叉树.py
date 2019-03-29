"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        list1 = []
        list2 = []
        if not root:
            return list1
        list2.append(root)
        while list2:
            p = list2.pop(0)
            list1.append(p.val)
            if p.left:
                list2.append(p.left)
            if p.right:
                list2.append(p.right)            
        return list1
"""
"""
comment
记得用队列s
"""

# 使用deque
from collections import deque
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        list1 = []
        temp = deque()
        if not root:
            return list1
        temp.append(root)
        while temp:
            p = temp.popleft()
            list1.append(p.val)
            if p.left:
                temp.append(p.left)
            if p.right:
                temp.append(p.right)
        return list1