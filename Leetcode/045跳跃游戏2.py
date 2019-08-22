#!/usr/bin/python
# -*- coding: utf-8 -*-
# 跳跃游戏2
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        times = [0]*n
        i = 0
        reach_list = [min(x + nums[x],n-1) for x in range(n)]

        while i < n-1:
            reach = reach_list[i]
            for j in range(i+1, reach+1):
                times[j] = times[i] + 1
            new_reach = max(reach_list[i+1:reach+1])
            for k in range(reach, i, -1):
                if reach_list[k] >= new_reach:
                    i = k
                    break
        return times[-1]