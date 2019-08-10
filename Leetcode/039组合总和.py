#!/usr/bin/python
# -*- coding: utf-8 -*-
# 组合总和
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = {}
        def get_sum(target):
            if target in dp:
                return
            dp[target] = []
            for i in candidates:
                if target-i == 0:
                    dp[target].append([i])
                if target-i > 0:
                    if target-i not in dp:
                        get_sum(target-i)
                    for item in dp[target-i]:
                        if i <= min(item):
                            dp[target].append([i] + item)

        get_sum(target)
        return dp[target]
            
if __name__ == "__main__":
    a = Solution()
    print a.combinationSum([1,2,3],6)

# i = 2
# item = [3,6,7]
# dp = {}
# dp[7] = []
# dp[7].append([i]+item)
# dp
'''
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''