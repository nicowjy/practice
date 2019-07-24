#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-24 19:59:03
# @Author   : Nico
# @File     : 和为S的两个数字
"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return []
        low, high = 0, len(array)-1
        while low < high:
            if array[low] + array[high] == tsum:
                return [array[low], array[high]]
            if array[low] + array[high] > tsum:
                high -= 1
            if array[low] + array[high] < tsum:
                low += 1
        return []
