#!/usr/bin/python
# -*- coding: utf-8 -*-
# 在排序数组中查找元素的第一个和最后一个位置
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_first():
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)/2
                if nums[mid] == target:
                    if mid == 0 or nums[mid-1] < target:
                        return mid
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1

        def find_last():
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)/2
                if nums[mid] == target:
                    if mid == len(nums)-1 or nums[mid+1] > target:
                        return mid
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return -1    
        
        return [find_first(), find_last()]
            

if __name__ == "__main__":
    a = Solution()
    print a.searchRange(nums = [2,2], target = 2)

# 示例 1:

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:

# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
