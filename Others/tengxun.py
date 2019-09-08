#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys 
for line in sys.stdin:
    a = line.split()
    print int(a[0]) + int(a[1])

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        for v in values:
            ans += v
    print ans


def hua(n,k):
    count = 0
    while k <= n:
        count += n-k+1
        k += k
    return count+1

def hua(n,k):
    count = 0
    while k <= n:
        start = 0
        while start+k <= n:
            count += 1
            print start
            start += 1
        k += k
    return count+1

s=raw_input()
t, k = int(s.split(' ')[0]), int(s.split(' ')[1])
for i in range(t):
    s = raw_input()
    a, b = int(s.split(' ')[0]), int(s.split(' ')[1])
    count = 0
    for n in range(a, b+1):
        count += hua(n, k)
    print count

hua(1,2)
hua(2,2)
hua(3,2)


1
6
1 2 3 4 5 6
s = raw_input()
t = int(s)
s = raw_input()
n = int(s)
s = raw_input()
arr = [int(x) for x in s.split(' ')]

def run(arr, n):
    save = {}
    for i in arr:
        if save.has_hey(i):
            save[i] = save[i] + 1
        else:
            save[i] = 1
    s = 0
    for k,v in save.items():
        if (v > n/2):
            return 'NO'
        s += int(v)
    if (s%2 == 0):
        return 'YES'
    else:
        return 'NO'
print run(arr, n)


T = int(input())
t = 2
while t <= T:
    n = int(input())
    nums = list(map(int, input().split()))
    l = len(nums)
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    value = []
    for k in dic.keys():
        value.append(dic[k])
    if max(value) > (sum(value) - max(value)):
        print ('NO')
    else:
        print ('YES')
    t += 1




n=int(input())
s = input()
m=int(input())
nums = []
for i in range(m):
    s=input()
    nums.append(s)

def rept(a):
    i=len(a)
    j=0
    nn = n-n%i
    while j<nn and s[j:j+1]==a:
        j+=1
    if j==nn:
        return True
    else:
        return False
count = 0
for a in nums:
    rst = rept(a)
    if rst is True:
        cnt += 1
print(count)


# coding=utf-8
import itertools
import sys

def helper(arr):
    return len(sorted(list(set(map(''.join, itertools.permutations(arr))))))


def run(n, p, q):
    s = 0
    save = []
    for i in range(p, n + 1):
        for j in range(q, n + 1):
            if (i + j) ==n:
                ss = []
                for k in range(i):
                    ss.append('1')
                for k in range(j):
                    ss.append('0')
                r = helper(ss)


                s = s + r
                for m in range(r):
                    save.append(i)


    res = 0.0
    for i in save:
        res += i * (1.0 / s)
    
    return res % 1000000007


if __name__ == '__main__':

    data=sys.stdin.readline().strip()
    data_arr=data.split(' ')
    n=int(data_arr[0])
    p = int(data_arr[1])
    q = int(data_arr[2])

    print run(n,p,q)

   
    # print run(2, 1, 0)
    # # print -3.5%2
    # # print 333333337*3%1000000007