#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-24 12:05:29
# @Author   : Nico
# @File     : 数字在排序数组中出现的次数
"""
题目描述
统计一个数字在排序数组中出现的次数。
"""
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or (len(data)==1 and data[0]!=k):
            return 0                         # 问清楚应该返回什么
        elif self.GetFirstK(data, k) == -1:
            return 0
        else:
            times = self.GetLastK(data, k) - self.GetFirstK(data, k) + 1

        return times

    def GetFirstK(self, data, k):
        low, high = 0, len(data)-1
        while low <= high:
            mid = (low + high)//2
            if data[mid] > k:
                high = mid-1
            elif data[mid] < k:
                low = mid+1
            else:
                if mid == 0:
                    # print 'first:%d' % mid
                    return mid
                elif data[mid-1] < k:
                    return mid
                else:
                    high = mid-1
        return -1
        
    def GetLastK(self, data, k):
        low, high = 0, len(data)-1
        while low <= high:
            mid = (low + high)//2
            if data[mid] > k:
                high = mid-1
            elif data[mid] < k:
                low = mid+1
            else:
                if mid == len(data)-1:
                    # print 'last:%d' % mid
                    return mid
                elif  data[mid+1] > k:
                    return mid
                else:
                    low = mid+1
        return -1


if __name__ == "__main__":
    a = Solution()
    print a.GetNumberOfK([1,2,3,3,3,3],3)