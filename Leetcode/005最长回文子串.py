#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        len1, len2 = 1, 1
        start1, start2 = 0, 0
        for i in range(len(s)-1):
            if len1 <= self.expandAroundCenter(s, i, i)[0]:
                len1, start1 = self.expandAroundCenter(s, i, i)
            if len2 <= self.expandAroundCenter(s, i, i+1)[0]:
                len2, start2 = self.expandAroundCenter(s, i, i+1)
        if len1 > len2:
            return s[start1:start1+len1]
        else:
            return s[start2:start2+len2]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1, left+1