#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or not numRows:
            return ''
        if numRows == 1:
            return s
        tmp = [''] * numRows
        grouplength = 2*numRows -2
        for i in range(len(s)):
            r = i%grouplength
            if r < numRows:
                tmp[r] += s[i]
            else:
                tmp[grouplength-r] += s[i]
        return ''.join(tmp)