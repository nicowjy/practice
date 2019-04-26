#-*- coding: utf-8 -*
# 整数翻转
class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x > 0 and x < 2**31-1:
            s = str(x)
            y = 0
            for i in range(len(s)):
                y += int(s[i]) * 10**i
            if y < 2**31-1:
                return y
            else:
                return 0
        elif x < 0 and x > -2**31:
            s = str(abs(x))
            y = 0
            for i in range(len(s)):
                y -= int(s[i]) * 10**i
            if y > -2**31:
                return y
            else:
                return 0
        else:
            return 0