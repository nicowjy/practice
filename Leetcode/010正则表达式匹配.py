#!/usr/bin/python
# -*- coding: utf-8 -*-
# 正则表达式匹配
# 回溯法
# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if not p:
#             return not s
#         first_match = bool(s) and p[0] in {s[0], '.'}
#         if len(p) >= 2 and p[1] == '*':
#             return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
#         else:
#             return first_match and self.isMatch(s[1:], p[1:])

# 动态规划：自顶向下的备忘录法 
# class Solution(object):
#     def isMatch(self, text, pattern):
#         memo = {}
#         def dp(i, j):
#             if (i, j) not in memo:
#                 if j == len(pattern):
#                     ans = i == len(text)
#                 else:
#                     first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                     if j+1 < len(pattern) and pattern[j+1] == '*':
#                         ans = dp(i, j+2) or first_match and dp(i+1, j)
#                     else:
#                         ans = first_match and dp(i+1, j+1)

#                 memo[i, j] = ans
#             return memo[i, j]

#         return dp(0, 0)

# 动态规划：自下而上
class Solution:
    def isMatch(self, s, p):
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i<len(s) and p[j] in {s[i], '.'} 
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


if __name__ == "__main__":
    a = Solution()
    print a.isMatch('aa', 'a*')
