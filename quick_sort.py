#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


def partition(nums, start, end):
    target = nums[end]
    small = start
    for i in range(start, end):
        if nums[i] < target:
            nums[i], nums[small] = nums[small], nums[i]
            small += 1
    nums[small], nums[end] = nums[end], nums[small]
    return small


def quick_sort(nums, start, end):
    if start >= end:
        return
    m = partition(nums, start, end)
    quick_sort(nums, start, m - 1)
    quick_sort(nums, m + 1, end)


nums = [1, 20, 2, 9, 15, 3, 10, 11, 12, 4]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
