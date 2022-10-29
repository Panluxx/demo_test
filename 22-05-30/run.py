# -*- coding: utf-8 -*-
# @Time     : 2021/3/9 20:38
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : run.py
# Software  : PyCharm

import os
import unittest
from BeautifulReport import BeautifulReport

loader = unittest.TestLoader()
cases_path = os.path.dirname(os.path.abspath(__file__))
suite = loader.discover(cases_path)
runner = BeautifulReport(suite)
runner.report(filename='pan', description='测试报告')
