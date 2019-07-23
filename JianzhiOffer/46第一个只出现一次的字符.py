#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-23 21:45:52
# @Author   : Nico
# @File     : 第一个只出现一次的字符
"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j, ch in enumerate(s):
            if ch in dic and dic[ch] == 1:
                return j
        return -1