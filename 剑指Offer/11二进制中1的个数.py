"""
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0

        count = -1
        if n < 0:
            n = -n
            count += 1

        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2

        return count

sum([(n>>i & 1) for i in range(0,32)])
2 >> 3

"""
comment
负数没有通过
"""