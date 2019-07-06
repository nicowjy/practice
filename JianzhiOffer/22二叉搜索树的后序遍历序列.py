# -*- coding:utf-8 -*-
"""
题目描述 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        r = True
        if len(sequence) == 1:
            return r
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
        if len(se_left) > 0:
            r = self.VerifySquenceOfBST(se_left)
        if len(se_right) > 0:
            r = self.VerifySquenceOfBST(se_right)
        return r

if __name__ == "__main__":
    a = Solution()
    print a.VerifySquenceOfBST([1,4,2,3,5])

"""
comment
通过了牛客网的答案也不一定对，自己多试几个测试用例。
"""