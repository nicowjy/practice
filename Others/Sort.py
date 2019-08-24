# -*- coding: utf-8 -*-
# @Time     : 07/01/2019
# @Author   : Nico
# 快排
def quick_sort(nums):
    if not nums:
        return []

    def partition(start, end):
        if start >= end:
            return None
        left, right = start, end
        p = nums[end]
        while left < right:
            while left < right and nums[left] <= p:
                left += 1
            if left < right:
                nums[right] = nums[left]
                right -= 1
            while left < right and nums[right] >= p:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
        nums[left] = p
        partition(start, left-1)
        partition(left+1, end)
    
    partition(0, len(nums)-1)
    return nums

# 归并
def merge_sort(nums):
    if not nums:
        return []

    def merge(nums, interval):
        start = 0
        tmp = []
        while start + interval < len(nums):
            i, j, end = start, start+interval, min(len(nums), start+2*interval)
            while i < start+interval and j < end:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            tmp += nums[i:start+interval] if i < start+interval else nums[j:end]
            start += 2*interval
        tmp += nums[start:]
        return tmp

    interval = 1
    while interval < len(nums):
        tmp = merge(nums, interval)
        interval *= 2
        nums = merge(tmp, interval)
        interval *= 2
    return nums
    
# 堆排序
def heap_sort(nums):
    def sift_down(start, end):
        e = nums[start]
        i, j = start, 2*start+1
        while j < end:
            if j+1 < end and nums[j+1] > nums[j]:
                j += 1
            if e > nums[j]:
                break
            nums[i] = nums[j]
            i, j = j, 2*j+1
        nums[i] = e
    
    end = len(nums)
    for i in range(end/2-1, -1, -1):
        sift_down(i, end)
    for i in range(end-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(0, i)
    return nums

# 选择排序
def select_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        k = 0
        for j in range(i+1):
            if nums[j] >= nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
    return nums

# 插入排序
def insert_sort(nums):
    for i in range(1, len(nums)):
        e = nums[i]
        j = i
        while j > 0 and nums[j-1] > e:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = e
    return nums

# 起泡排序
def bubble_sort(nums):
    for i in range(len(nums)):
        found = False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                found = True
        if not found:
            break
    return nums

nums = [5,2,3,9,7,4,0,4]
print bubble_sort(nums)