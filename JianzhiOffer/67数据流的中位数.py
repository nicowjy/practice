#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 20:26:34
# @Author   : Nico
# @File     : 数据流的中位数
"""
题目描述
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""
class Solution:
    def __init__(self):
        self.count = 0
        self.tmp = []

    def Insert(self, num):
        # write code here
        self.count += 1
        self.tmp.append(num)
        self.tmp.sort()

    def GetMedian(self, data):
        # write code here
        if not self.tmp:
            return None
        if self.count & 1:
            return self.tmp[self.count >> 1]
        else:
            return (self.tmp[self.count>>1] + self.tmp[(self.count>>1)-1])*1.0/2