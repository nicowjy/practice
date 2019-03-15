"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def push(self, node):
        self.list1.append(node)

    def pop(self):
        '''
        self.list2 = self.list1[::-1]
        e = self.list2.pop()
        self.list1 = self.list2[::-1]
        return e
        '''
        if self.list2 == []:       # list2不为0则直接pop
            while self.list1:
                self.list2.append(self.list1.pop())
        return self.list2.pop()

"""
commet
通过"if self.list2 == []"保证：
只要前面的数还在，后面的数就不会进到list2中
"""