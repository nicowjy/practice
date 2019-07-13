#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-13 10:59:11
# @Author   : Nico
# @File     : 机器人的运动范围
"""
题目描述
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""
class Solution:
     
    def __init__(self):
        self.vis = {}
         
    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.moving(threshold, rows, cols, 0, 0)
         
    def moving(self, threshold, rows, cols, r, c):
        if self.getDigitSum(r) + self.getDigitSum(c) > threshold:
            return 0
        if r >= rows or c >= cols or r < 0 or c < 0:
            return 0
        if (r, c) in self.vis:
            return 0
        self.vis[(r, c)] = 1
         
        return 1 + self.moving(threshold, rows, cols, r-1, c) \
                 + self.moving(threshold, rows, cols, r+1, c) \
                 + self.moving(threshold, rows, cols, r, c-1) \
                 + self.moving(threshold, rows, cols, r, c+1)
        
    def getDigitSum(self, number):
        sum = 0
        while number > 0:
            sum += number%10
            number /= 10
        return sum




if __name__ == "__main__":
    a = Solution()
    print a.movingCount(10,1,100)   # 29

'''
用例:
15,20,20

对应输出应该为:

359

你的输出为:

328
'''