#!/usr/bin/python
# -*- coding: utf-8 -*-
# 不同的二叉搜索树
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
