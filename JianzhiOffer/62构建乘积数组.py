#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 16:28:00
# @Author   : Nico
# @File     : 构建乘积数组
"""
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
"""
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return None
        if len(A) == 1:
            return A
        beforeList = self.before(A)
        afterList = self.after(A)
        B = [afterList[1]]
        for i in range(1, len(A)-1):
            e = beforeList[i-1] * afterList[i+1]
            B.append(e)
        B.append(beforeList[-2])
        return B

    def before(self, A):
        e = 1
        tmp = []
        for i in range(len(A)):
            e *= A[i]
            tmp.append(e)
        return tmp
        
    def after(self, A):
        e = 1
        tmp = []
        for i in range(len(A)-1, -1, -1):
            e *= A[i]
            tmp.insert(0, e)
        return tmp