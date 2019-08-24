#!/usr/bin/python
# -*- coding: utf-8 -*-
# 最大矩形
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        height_maxtrix = [[0]*m for i in range(n)]
        for j in range(m):
            height_maxtrix[0][j] = 1 if matrix[0][j] == "1" else 0
            for i in range(1, n):
                height_maxtrix[i][j] = height_maxtrix[i-1][j] + 1 if matrix[i][j] == "1" else 0
        res = 0
        for i in range(n):
            res = max(res, self.largestRectangleArea(height_maxtrix[i]))
        return res

    def largestRectangleArea(self, heights):
        heights = [0] + heights + [0]
        stack = []
        size = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                size = max(size, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return size
range(1,1)
if __name__ == "__main__":
    a = Solution()
    print a.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])