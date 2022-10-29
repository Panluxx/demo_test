# -*- coding: utf-8 -*-
# @Time     : 2022/7/19 22:20
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : db_redis.py
# Software  : PyCharm
import re

import redis

conn = redis.Redis(host='127.0.0.1', port=6379, encoding="utf-8")
# value = conn.get('key1')
# print(value)
# value = str(value)
# print(value.strip("b'"))
for key in conn.keys():
    print(str(key).strip("b'"))


