# -*- coding: utf-8 -*-
# @Time     : 2021/1/28 22:40
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : while_01.py
# Software  : PyCharm

# n = 0
# while True:
#     print('123')
#     if n == 2:
#         break
#     n += 1
#
# m = 0
# while m < 3:
#     print('321')
#     m += 1
#
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(i, sum)
#
# n = 0
# for i in range(1, 101):
#     n += i
# print(n)

i = 1
result = 0
while i <= 100:
    if i % 3 == 0:
        result += i
        i += 1
    else:
        i += 1
print(i)

