#!/usr/bin/python
# -*- coding: utf-8 -*-
# 单词搜索
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n, m = len(board), len(board[0])
        if not word:
            return False
        def find_word(i, j, word):
            if board[i][j] == word[0] and used[i][j] == 0:
                used[i][j] = 1
                if not word[1:]:
                    return True
                elif i < n-1 and find_word(i+1, j, word[1:]):
                    return True
                elif j < m-1 and find_word(i, j+1, word[1:]):
                    return True
                elif i > 0 and find_word(i-1, j, word[1:]):
                    return True
                elif j > 0 and find_word(i, j-1, word[1:]):
                    return True
                else:
                    used[i][j] = 0
                    return False
            else:
                return False
        
        for i in range(n):
            for j in range(m):
                used = [[0]*m for k in range(n)]
                if find_word(i, j, word):
                    return True
        return False


if __name__ == "__main__":
    a = Solution()
    print a.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS")
