#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-27 12:50:56
# @Author   : Nico
# @File     : 圆圈中最后剩下的数
"""
题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。
然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m <= 0:
            return -1
        if n == 1:
            return 0
        if m == 1:
            return n-1
        pHead = self.CreateList(n)
        return self.DeleteNode(pHead, m)

    def CreateList(self, n):
        p = ListNode(0)
        for i in range(n):
            q = ListNode(i)
            p.next = q
            p = q
            if i == 0:
                pHead = p
            if i == n-1:
                p.next = pHead
        return pHead

    def DeleteNode(self, pHead, m):
        p = pHead
        q = pHead.next
        while p != q:
            for i in range(m-2):
                p = p.next
                q = q.next
            q = q.next
            p.next = q
            p = p.next
            q = q.next
        return p.val
        
        
if __name__ == "__main__":
    a = Solution()
    print a.LastRemaining_Solution(6,7)
    
'''
思路：
1.建立一个环形链表
2.开始删
'''