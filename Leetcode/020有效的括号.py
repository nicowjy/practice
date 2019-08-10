#!/usr/bin/python
# -*- coding: utf-8 -*-
# 有效的括号
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket = {'}':'{',
                   ']':'[',
                   ')':'('}
        for ch in s:
            if ch in bracket:
                top = stack.pop() if stack else '#'
                if bracket[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack

if __name__ == "__main__":
    a = Solution()
    print a.isValid("]")