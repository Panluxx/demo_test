# -*- coding: utf-8 -*-
# @Time     : 2022/6/1 21:10
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test2.py
# Software  : PyCharm

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 3))
