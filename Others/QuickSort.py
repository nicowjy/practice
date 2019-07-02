# -*- coding: utf-8 -*-
# @Time     : 07/01/2019
# @Author   : Nico
'''
import random
class Lst:
    def Partition(self, data, start, end):
        if data == [] or start < 0 or end >= len(data):
            return 'Invalid Parameters'
        
        index = random.randint(start, end)
        data[index], data[end] = data[end], data[index]

        low = start
        while low < end:
            if data[index] < data[end]:
                if low != index:
                    data[index], data[low] = data[low], data[index]
            low += 1

        data[low], data[end] = data[end], data[low]
        return low

    def QuickSort(self, data, start, end):
        if start == end:
            return

        index = self.Partition(data, start, end)
        if index > start:
            self.QuickSort(data, start, index-1)
        if index < end:
            self.QuickSort(data, index+1, end)

if __name__ == "__main__":
    lst1 = Lst()
    print lst1.QuickSort([5,2,3,9,7], 0, 4)
'''

# 快速排序
# 定义一个非递归的主函数，其中调用一个递归定义的函数，给定划分范围初值
def quick_sort(lst):
    qsort_rec(lst, 0, len(lst)-1)
    return lst

# 递归过程
def qsort_rec(lst, l, r):
    if l >= r:                             # 无分段记录或只有一个记录
        return
    i = l
    j = r
    pivot = lst[i]                         # lst[i]为初始空位
    while i < j:                           # 找pivot的最终位置
        while i < j and lst[j] >= pivot:
            j -= 1                         # 用j向左扫描找到小于pivot的记录
        if i < j:
            lst[i] = lst[j]
            i += 1                         # 小记录移到左边
        while i < j and lst[i] <= pivot:
            i += 1                         # 用i向右扫描找到大于pivot的记录
        if i < j:
            lst[j] = lst[i]
            j -= 1                         # 大记录移到右边
    lst[i] = pivot                         # 将pivot存入为其确定的最终位置
    qsort_rec(lst, l, i-1)                 # 递归处理左半区间
    qsort_rec(lst, i+1, r)                 # 递归处理右半区间

print quick_sort([5,2,3,9,7])