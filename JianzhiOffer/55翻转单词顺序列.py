#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-24 20:24:25 
# @Author   : Nico
# @File     : 翻转单词顺序列
"""
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        res = ''
        words = s.split(' ')
        for word in words[::-1]:
            res += word
            res += ' '
        return res[:-1]


if __name__ == "__main__":
    a = Solution()
    print a.ReverseSentence(' ')

'''
split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息
split(' ')则对单个空格进行切分，本题选择后者
'''