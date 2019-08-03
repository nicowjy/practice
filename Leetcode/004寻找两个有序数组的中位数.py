#!/usr/bin/python
# -*- coding: utf-8 -*-
# 寻找两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         m, n = len(nums1), len(nums2)
#         if m == 0 or n == 0:
#             if m == 0 and n == 0:
#                 return None
#             elif m == 0:
#                 return (nums2[n/2] + nums2[(n-1)/2])*1.0/2
#             else:
#                 return (nums1[m/2] + nums1[(m-1)/2])*1.0/2
#         if m > n:
#             nums1, nums2 = nums2, nums1
#             m, n = len(nums1), len(nums2)
#         start, end = 0, m-1
#         while start <= end:
#             i = (start + end)/2
#             j = (m + n - 1)/2 - 1 - i
#             if i == m-1 or end == 0:
#                 if nums1[i] > nums2[j]:
#                     if (m+n) & 1 == 1:
#                         return nums1[i]*1.0
#                     else:
#                         return (nums1[i]+nums2[j+1])*1.0/2
#                 else:
#                     if i == m-1:
#                         return (nums2[(n-m-1)/2] + nums2[(n-m)/2])*1.0/2  
#                     else:                                       # i == 0
#                         return (nums2[(n+m-1)/2] + nums2[(n+m)/2])*1.0/2    
#             if nums1[i] <= nums2[j+1] and nums2[j] <= nums1[i+1]:
#                 if (m+n) & 1 == 1:
#                     return max(nums1[i], nums2[j])*1.0
#                 else:
#                     return (max(nums1[i], nums2[j]) + min(nums1[i+1], nums2[j+1]))*1.0/2
#             if nums1[i+1] < nums2[j]:
#                 start = i+1
#             else:
#                 end = i



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
        	return self.findKth(nums1, nums2, n / 2 + 1) *1.0
        else:
        	smaller = self.findKth(nums1, nums2, n / 2)
        	bigger = self.findKth(nums1, nums2, n / 2 + 1)
        	return (smaller + bigger) / 2.0


    def findKth(self, A, B, k):
    	if len(A) == 0:
    		return B[k-1]
    	if len(B) == 0:
    		return A[k-1]
    	if k == 1 :
    		return min(A[0],B[0])
    	a = A[ k / 2 - 1 ] if len(A) >= k / 2 else None
    	b = B[ k / 2 - 1 ] if len(B) >= k / 2 else None

    	if b is None or (a is not None and a < b):
    		return self.findKth(A[k/2:], B, k - k/2)
    	return self.findKth(A, B[k/2:], k - k/2)

if __name__ == "__main__":
    a = Solution()
    print a.findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],[0,6])