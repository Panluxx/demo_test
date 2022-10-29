# -*- coding: utf-8 -*-
# @Time     : 2021/3/9 21:05
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_add.py
# Software  : PyCharm

import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('用例执行前****')

    @classmethod
    def tearDownClass(self) -> None:
        print('用例执行后****')

    def setUp(self) -> None:
        self.data = [{'x': 3, 'y': 2, 'expected': 5},
                     {'x': 3, 'y': 4, 'expected': 8}]

    def test_add_success(self):
        self.assertEqual(self.data[0]['expected'],
                         add(self.data[0]['x'], self.data[0]['y']))

    def test_add_error(self):
        self.assertEqual(self.data[1]['expected'],
                         add(self.data[1]['x'], self.data[1]['y']))


if __name__ == '__main__':
    unittest.main()
