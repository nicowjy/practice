"""
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, node):        
        if not self.minstack or node <= self.minstack[-1]:
            self.minstack.append(node)
        self.stack.append(node)

    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minstack[-1]

"""
comment
回去看书里解法
"""