#!/usr/bin/python
# -*- coding: utf-8 -*-
# 通配符匹配
class Solution:
    def isMatch(self, s, p):
        dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] == '*' and dp[0][j-1]:
                dp[0][j] = True
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*' and (dp[i][j-1] or dp[i-1][j]):
                    dp[i][j] = True
                elif p[j-1] in {s[i-1], '?'} and dp[i-1][j-1]:
                    dp[i][j] = True

        return dp[-1][-1]

if __name__ == "__main__":
    a = Solution()
    print a.isMatch("aab","c*a*b")