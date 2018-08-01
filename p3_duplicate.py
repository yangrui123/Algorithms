#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

"找出数组中重复的数字"
"在一个长度为n的数组里的所有数字都在0~n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字" \
"重复的次数。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2,3,1,0,2,5,3},那么对应的输出是重复的数组2或者3"


# 方法一：sort，时间nlogn
def sort():
    pass


# 方法二：hash 时间复杂度：n；空间：n
def hash():
    pass


# 方法三：
def getDuplication(nums):
    if nums == []:
        return False
    for item in nums:
        if item < 0 or item >= len(nums):
            return False
    for i in range(len(nums)):
        item = nums[i]
        while item != i:
            if item == nums[item]:
                return item
            nums[i], nums[item] = nums[item], nums[i]
            item = nums[i]
    return False


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    res = getDuplication(nums)
    print(res)
