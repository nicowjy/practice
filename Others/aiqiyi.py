#!/usr/bin/env python  
# coding=utf-8  
# Python使用的是2.7.6，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
while 1:
    a=[]  
    s = raw_input()
    # raw_input()里面不要有任何提示信息
    if s != "":
        for x in s.split():  
            a.append(int(x))  

        print sum(a)
    else:
        break   q


s = raw_input()
n = int(s)
s = raw_input()
a = [int(x) for x in s.split()]

dp = {}
dp[3] = {}
dp[3][(1,1)] = 1
dp[3][(1,0)] = 2
dp[3][(0,1)] = 2
dp[3][(0,0)] = 1
n=4
for i in range(4, n+1):
    tmp = [[0], [1]]
    for _ in range(i-2):
        new_tmp = []
        for item in tmp:
            new_tmp.append(item + [0])
            new_tmp.append(item + [1])
        tmp = new_tmp

    dp[i] = {}
    for nums in tmp:
        dp[i][tuple(nums)] = dp[i-1][tuple(nums[1:])] * dp[i-1][tuple(nums[:-1])] + 1

print dp[n][tuple(a)]
    

