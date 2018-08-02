#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


# 递归实现
def Fibonacci_1(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci_1(n-1) + Fibonacci_1(n-2)


def Fibonacci_2(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    for i in range(2, n+1):
        n1, n2 = n2, n1+n2
    return n2

# res = Fibonacci_1(100)
res = Fibonacci_2(20)
print(res)
