#!/usr/bin/python
# -*- coding: utf-8 -*-
# 颜色分类
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, len(nums)-1
        cur = 0
        while cur <= p2:
            if nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            elif nums[cur] == 0:
                nums[cur], nums[p1] = nums[p1], nums[cur]
                p1 += 1
                cur += 1
            else:                     # nums[cur] == 1
                cur += 1
        return nums

if __name__ == "__main__":
    a = Solution()
    print a.sortColors([0])