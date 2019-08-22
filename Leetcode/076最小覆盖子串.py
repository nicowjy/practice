#!/usr/bin/python
# -*- coding: utf-8 -*-
# 最小覆盖子串
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''
        length = []
        dict_t = Counter(t)
        len_t = len(t)
        i = 0
        for j, char in enumerate(s):
            if dict_t[char] > 0:
                len_t -= 1
            if char in dict_t:
                dict_t[char] -= 1
            if len_t == 0:
                while i <= j and s[i] not in dict_t or dict_t[s[i]] < 0:
                    if dict_t[s[i]] < 0:
                        dict_t[s[i]] += 1
                    i += 1
                if not length or length[1] >= j-i+1:
                    length = [i,j-i+1]
                dict_t[s[i]] += 1
                len_t += 1
                i += 1
    
        return '' if not length else s[length[0]:length[0]+length[1]]
