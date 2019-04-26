# 两数和
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        # no special case handling because it's assumed that it has only one solution

def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    # no special case handling because it's assumed that it has only one solution

print(twoSum(nums = [2, 7, 11, 15], target = 9))