#!/usr/bin/env python  
# coding=utf-8  
while 1:
    a=[]
    s = raw_input()
    n, m = int(s.split(' ')[0]), int(s.split(' ')[1])
    for i in range(n):
        s = raw_input()
        if s != "":
            a.append([int(x) for x in s.split(' ')])
        else:
            break
    print biaomianji(n, m, a)


def biaomianji(n, m, matrix):
    face = [0] * m
    left = [0] * n
    has = [[0]*m for x in range(n)]
    add = 0
    for i in range(n):
        left[i] = max(matrix[i])
        for j in range(m):
            if matrix[i][j] > 0:
                has[i][j] = 1
            face[j] = max(face[j], matrix[i][j])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                add += 4
    
    return sum(face)*2 + sum(left)*2 + sum([sum(x) for x in has])*2

print biaomianji(2, 2, [[2,1],[1,1]])

y = [4,4,3,3,2]
print ' '.join([str(x) for x in y])