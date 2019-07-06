#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-06 15:29:31
# @Author   : Nico
# @File     : 之字形打印二叉树
"""
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        listOdd = []
        listEven = []
        result = []
        if not pRoot:
            return result
        listOdd.append(pRoot)
        while listOdd or listEven:
            if listOdd:
                temp = []
                while listOdd:
                    p = listOdd.pop()
                    temp.append(p.val)
                    if p.left:
                        listEven.append(p.left)
                    if p.right:
                        listEven.append(p.right) 
                result.append(temp)   
            if listEven:
            temp = []        
                while listEven:
                    p = listEven.pop()
                    temp.append(p.val)
                    if p.right:
                        listOdd.append(p.right)
                    if p.left:
                        listOdd.append(p.left)
                result.append(temp)
        return result