#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-07 15:44:47
# @Author   : Nico
# @File     : 序列化二叉树
"""
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    index = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '$'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    
    def Deserialize(self, s):
        # write code here
        self.index += 1   
        if s.split(',')[self.index] == '$':
            return None
        else:
            root = TreeNode(int(s.split(',')[self.index]))         
        
        root.left = self.Deserialize(s)
        root.right = self.Deserialize(s)
        return root



"""
comment
需要有一个实例变量
ps:数字10占两个字符
"""

if __name__ == "__main__":
    a = Solution()
    print a.Serialize(a.Deserialize('1,2,$,$,10,$,$'))