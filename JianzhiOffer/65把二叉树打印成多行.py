#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 19:43:20
# @Author   : Nico
# @File     : 把二叉树打印成多行
"""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def __init__(self):
        self.res = []

    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return self.res
        list1 = deque()
        list2 = deque()
        list1.append(pRoot)
        while list1 or list2:
            list2, list1 = self.PrintLine(list1, list2)
        return self.res

    def PrintLine(self, list1, list2):
        tmp = []
        while list1:
            p = list1.popleft()
            tmp.append(p.val)            
            if p.left:
                list2.append(p.left)
            if p.right:
                list2.append(p.right)
        self.res.append(tmp)
        return list1, list2

                
