#!/usr/bin/python
# -*- coding: utf-8 -*-
# 子集
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        return [x+[nums[-1]] for x in self.subsets(nums[:-1])] + self.subsets(nums[:-1])

if __name__ == "__main__":
    a = Solution()
    print a.subsets([1,2,3])