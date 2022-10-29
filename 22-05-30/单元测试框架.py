# -*- coding: utf-8 -*-
# @Time     : 2021/3/4 21:30
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 单元测试框架.py
# Software  : PyCharm


import unittest


def add(a, b):
    return a + b


x = 2
y = 3
expected = 5


class TestAdd(unittest.TestCase):

    def test_add_success(self):
        self.assertEqual(expected, add(x, y))


if __name__ == '__main__':
    unittest.main()
