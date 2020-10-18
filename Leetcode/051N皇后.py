#!/usr/bin/python
# -*- coding: utf-8 -*-
# nico.wjy
# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         def could_place(row, col):
#             return not (cols[col] + pie[row+col] + na[row-col])

#         def place_queen(row, col):
#             q.add((row, col))
#             cols[col] = 1
#             pie[row+col] = 1
#             na[row-col] = 1

#         def remove_queen(row, col):
#             q.remove((row, col))
#             cols[col] = 0
#             pie[row+col] = 0
#             na[row-col] = 0

#         def add_solution():
#             solution = []
#             for _, col in sorted(q):
#                 solution.append('.'*col + 'Q' + '.'*(n-col-1))
#             output.append(solution)

#         def backtrack(row=0):
#             for col in range(n):
#                 if could_place(row, col):
#                     place_queen(row, col)
#                     if row == n-1:
#                         add_solution()
#                     else:
#                         backtrack(row+1)
#                     remove_queen(row, col)

#         col = [0] * n
#         pie = [0] * (2*n-1)
#         na = [0] * (2*n-1)
#         q = set()
#         output = []
#         backtrack()
#         return output

        
# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         ans = []
#         def dfs(nums, row):
#             if row == n:
#                 ans.append(nums[:])
#                 return
#             for col in range(n):      
#                 nums[row] = col        # nums[row]: col of row's queen
#                 if valid(nums, row):
#                     dfs(nums, row+1)

#         def valid(nums, row):
#             for i in range(row):
#                 if abs(nums[i] - nums[row]) == abs(i - row) or nums[i] == nums[row]:
#                     return False
#             return True

#         dfs([None for _ in range(n)], 0)

#         # draw the graph
#         result = [[] for _ in range(len(ans))]
#         for i in range(len(ans)):
#             for col in ans[i]:
#                 tmp = '.'*n
#                 result[i].append(tmp[:col]+'Q'+tmp[col+1:])
#         return result

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        def backtrack(nums, row):
            if row == n:
                ans.append(nums[:])
                return
            for col in range(n):
                if valid(nums, row, col):
                    nums[row] = col
                    backtrack(nums, row+1)
                    nums[row] = None

        def valid(nums, row, col):
            for i in range(row):
                if abs(nums[i] - col) == abs(i - row) or nums[i] == col:
                    return False
            return True

        backtrack([None for _ in range(n)], 0)

        # draw the graph
        result = [[] for _ in range(len(ans))]
        for i in range(len(ans)):
            for col in ans[i]:
                tmp = '.'*n
                result[i].append(tmp[:col]+'Q'+tmp[col+1:])
        return result


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
