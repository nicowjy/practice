#!/usr/bin/python
# -*- coding: utf-8 -*-
# 最小路径和
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid[0]), len(grid)
        dp = [[0]*m for i in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]