# -*- coding: utf-8 -*-
# @Time     : 2022/6/1 21:36
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test03.py
# Software  : PyCharm


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 5))


def add(x, y):
    return x ** y


print(add(3, 5))
