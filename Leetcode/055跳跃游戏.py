#!/usr/bin/python
# -*- coding: utf-8 -*-
# 跳跃游戏
# 贪心算法
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        tmp = [False] * n
        tmp[-1] = True
        i = n-2
        while i >= 0:
            furthestJump = min(i+nums[i], n-1)
            for j in range(furthestJump, i, -1):
                if tmp[j] is True:
                    tmp[i] = True
            i -= 1
                
        return tmp[0]


if __name__ == "__main__":
    a = Solution()
    print a.canJump([1,5,0])
