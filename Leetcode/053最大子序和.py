#!/usr/bin/python
# -*- coding: utf-8 -*-
# 最大子序和
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max(nums)
        if max_sum < 0:
            return max_sum
        tmp_list = []
        for i in range(nums):
            if i <= 0:
                if sum(tmp_list) + i > 0:
                    tmp_list.append(i)
                else:
                    tmp_list = []
            else:
                tmp_list.append(i)
                max_sum = max(max_sum, sum(tmp_list))
        return max_sum
    
'''
有空用分治法做一遍
'''