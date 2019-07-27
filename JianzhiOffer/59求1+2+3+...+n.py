#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 13:35:04
# @Author   : Nico
# @File     : 求1+2+3+...+n
"""
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        self.add_n(n)
        return self.sum

    def add_n(self, n):
        self.sum += n
        n -= 1
        return n > 0 and self.add_n(n)

if __name__ == "__main__":
    a = Solution()
    print a.Sum_Solution(1)