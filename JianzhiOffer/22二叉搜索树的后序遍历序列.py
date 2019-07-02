"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence.pop()
        se_left = []
        se_right = []        
        while sequence:
            e = sequence.pop(0)
            if e < root:
                se_left.append(e)
            else:
                se_right.append(e)
                break
        while sequence:
            e = sequence.pop(0)
            if e <= root:
                return False
            else:
                se_right.append(e)
        self.VerifySquenceOfBST(se_left)
        self.VerifySquenceOfBST(se_right)
        return True