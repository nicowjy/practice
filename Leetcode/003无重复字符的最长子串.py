#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = len(s)
        maxlength, start, end = 0, 0, 0
        while start < l and end < l:
            if s[end] in s[start:end]:
                start += 1
                maxlength = max(maxlength, end-start)
            else:
                end += 1
                maxlength = max(maxlength, end-start)   
        return maxlength       