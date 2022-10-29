# -*- coding: utf-8 -*-
# @Time     : 2022/7/11 21:28
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test1.py
# Software  : PyCharm


data = [{"username": "18377560722", "password": "admin123456"}, {"username": "18377560722", "password": "admin123456"}]
for i in range(len(data)):
    data[i]['iss'] = 'pass'
print(data)
