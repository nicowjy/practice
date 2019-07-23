#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-23 21:09:42
# @Author   : Nico
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        tmp = 0
        for item in array:
            tmp ^= item
        try:
            index_ = bin(tmp).replace('0b','')[::-1].index('1')
        except:
            return None
        tmp1, tmp2 = 0, 0
        for item in array:
            if index_ >= len(bin(item).replace('0b','')):
                tmp1 ^= item
            elif bin(item).replace('0b','')[::-1][index_] == '1':
                tmp1 ^= item
            else:
                tmp2 ^= item
        return [tmp1, tmp2]

'''
分两步：
1.一个数组里除了一个数字之外，其他的数字都出现了两次。
2.把这两个出现一次的数字分到两个数组中。
'''