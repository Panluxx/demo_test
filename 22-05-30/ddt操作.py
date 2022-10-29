# -*- coding: utf-8 -*-
# @Time     : 2021/3/17 21:10
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : ddt操作.py
# Software  : PyCharm


import unittest
import ddt
from log日志的封装 import logger


def add(a, b):
    return a + b


test_data = [
    ((1, 2), 2),
    ((1, 2), 3),
    ((1, 2), 4)
]


@ddt.ddt
class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = logger
        logger.debug('*' * 20 + 'test开始' + '*' * 20)

    @classmethod
    def tearDownClass(cls) -> None:
        logger.debug('*' * 20 + 'test结束' + '*' * 20)

    @ddt.data(*test_data)
    def test_add_success(self, test_data):
        try:
            self.assertEqual(test_data[1], add(*test_data[0]))
            self.logger.debug('测试通过')
        except:
            self.logger.warning('测试不通过')
            raise


if __name__ == '__main__':
    unittest.main()
