# -*- coding: utf-8 -*-
# @Time     : 2021/3/4 20:31
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 类的继承.py
# Software  : PyCharm


class Parent:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_name(self, data):
        return self.name + data

    def get_password(self):
        return self.password


class Son(Parent):

    def __init__(self, name, password):
        super().__init__(name, password)
        print('继承init')

    def get_name(self, data):
        super().get_name(data)
        print(f'继承get_name{data}')


class Sunzi(Son):
    pass


son = Son('qwe', 'weq')
son.get_name('ddd')

sun = Sunzi('234','234')
sun.get_name('aaa')
