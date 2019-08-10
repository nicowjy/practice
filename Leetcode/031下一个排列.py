#!/usr/bin/python
# -*- coding: utf-8 -*-
# 下一个排列
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):    # 不能到0
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        nums[i:] = sorted(nums[i:])
                        break
                return nums              
        return nums.sort() if nums else None