# -*- coding: utf-8 -*-
# @Time     : 2022/8/10 22:01
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test1.py
# Software  : PyCharm

import pytest


class TestDemo(object):
    def test_one(self):
        a = 1
        b = 2
        assert a == b


if __name__ == '__main__':
    pytest.main()
