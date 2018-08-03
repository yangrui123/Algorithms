#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


def moving_count(rows, cols, k):
    if rows <= 0 or cols <= 0 or k < 0:
        return 0
    visited = []
    for i in range(rows):
        visited.append([0]*cols)
    count = moving_count_core(rows, cols, 0, 0, visited, k)
    return count


def moving_count_core(rows, cols, i, j, visited, k):
    count = 0
    if check(rows, cols, i, j, k) and visited[i][j] == 0:
        visited[i][j] = 1
        count = 1 + moving_count_core(rows, cols, i, j-1, visited, k) \
                + moving_count_core(rows, cols, i, j+1, visited, k) \
                + moving_count_core(rows, cols, i-1, j, visited, k) \
                + moving_count_core(rows, cols, i+1, j, visited, k)

    return count


def check(rows, cols, i, j, k):
    if 0<= i < rows and 0<= j < cols and getsum(i)+getsum(j)<=k:
        return True
    return False


def getsum(number):
    total = 0
    while number > 0:
        total += number%10
        number = number//10
    return total