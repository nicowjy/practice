"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
"""
# -*- coding:utf-8 -*-
class Solution:
    def helper(self, base, exponent):
        e = 1
        if exponent == 0:
            return e        
        elif exponent > 0:
            if exponent%2 == 0:
                e = self.Power(base, exponent/2) * self.Power(base, exponent/2)
            else:
                e = self.Power(base, (exponent-1)/2) * self.Power(base, (exponent-1)/2) * base  
        return e
    
    def Power(self, base, exponent):
        if exponent == 0:
            return 1        
        elif exponent > 0:
            e = self.helper(base, exponent)
        else:
            e = 1.0/self.helper(base, -exponent)
        return e


if __name__ == "__main__":
    a = Solution()
    a.Power(2,3)