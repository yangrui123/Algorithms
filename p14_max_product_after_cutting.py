#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

"剪绳子"


# DP方法：
def max_product_dp(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    products = []
    products.extend([0,1,2,3])
    max_value = 0
    for i in range(4, n+1):
        for j in range(1, i//2+1):
            x = j * products[i-j]
            max_value = max(max_value, x)
        products.append(max_value)
    return products[-1]


def max_products_greedy(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    timesOf3 = n // 3
    if n - timesOf3*3 == 1:
        timesOf3 -= 1
    products = (3**timesOf3) * (2**(n-timesOf3*3>>1))
    return products

res = max_product_dp(6)
print(res)
res = max_products_greedy(6)
print(res)