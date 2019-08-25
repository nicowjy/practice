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
        visited = [0]*n                   # 用一个数组记录已访问的点

        while i < n-1:
            reach = reach_list[i]
            for j in range(reach, i, -1):
                if visited[j] == 0:
                    times[j] = times[i] + 1
                    visited[j] = 1
                else:
                    break
            new_reach = max(reach_list[i+1:reach+1])
            for k in range(reach, i, -1):
                if reach_list[k] >= new_reach:
                    i = k
                    break
        return times[-1]

# 无需记录路径
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1,1,1,1]
        n = len(nums)
        if n == 1:
            return 0
        reach_list = [min(x + nums[x],n-1) for x in range(n)]
        count = 0
        i, new_reach = 0, nums[0]
        while i <= n-1:
            reach = new_reach
            count += 1
            new_reach = max(reach_list[i:reach+1])
            i = reach+1
        return count