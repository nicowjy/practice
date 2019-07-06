"""
题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []    # 一定注意这里只有一层：[] + [[6]] = [[6]]; [[]] + [[6]] = [[], [6]]

        tmp = []
        if not root.right and not root.left and root.val == expectNumber:
            return [[root.val]]
        else:
            expectNumber -= root.val
            left = self.FindPath(root.left, expectNumber)
            right = self.FindPath(root.right, expectNumber)
            for item in left+right:
                tmp.append([root.val]+item)         # 对每一种可行方案，都需要加root
        return tmp

"""
comment
先将需要返回的函数记录在一个变量中，在通过对该变量的变量添加到结果中。
以此将每一种可能都添加到最初的结果中。
注意一下列表怎么拼
"""