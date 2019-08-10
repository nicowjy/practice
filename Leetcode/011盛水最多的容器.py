#!/usr/bin/python
# -*- coding: utf-8 -*-
# 盛水最多的容器
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        i, j = 0, len(height)-1
        while i < j:
            area = max(area, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area




if __name__ == "__main__":
    a = Solution()
    print a.maxArea([1,8,6,2,5,4,8,3,7])  # 49