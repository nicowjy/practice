#!/usr/bin/python
# -*- coding: utf-8 -*-
# N皇后
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def could_place(row, col):
            return not (cols[col] + pie[row+col] + na[row-col])

        def place_queen(row, col):
            q.add((row, col))
            cols[col] = 1
            pie[row+col] = 1
            na[row-col] = 1

        def remove_queen(row, col):
            q.remove((row, col))
            cols[col] = 0
            pie[row+col] = 0
            na[row-col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(q):
                solution.append('.'*col + 'Q' + '.'*(n-col-1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row == n-1:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row, col)

        col = [0] * n
        pie = [0] * (2*n-1)
        na = [0] * (2*n-1)
        q = set()
        output = []
        backtrack()
        return output

        




















# class Solution:
#     def solveNQueens(self, n):
#         def could_place(row, col):
#             return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
#         def place_queen(row, col):
#             queens.add((row, col))
#             cols[col] = 1
#             hill_diagonals[row - col] = 1
#             dale_diagonals[row + col] = 1
        
#         def remove_queen(row, col):
#             queens.remove((row, col))
#             cols[col] = 0
#             hill_diagonals[row - col] = 0
#             dale_diagonals[row + col] = 0
        
#         def add_solution():
#             solution = []
#             for _, col in sorted(queens):
#                 solution.append('.' * col + 'Q' + '.' * (n - col - 1))
#             output.append(solution)
        
#         def backtrack(row = 0):
#             for col in range(n):
#                 if could_place(row, col):
#                     place_queen(row, col)
#                     if row + 1 == n:
#                         add_solution()
#                     else:
#                         backtrack(row + 1)
#                     remove_queen(row, col)
        
#         cols = [0] * n
#         hill_diagonals = [0] * (2 * n - 1)
#         dale_diagonals = [0] * (2 * n - 1)
#         queens = set()
#         output = []
#         backtrack()
#         return output


if __name__ == "__main__":
    a = Solution()
    print a.solveNQueens(4)
