#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 14:05:11
# @Author   : Nico
# @File     : 不用加减乘除做加法
"""
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""
class Solution:
    def Add(self, num1, num2):
        # write code here   
        if num1 ^ num2 > -2147483648:
            a = num1 ^ num2
            b = (num1 & num2) << 1
        else:
            a = (num1 ^ num2)%0x100000000
            b = ((num1 & num2) << 1)%0x100000000      
        if a & b != 0:
            res = self.Add(a, b)
        else:    
            res = a ^ b
        return res
        
if __name__ == "__main__":
    a = Solution()
    print a.Add(-1,2)
    
'''
注意负数
使用一开始的方法：
如果负数绝对值小于正数，会一直迭代下去
'''