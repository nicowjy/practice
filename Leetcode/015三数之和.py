#!/usr/bin/python
# -*- coding: utf-8 -*-
# 三数之和
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) < 3:
            return res
        nums.sort()
        for k in range(len(nums)):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            num = nums[k]
            i, j = k+1, len(nums)-1
            while i < j:
                if i >= j or nums[j] < 0:
                    break
                threesum = num + nums[i] + nums[j]
                if threesum == 0:
                    res.append([num, nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1                   
                    i += 1
                    j -= 1
                elif threesum < 0:
                    i += 1
                else:
                    j -= 1
        return res


if __name__ == "__main__":
    a = Solution()
    print a.threeSum([-1, 0, 1, 2, -1, -4])