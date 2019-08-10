#!/usr/bin/python
# -*- coding: utf-8 -*-
# 开根号(牛顿迭代)
def sqrt_newton(num):
    x = num*1.0/2
    while abs(x**2 - num) > 0.001:
        x = x/2 + num/(2*x)
    return x

print sqrt_newton(3)