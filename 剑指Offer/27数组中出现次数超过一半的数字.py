"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 0
        num = 0

        for i in numbers:
            if num == i:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    num = i
                    count = 1

        times = 0
        for i in numbers:
            if num == i:
                times += 1

        if times > len(numbers)//2:
            return num
        else:
            return 0

"""
comment
思路很重要：
出现次数超过数组长度的一般，则该数字出现次数比其他数字之和还多。

使用collections中Counter函数也可：
import collections
def MoreThanHalfNum_Solution(numbers):
    tmp = collections.Counter(numbers)
    x = len(numbers)//2
    for num, times in tmp.items:
        if times > x:
            return num
    return 0
"""