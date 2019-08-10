#!/usr/bin/python
# -*- coding: utf-8 -*-
# 搜索旋转排序数组
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1  
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[left]:
                if nums[left] <= nums[mid]:
                    left = mid+1
                elif target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[left] > nums[mid]:
                    right = mid-1
                elif target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1

if __name__ == "__main__":
    a = Solution()
    print a.search([1,3], 1)
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def mid_search(left, right):
            while left <= right:
                mid = (left+right) / 2
                if target == nums[mid]:
                    return mid
                if target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            return -1

        def find_rotate():
            left, right = 0, len(nums)-1
            if nums[left] <= nums[right]:
                return 0
            while left <= right:
                mid = (left+right) / 2
                if nums[mid] > nums[mid+1]:
                    return mid+1
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid
            return 0
        
        if not nums:
            return -1  
        rotate_index = find_rotate()
        if nums[rotate_index] > target:
            return -1
        if nums[rotate_index] == target:
            return rotate_index
        if rotate_index == 0:
            return mid_search(0, len(nums)-1)
        if target < nums[0]:
            return mid_search(rotate_index, len(nums)-1)
        else:
            return mid_search(0, rotate_index-1)
'''