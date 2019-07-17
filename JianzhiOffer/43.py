#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-17 23:22:39
# @Author   : Nico
# @File     : 把数组排成最小的数
"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        res = ''
        if not numbers:
            return res
        tmp = sorted(numbers, cmp = lambda x,y: self.Compare(x, y))  # O(nlogn)
        for item in tmp:
            res += str(item)
        return res        

    def Compare(self, num1, num2):    # 定义新的比较函数
        a = str(num1)+str(num2)
        b = str(num2)+str(num1)
        while a and b:
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                a = a[1:]
                b = b[1:]
        return 0

'''
comment
注意一下sorted函数中cmp参数的用法
'''