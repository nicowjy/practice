#!/usr/bin/python
# -*- coding: utf-8 -*-
# 求众数
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        tmp = nums[0]
        for num in nums:
            count += 1 if tmp == num else -1
            if count == 0:
                tmp = num
                count = 1
        return tmp