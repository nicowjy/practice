#!/usr/bin/python
# -*- coding: utf-8 -*-


def fanzhuan(s):
    if not s:
        return ''
    res = ''
    words = s.split(' ')
    for word in words:
        if len(word)%2 == 1:
            res += word[::-1]
        else:
            res += word
        res += ' '
    return res[:-1]

while 1:
    s = raw_input()
    print fanzhuan(s)
print fanzhuan('zai lai yi bian')


def numDecoding(s):
    s = str(s)
    d = list()
    for i in range(1,27):
        d.append(str(i))
    dp = [0]*len(s)
    if s[0] in d:
        dp[0] = 1
    else:
        return 0    
    for i in range(1, len(s)):
        a = 0
        b = 0
        if s[i] in d:
            a = dp[i-1]
        if s[i-1:i+1] in d:
            if i == 1:
                b = 1
            else:
                b = dp[i-2]
        dp[i] = a+b
    return dp[-1]


s = raw_input()
print numDecoding(s)


s = raw_input()
h, w = int(s.split(' ')[0]), int(s.split(' ')[1])
pic = []
for i in range(h):
    s = raw_input()
    pic.append([int(x) for x in s.split(' ')])
s = raw_input()
m = int(s)
kernel = []
for i in range(m):
    s = raw_input()
    kernel.append([float(x) for x in s.split(' ')])

def juanji(h,w,m,pic,kernel):
    res = [[0]*(w-m+1) for i in range(h-m+1)]
    for i in range(h-m+1):
        for j in range(w-m+1):
            e = 0
            for a in range(m):
                for b in range(m):
                    e += kernel[i+a][i+b]*kernel[a][b]
            res[i][j] = e
    
    for i in range(len(res)):
        print ' '.join([str(int(j)) for i in res[j]])

print juanji(h,w,m,pic,kernel)



[]