#!/usr/bin/python
# -*- coding: utf-8 -*-
# ???
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 0, 1
        for k in range(n):
            i, j  = j, i+j
        return j