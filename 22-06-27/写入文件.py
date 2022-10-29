# -*- coding: utf-8 -*-
# @Time     : 2021/6/11 21:22
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 写入文件.py
# Software  : PyCharm


str_1 = 'url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456\nurl:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000'

with open('data.txt', mode='w', encoding='utf-8') as f:
    f.write(str_1)
