#!/usr/bin/python
# -*- coding: utf-8 -*-
# 解数独
class Solution(object):
    def __init__(self):
        self.check = 0

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def could_fill(row, col, num):
            return board[row][col] == '.' and not rows[row][num-1] and not cols[col][num-1] and not square[(row/3)*3 + col/3][num-1]

        def fill(row, col, num):
            board[row][col] = str(num)
            rows[row][num-1] = 1
            cols[col][num-1] = 1
            square[(row/3)*3 + col/3][num-1] = 1

        def remove(row, col, num):
            board[row][col] = '.'
            rows[row][num-1] = 0
            cols[col][num-1] = 0
            square[(row/3)*3 + col/3][num-1] = 0

        def backtrack(row = 0, col = 0):
            if board[row][col] == '.' :
                for num in range(1, 10):
                    if could_fill(row, col, num):
                        fill(row, col, num)
                        if row == 8 and col == 8:
                            self.check = 1
                            return
                        backtrack(0, col+1) if row == 8 else backtrack(row+1, col)
                        if self.check == 0:
                            remove(row, col, num) 
            else:
                if row == 8 and col == 8:
                    self.check = 1
                    return board
                backtrack(0, col+1) if row == 8 else backtrack(row+1, col)

        rows = [[0]*9 for k in range(9)]
        cols = [[0]*9 for k in range(9)]
        square = [[0]*9 for k in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    fill(row, col, int(board[row][col]))
        backtrack()