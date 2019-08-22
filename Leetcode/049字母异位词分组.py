#!/usr/bin/python
# -*- coding: utf-8 -*-
# 字母异位词分组
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        group = {}
        i = 0
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in group:
                res[group[sorted_word]].append(word)
            else:
                group[sorted_word] = i
                i += 1
                res.append([word])
        return res

if __name__ == "__main__":
    a = Solution()
    print a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# bool(set('ate')==set('eat'))
# res = []
# res.append(['eat'])
# res[0].append('ate')
# res