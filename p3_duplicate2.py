#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


"不修改数组找出重复的数字"
"在一个长度为n+1的数组里的所有数字都在1~n的范围内， 所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，" \
"但不能修改输入的数组。例如，如果输入长度为8的数组{2,3,5,4,3,2,6,7},那么对应的输出是重复的数字2或者3"


def count(nums, left, right):
    total = 0
    for item in nums:
        if item >= left and item <= right:
            total += 1
    return total


# 时间nlogn,空间O(1)
def getDuplication(nums):
    if len(nums) <= 1:
        return False
    n = len(nums)-1
    left = 1
    right = n
    while left < right:
        mid = left + right >> 1
        total = count(nums, left, mid)
        if total > mid - left + 1:
            right = mid
        else:
            left = mid + 1
    return left


nums = [2, 3, 5, 4, 4, 6,7,4]
res = getDuplication(nums)
print(res)