"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray is None:
            return 0
        l = 0
        r = len(rotateArray)-1

        if rotateArray[l] < rotateArray[r]:
            return rotateArray[l]
        while rotateArray[l] >= rotateArray[r]:
            if l == r-1:
                return rotateArray[r]
            mid = (l+r)/2
            if rotateArray[l] <= rotateArray[mid]:
                l = mid
            else:
                r = mid


'''
原始办法
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray is None:
            return 0
        for i in range(len(rotateArray)):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
comment:
注意一下< 和 <= 的使用
'''