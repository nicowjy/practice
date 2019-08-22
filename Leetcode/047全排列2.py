#!/usr/bin/python
# -*- coding: utf-8 -*-
# ???2
class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        nums.sort()
        res = []

        for j in range(len(nums)):
            if j == 0:
                for x in self.permuteUnique(nums[1:]):
                    res.append([nums[j]] + x)
                continue
            if j > 0 and (nums[j] == nums[0] or nums[j] == nums[j-1]):
                continue
            for x in self.permuteUnique(nums[1:j]+[nums[0]]+nums[j+1:]):
                res.append([nums[j]] + x)
        
        return res

if __name__ == "__main__":
    a = Solution()
    print a.permuteUnique([-1,2,0,-1,1,0,1])