# -*- coding: utf-8 -*-
# @Time     : 2022/7/6 21:07
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_time.py
# Software  : PyCharm


import time

print(time.time())
print(time.asctime())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
