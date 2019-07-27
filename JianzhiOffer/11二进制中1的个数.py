"""
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        for i in range(0,32):
            if n&1:
                count=count+1
            n=n>>1
        return count


if __name__ == "__main__":
    a = Solution()
    a.NumberOf1(-2)


"""
comment
负数没有通过，改了之后可以了

自己的代码运行正确率44%：
用例:
-2147483648

对应输出应该为:

1

你的输出为:

2

"""

