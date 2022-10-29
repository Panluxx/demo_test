# -*- coding: utf-8 -*-
# @Time     : 2022/7/6 20:56
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_os.py
# Software  : PyCharm


import os


print(os.path.abspath('test_os.py'))
print(os.path.normpath('D://Git//demo_test//22-07-05//test_os.py'))
print(os.path.relpath('D://Git//demo_test//22-07-05//test_os.py'))
print(os.path.dirname(r'D:\Git\demo_test\22-07-05\test_os.py'))
print(os.path.basename(r'D:\Git\demo_test\22-07-05\test_os.py'))
print(os.path.exists(r'D:\Git\demo_test\22-07-05\test_os.py'))
print(os.path.join(r'D:\Git\demo_test\22-07-05', 'test.txt'))
print(os.getlogin())
print(os.cpu_count())
print(os.getcwd())
