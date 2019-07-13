#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-13 16:02:44
# @Author   : Nico
# @File     : 正则表达式匹配
"""
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        elif (not s and pattern and len(pattern)==1) or not pattern:
            return False
        else:
            if len(pattern) >= 2 and pattern[:2] == '.*':
                if len(s) >= 1:
                    res = self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern) or self.match(s, pattern[2:]) 
                else:
                    res = self.match(s, pattern[2:]) 
            elif len(pattern) >= 2 and pattern[1] == '*':
                if not s:
                    res = self.match(s, pattern[2:]) 
                elif s[0] == pattern[0]:
                    res = self.match(s[1:], pattern) or self.match(s[1:], pattern[2:]) or self.match(s, pattern[2:])
                else:
                    res = self.match(s, pattern[2:])
            elif pattern[0] == '.' or s[0] == pattern[0]:
                res = self.match(s[1:], pattern[1:])
            else:
                return False
        return res


if __name__ == "__main__":
    a = Solution()
    print a.match("",".*a")


'''
comment
1.注意 index out of range 的情况
2.所有匹配情况
'''