#!/usr/bin/python
# -*- coding: utf-8 -*-
# 最长有效括号
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = 0
        maxlength = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right == left:
                maxlength = max(maxlength, right*2)
            if right > left:
                left = right = 0
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                left += 1
            else:
                right += 1
            if right == left:
                maxlength = max(maxlength, right*2)
            if right > left:
                left = right = 0     
                
        return maxlength

if __name__ == "__main__":
    a = Solution()
    print a.longestValidParentheses("((()")
