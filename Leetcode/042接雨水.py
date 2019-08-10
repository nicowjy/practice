#!/usr/bin/python
# -*- coding: utf-8 -*-
# 接雨水
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        if not height or max(height)==0:
            return ans
        left_max = right_max = 0
        for i in range(len(height)):
            if height[i] >= left_max:
                left_max_index = i
                left_max = height[i]
            if height[i] < left_max:
                ans += left_max - height[i]
        for i in range(len(height)-1, left_max_index, -1):
            right_max = max(right_max, height[i])
            ans -= left_max-right_max
        return ans
