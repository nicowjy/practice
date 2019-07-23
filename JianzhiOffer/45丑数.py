#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-23 21:12:35
# @Author   : Nico
# @File     : 丑数
"""
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        ugly_list = [1,2,3,4,5]
        if index <= 0 or not isinstance(index, int):
            return 0
        while index > len(ugly_list):
            ugly_list.append(self.FindNextUglyNumber(ugly_list))
        return ugly_list[index-1]


    def FindNextUglyNumber(self, ugly_list):
        e = ugly_list[-1]
        for i in range(len(ugly_list)):
            num2 = ugly_list[i]*2
            if num2 > e:
                break
        for i in range(len(ugly_list)):
            num3 = ugly_list[i]*3
            if num3 > e:
                break
        for i in range(len(ugly_list)):
            num5 = ugly_list[i]*5
            if num5 > e:
                break
        return min(num2, num3, num5)
            
if __name__ == "__main__":
    
    a = Solution()
    print a.GetUglyNumber_Solution(6)