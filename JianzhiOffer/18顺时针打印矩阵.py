# -*- coding:utf-8 -*-
"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return None
        row, col = len(matrix), len(matrix[0])
        start = 0
        temp = []
        while start <= (min(row, col)-1)>>1:
            self.printInCircle(matrix, start, temp)
            start += 1
        return temp

    def printInCircle(self, matrix, start, temp):
        endRow = len(matrix)-1-start
        endCol = len(matrix[0])-1-start
        r, c = start, start
        temp.append(matrix[r][c])
        while c < endCol:
            c += 1
            temp.append(matrix[r][c])            
        while r < endRow:
            r += 1
            temp.append(matrix[r][c])
        while c > start and r > start:
            c -= 1
            temp.append(matrix[r][c])
        while r > start+1 and start < endCol:
            r -= 1
            temp.append(matrix[r][c])
time.localtime()
"""
comment
下面这个方法过于神奇了，自己写一个简单一点的
    def printMatrix(self, matrix):
        # write code here
        result=[]
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        B = []
        for i in range(c):
            A = []
            for j in range(r):
                A.append(matrix[j][i])
            B.append(A)
        B.reverse()                # 所有行上下颠倒
        return B
"""

if __name__ == "__main__":
    a = Solution()
    print a.printMatrix([[1,2],[3,4]])
    print a.printMatrix([[1]])
    print a.printMatrix([[1],[2],[3],[4],[5]])
    print a.printMatrix([[1,2,3,4,5]])
    print a.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])