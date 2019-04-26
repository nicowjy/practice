"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 考虑最大最小和空数组
        if array == [[]]:
            return False

        # 从右上角开始，排除不可能的列
        i = len(array[0])-1
        j = 0
        while i > 0 and j < len(array)-1:
            while target < array[j][i] and i > 0:
                i -= 1
            while target > array[j][i] and j < len(array)-1:
                j += 1
            if target == array[j][i]:
                return True
        return False

"""
comment：
先通过就行，别想复杂度
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n = len(array)
        for i in range(n):
            if target in array[i]:
                return 'true'
        return 'false'

while True:
    try:
        S = Solution()
        # 字符串转为list
        L = list(eval(raw_input()))
        array = L[1]
        target = L[0]
        print(S.Find(target, array))
    except:
        break
"""