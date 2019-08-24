#!/usr/bin/python
# -*- coding: utf-8 -*-

# 建堆：适合n >> k 的情况
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def sift_down(start, end):
            e = nums[start]
            i, j = start, 2*start+1
            while j < end:
                if j+1 < end and nums[j+1] > nums[j]:
                    j += 1
                if e > nums[j]:
                    break
                nums[i] = nums[j]
                i, j = j, 2*j+1
            nums[i] = e
        
        end = len(nums)
        for i in range(end/2-1, -1, -1):
            sift_down(i, end)
        for i in range(k-1):
            nums[0], nums[end-1-i] = nums[end-1-i], nums[0]
            sift_down(0, end-i-1)
        return nums[0]

    return nums

# 分治：借鉴快排的partition，顺便把快排写一遍
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)       
        nums, p = self.partition(nums)
        if p == n-k:
            return nums[p]
        elif p > n-k:
            return self.findKthLargest(nums[:p], p+k-n)
        else:
            return self.findKthLargest(nums[p:], k)


    def partition(self, nums):
        left, right = 0, len(nums)-1
        e = nums[-1]
        while left < right:
            while left < right and nums[left] <= e:
                left += 1
            if left < right:
                nums[right] = nums[left]
                right -= 1            
            while left < right and nums[right] >= e:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
        nums[left] = e
        return nums, left
            
if __name__ == "__main__":
    a = Solution()
    print a.findKthLargest([3,2,1,5,6,4],6)        



'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''