#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


"位运算"
def numberof1(n):
    count = 0
    while n:
        count += 1
        n = (n-1) & n
    return count


def numberof1_2(n):
    count = 0
    flag = 1
    while flag <= n:
        if flag & n:
            count += 1
        flag = flag << 1
    return count


res = numberof1(25)
print(res)
res = numberof1_2(25)
print(res)
