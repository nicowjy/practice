#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y, t = 0, x
        while t > 0:
            y = y*10 + t%10
            t /= 10
        return y == x