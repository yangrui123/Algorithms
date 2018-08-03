#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


def has_path(matrix, s):
    record = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        record.append([0] * n)
    idx = 0
    for i in range(m):
        for j in range(n):
            if has_path_core(matrix, s, i, j, idx, record):
                return True
            record[i][j] = 0
    return False


def has_path_core(matrix, s, row, col, idx, record):
    if idx == len(s):
        return True
    if 0<=row<len(matrix) and 0<=col<len(matrix[0]) and matrix[row][col] == s[idx] and record[row][col] == 0:
        record[row][col] = 1
        if has_path_core(matrix, s, row, col-1, idx+1, record) or has_path_core(matrix, s, row, col+1, idx+1, record) \
               or has_path_core(matrix, s, row-1, col,idx+1, record) or has_path_core(matrix, s, row+1, col, idx+1, record):
            return True
        record[row][col] = 0
    return False



s = 'abfcsh'
matrix = [['a', 'b', 't', 'g'],
          ['c', 'f', 'c', 's'],
          ['j', 'd', 'e', 'h']]
res = has_path(matrix, s)
print(res)


