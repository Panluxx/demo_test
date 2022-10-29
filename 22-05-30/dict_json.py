# -*- coding: utf-8 -*-
# @Time     : 2021/1/19 22:04
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : dict_json.py
# Software  : PyCharm

dict1 = {'q': '1', 'b': '2', 'c': '3'}
print(type(dict1))
dict1['g'] = '4'
print(dict1)
dict1['c'] = '12'
print(dict1)

for key, value in dict1.items():
    print(key, value)
