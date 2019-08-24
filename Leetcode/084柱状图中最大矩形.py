#!/usr/bin/python
# -*- coding: utf-8 -*-
# 柱状图中最大矩形
# 分治法：超出内存限制
# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         if not heights:
#             return 0
#         n = len(heights)
#         min_height = min(heights)
#         size = min_height*n
#         for i in range(n):
#             if heights[i] == min_height:
#                 size = max(size, self.largestRectangleArea(heights[:i]), self.largestRectangleArea(heights[i+1:]))
#                 return size

# 栈
class Solution:
    def largestRectangleArea(self, heights):
        heights = [0] + heights + [0]
        stack = []
        size = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                size = max(size, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return size

if __name__ == "__main__":
    a = Solution()
    print a.largestRectangleArea([2,1,5,6,2,3])