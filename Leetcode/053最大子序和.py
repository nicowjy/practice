#!/usr/bin/python
# -*- coding: utf-8 -*-
# 最大子序和
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = (-1<<31)+1                        # 四则运算优先级大于位运算
        cursum = 0
        for num in nums:
            cursum = max(cursum+num,num)
            res = max(res,cursum)
        return res