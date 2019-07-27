#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 15:58:22
# @Author   : Nico
# @File     : 把字符串转化为整数
"""
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
复制
+2147483647
    1a33
输出
复制
2147483647
    0
"""
import re
class Solution:
    def StrToInt(self, s):
        # write code here
        num = 0
        if not s or not re.match(r"[\+\-]?[0-9]+$", s):
            return 0
        else:
            for i in range(1, len(s)):
                num = num*10 + self.single_int(s[i])
        if s[0] == '+':
            return num
        elif s[0] == '-':
            return -num
        else:
            return num + self.single_int(s[0])*10**(len(s)-1)
    
    # 将单个字符转化为int型
    def single_int(self, char_a):
        for i in range(10):
            if str(i) == char_a:
                return i
                
if __name__ == "__main__":
    a = Solution()
    print a.StrToInt('1a33')