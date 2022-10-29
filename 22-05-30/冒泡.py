# -*- coding: utf-8 -*-
# @Time     : 2021/1/29 21:33
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 冒泡.py
# Software  : PyCharm

a = [1, 3, 4, 2, 5, 88888, 444, 6666, 777, 322, 432, 4432, 434, 3]

for num_one in range(len(a) - 1):
    mix_num = num_one
    for num_two in range(num_one + 1, len(a)):
        if a[num_two] < a[num_one]:
            a[num_one], a[num_two] = a[num_two], a[num_one]
print(a)


