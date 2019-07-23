#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-23 22:10:11
# @Author   : Nico
# @File     : 数组中的逆序对
"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 
即输出P%1000000007

输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5

示例1
输入
1,2,3,4,5,6,7,0
输出
7
"""
class Solution:
    def InversePairs(self, data):
        # write code here
        data = list(x%1000000007 for x in data)
        slen, llen = 1, len(data)
        temp = [None]*llen
        count = 0
        while slen < llen:  
            count += self.InversePairsCount(data, temp, slen, llen)          
            slen *= 2
            count += self.InversePairsCount(temp, data, slen, llen)   # 结果存回原位
            slen *= 2
        return count%1000000007

    def InversePairsCount(self, lfrom, lto, slen, llen):
        i = 0
        count = 0
        if slen >= llen:
            return count
        while i + 2*slen < llen:
            count += self.InversePairsCore(lfrom, lto, i, i+slen, i+2*slen)
            i += 2*slen
        if i + slen < llen:
            count += self.InversePairsCore(lfrom, lto, i, i+slen, llen)
        else:
            for j in range(i, llen):
                lto[j] = lfrom[j]
        return count%1000000007

    def InversePairsCore(self, lfrom, lto, start, mid, end):
        count = 0
        i, j, k = mid-1, end-1, end-1
        while i >= start and j >= mid:
            if lfrom[i] > lfrom[j]:
                count += j-mid+1
                lto[k] = lfrom[i]
                i -= 1
            else:
                lto[k] = lfrom[j]
                j -= 1
            k -= 1
        while i >= start:
            lto[k] = lfrom[i]
            i -= 1
            k -= 1
        while j >= mid:
            lto[k] = lfrom[j]
            j -= 1
            k -= 1
        return count%1000000007