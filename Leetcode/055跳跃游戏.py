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
        reach = 0
        for i in range(n):
            if i > reach:
                return False
            if i + nums[i] > reach:
                reach = i + nums[i]
            else:
                continue
            if reach >= n-1:
                return True


if __name__ == "__main__":
    a = Solution()
    print a.canJump([1,5,0])
