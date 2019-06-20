#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : Tuesday, March 5th 2019, 4:39:46 pm
# @Author   : Nico

import random
def Partition(data, start, end):
    if data == [] or start < 0 or end >= len(data):
        return 'Invalid Parameters'
    
    index = random.randint(start, end)
    data[index], data[end] = data[end], data[index]

    low = start
    while low < end:
        if data[index] < data[end]:
            low += 1
            if low != index:
                data[index], data[low] = data[low], data[index]
    
    low += 1
    data[low], data[end] = data[end], data[low]

    return low

lst1 = [5,2,3,9,7]
Partition(lst1, 0, 4)