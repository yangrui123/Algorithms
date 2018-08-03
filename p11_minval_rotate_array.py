#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


"旋转数组的最小数字"
"把一个数组的最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转，输入一个递增排序的数组的一个旋转，输出旋转数组的" \
"最小元素。"


# 遍历数组,时间：O(n)
def min_inorder(nums):
    if not nums:
        return
    small = nums[0]
    for item in nums:
        small = min(item, small)
    return small


# 二分查找方法，时间O(nlogn)
def min_binary_search(nums):
    if not nums:
        return
    left = 0
    right = len(nums) - 1
    minIndex = left
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
        minIndex = left + right >> 1
        if nums[minIndex] == nums[left] and nums[left] == nums[right]:
            return min_inorder(nums)
        if nums[minIndex] >= nums[left]:
            left = minIndex
        else:
            right = minIndex
    return nums[minIndex]


nums = [1,1,1,0,1]
res = min_binary_search(nums)
print(res)