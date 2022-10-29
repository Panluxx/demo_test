# -*- coding: utf-8 -*-
# @Time     : 2021/3/2 22:16
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 类的使用.py
# Software  : PyCharm


class Shui:

    def __init__(self, big):
        self.big = big

    def eat(self):
        return f'吃{self.big}苹果'

    @staticmethod
    def oo():
        return '这是个静态的方法'


shui = Shui('大')
print(shui.eat())
print(shui.oo())


class Ping(Shui):

    def yanse(self):
        return '吃锤子'


ping = Ping('小')
print(ping.eat())
print(ping.yanse())
