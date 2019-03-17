"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
"""
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        e = 1
        while exponent > 0:
            e *= base
            exponent -= 1
        while exponent < 0:
            e /= base
            exponent += 1
        return e