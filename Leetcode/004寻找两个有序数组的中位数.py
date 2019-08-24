#!/usr/bin/python
# -*- coding: utf-8 -*-
# 寻找两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.findKth(nums1, nums2, l/2+1)*1.0
        else:
            return (self.findKth(nums1, nums2, l/2) + self.findKth(nums1, nums2, l/2+1))*1.0/2
        
    def findKth(self, nums1, nums2, k):
		if not nums1:
			return nums2[k-1]
		if not nums2:
			return nums1[k-1]
		if k == 1:
			return min(nums1[0], nums2[0])
		if len(nums1) < k/2:
			return self.findKth(nums1, nums2[k/2:], k-k/2)
		if len(nums2) < k/2:
			return self.findKth(nums1[k/2:], nums2, k-k/2)
		a, b = nums1[k/2-1], nums2[k/2-1]
		if a >= b:
			return self.findKth(nums1, nums2[k/2:], k-k/2)
		else:
			return self.findKth(nums1[k/2:], nums2, k-k/2)