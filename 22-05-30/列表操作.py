# -*- coding: utf-8 -*-
# @Time     : 2021/1/18 20:48
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 列表操作.py
# Software  : PyCharm


print('hello world')

# n = 0
# for i in range(1, 101):
#     n += i
#     print(n)

str_list = '123, is, list'
print(type(str_list.strip(',')))
print(str_list.strip(' ').split(', '))

list_1 = ['1', '2', '3']
list_2 = ['6', '5', '4']
# list_1.append(list_2)
# print(list_1)

list_1.extend(list_2)
print(list_1)
list_1.pop(2)
print(list_1)
list_1.sort()
print(list_1)

print(float(0.1) + float(0.2))




