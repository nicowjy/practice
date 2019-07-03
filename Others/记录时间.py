#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time     : 2019-07-03 23:42:03
# @Author   : Nico
# chcp 65001 解决乱码
import time
 
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

s=time.time()
count = 0
for i in range(100000000):
    count += i&1
end=time.time()

print "位运算耗时", end-s  # 12.5320000648

s=time.time()
count = 0
for i in range(100000000):
    count += i%2
end=time.time()

print "取余运算耗时", end-s  # 13.6440000534