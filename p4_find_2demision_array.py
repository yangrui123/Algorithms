#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


"二维数组中的查找"
"在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个" \
"二维数组和一个整数，判断数组中是否含有该整数。"


# 时间n^2
def find(array, target):
    if array == [] or array == [[]]:
        return False
    if target < array[0][0] or target > array[-1][-1]:
        return False
    for i in range(len(array)):
        if array[i][0] > target:
            break
        for j in range(len(array[0])):
            if array[i][j] == target:
                return True
            if array[i][j] > target:
                break
    return False


# time:n
def search(array, target):
    if array == [] or array == [[]]:
        return False
    if target < array[0][0] or target > array[-1][-1]:
        return False
    i = 0
    j = len(array[0])-1
    while i < len(array) and j >= 0:
        if array[i][j] == target:
            return True
        if array[i][j] > target:
            j -= 1
        elif array[i][j] < target:
            i += 1
    return False


array = [[1,2,8,9],
         [2,4,9,12],
         [4,7,10,13],
         [6,8,11,15]]
target = 16
res = search(array, target)
print(res)