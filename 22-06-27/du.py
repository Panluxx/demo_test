# -*- coding: utf-8 -*-
# @Time     : 2021/6/11 21:27
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : du.py
# Software  : PyCharm


file = open('data.txt', encoding='utf-8')

list_a = []
for items in file.readlines():
    dict_a = {}
    for item in items.strip('\n').split('@'):
        dict_a[item.split(':')[0]] = item.split(':')[1]
    list_a.append(dict_a)
file.close()
print(list_a)
