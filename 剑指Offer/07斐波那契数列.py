"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        i, j = 0, 1
        if n == 0:
            return 0
        for k in range(n):
            i, j = j, i+j

        return i