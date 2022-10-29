# -*- coding: utf-8 -*-
# @Time     : 2021/3/11 21:28
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : config配置文件.py
# Software  : PyCharm

import os
from configparser import ConfigParser

# conf = ConfigParser()
# conf.read('setting.ini', encoding='utf-8')
# data = conf.get('excel', 'file_name')
# print(data)

setting_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setting.ini')
conf = ConfigParser()
conf.read(setting_name, encoding='utf-8')
print(conf.get('excel', 'file_name'))
