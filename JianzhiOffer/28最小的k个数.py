"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput is None:
            return
        if k > len(tinput) or k <= 0:
            return []        
        tmp = tinput[:k]
        # 第一个循环建堆，从位置i开始，以end为建堆范围的边界
        for i in range(k//2, -1, -1):           # 遍历所有根节点
            self.siftdown(tmp, tmp[i], i, k)
        # 第二个循环负责添加之后的数据
        for i in range(k, len(tinput)):
            num = tinput[i]
            if num >= tmp[0]:
                continue
            else:
                tmp[0] = num
                self.siftdown(tmp, num, 0, k)

        tmp = sorted(tmp)
        return tmp
 
    def siftdown(self, elems, e, begin, end):
        i, j = begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] > elems[j]:
                j += 1
            if e > elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e