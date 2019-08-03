#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0 and x <= (1<<31)-1:
            s = str(x)
            y = 0
            for i in range(len(s)):
                y += int(s[i]) * 10**i
            if y <= (1<<31)-1:
                return y
            else:
                return 0
        elif x < 0 and x > -1<<31:
            s = str(abs(x))
            y = 0
            for i in range(len(s)):
                y -= int(s[i]) * 10**i
            if y > -1<<31:
                return y  
            else:
                return 0
        else:
            return 0     