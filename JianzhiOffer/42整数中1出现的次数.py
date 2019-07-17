#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-17 22:38:44
# @Author   : Nico
# @File     : 整数中1出现的次数（从1到n整数中1出现的次数）
"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n or n <= 0:
            return 0
        num = str(n)
        length = len(num)
        count = 0
        if length == 1:
            return 1
        if num[0] == '1':
            count += int(num[1:]) + 1
        else:
            count += 10**(length-1)
        count += 10**(length-2) * (length-1) * int(num[0])
        if n > 10:            
            count += self.NumberOf1Between1AndN_Solution(int(num[1:]))
        return count

if __name__ == "__main__":
    a = Solution()
    print a.NumberOf1Between1AndN_Solution(55)