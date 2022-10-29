# -*- coding: utf-8 -*-
# @Time     : 2021/2/23 22:36
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : os操作.py
# Software  : PyCharm


import os

file_path = os.path.abspath(__file__)
print(file_path)

dir_name = os.path.dirname(file_path)
print(dir_name)

# 创建文件
# os.mkdir(os.path.join(dir_name, 'data'))
#
# with open('data.txt', mode='w', encoding='utf-8') as f:
#     f.write('qwe')

