"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        list1 = []
        for num in array:
            if num % 2 == 1:
                list1.append(num)
        for num in array:
            if num % 2 == 0:
                list1.append(num)
        return list1


"""
comment
class Solution:
    def func(self, n):
        return n & 1 == 1   # n为奇数返回true

    def reOrderArray(self, array, func):
        # write code here
        if array is None:
            return
        l = 0
        r = len(array)-1
        while l < r:
            while l < r and self.func(array[l]):
                l += 1
            while l < r and not self.func(array[r]):
                r -= 1
            array[l], array[r] = array[r], array[l]
        
        return array
注意要求，书中代码改变了奇偶数的相对位置
"""