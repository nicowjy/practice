#!/usr/bin/python
# -*- coding: utf-8 -*-
# 合并区间
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp = []
        intervals.sort(key=lambda x:x[0])
        found = False
        i = 0
        while i <= len(intervals)-1:
            if i == len(intervals)-1:
                tmp.append(intervals[i])
                break
            if intervals[i][1] >= intervals[i+1][0]:
                tmp.append([intervals[i][0], max(intervals[i][1],intervals[i+1][1])])
                found = True
                i += 2
            else:
                tmp.append(intervals[i])
                i += 1
        if found:
            tmp = self.merge(tmp)
        return tmp

if __name__ == "__main__":
    a = Solution()
    print a.merge([[1,4],[0,4]])

intervals = [[1,4],[0,4]]
intervals.sort(key=lambda x:x[0])
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:

# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
