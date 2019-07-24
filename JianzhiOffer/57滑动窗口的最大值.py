#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-24 20:50:41
# @Author   : Nico
# @File     : 滑动窗口的最大值
"""
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， 
{2,[3,4,2],6,2,5,1}， 
{2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， 
{2,3,4,2,[6,2,5],1}， 
{2,3,4,2,6,[2,5,1]}。
"""
from collections import deque
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        if size > len(num) or size <= 0:
            return res        
        tmp = deque()
        for i in range(len(num)):       
            if not tmp:
                tmp = deque([[i, num[i]]])
            else:
                if tmp[0][0] < i-size+1:
                    tmp.popleft()
                if not tmp or num[i] >= tmp[0][1]:
                    tmp = deque([[i, num[i]]])
                else:
                    while len(tmp)>1 and num[i] >= tmp[-1][1]:
                        tmp.pop()
                    tmp.append([i, num[i]])
            if i >= size-1:
                res.append(tmp[0][1])
        return res

if __name__ == "__main__":
    a = Solution()
    print a.maxInWindows([10,14,12,11],1)