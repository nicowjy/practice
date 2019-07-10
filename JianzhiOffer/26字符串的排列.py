#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2019-07-07 18:58:22
# @Author   : Nico
# @File     : 字符串的排列
"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        res = []

        for j in range(len(ss)):
            if j == 0:
                for x in self.Permutation(ss[1:]):
                    res.append(ss[j] + x)
                continue
            if ss[j] == ss[0]:
                continue
            for x in self.Permutation(ss[1:j]+ss[0]+ss[j+1:]):
                res.append(ss[j] + x)
        
        return res



"""
comment
注意各种边界：
1. 重复字符    # 可以用set(list1)去重，返回
2. 字符串为空
3. 和牛客网上的答案顺序不一致
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        ss = sorted(ss)
        list1 = []
        for i, le in enumerate(ss):
            if i >= 1:
                if le == ss[i-1]:
                    continue
            substr = ss[:i] + ss[i+1:]
            list2 = self.Permutation(substr)
            if list2:
                for item in list2:
                    list1.append(le+item)
            else:
                list1.append(le)
        return list1
"""

if __name__ == "__main__":
    a = Solution()
    print a.Permutation('aabc')