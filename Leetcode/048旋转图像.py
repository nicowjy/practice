#!/usr/bin/python
# -*- coding: utf-8 -*-
# 旋转图像
# class Solution:
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix[0])
#         for i in range(n // 2 + n % 2):
#             for j in range(n // 2):
#                 tmp = [0] * 4
#                 row, col = i, j
#                 # store 4 elements in tmp
#                 for k in range(4):
#                     tmp[k] = matrix[row][col]
#                     row, col = col, n - 1 - row
#                 # rotate 4 elements   
#                 for k in range(4):
#                     matrix[row][col] = tmp[(k - 1) % 4]
#                     row, col = col, n - 1 - row

                    
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
            for j in range(n/2 + n%2):
                e = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = matrix[i][j]
                matrix[i][j] = e


if __name__ == "__main__":
    a = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    a.rotate(matrix)
    print matrix