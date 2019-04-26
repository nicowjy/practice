'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        n = 0
        s_spy = ''
        while n < len(s):
            if s[n] == ' ':
                s_spy += '%20'
            else:
                s_spy += s[n]
            n += 1
        return s_spy
        
"""
comment：
多个case有时不需要特殊处理
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(" ", "%20")
"""