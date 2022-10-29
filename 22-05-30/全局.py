# -*- coding: utf-8 -*-
# @Time     : 2021/2/19 22:49
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 全局.py
# Software  : PyCharm


a = 'xixi'


def run():
    global a
    a = 'dod'
    print(a)
    return a


run()
print(a)

b = 'man'


def offer(name):
    print('这个叫{}很{}的'.format(name, b))
    eat(name, '冰激凌')


def eat(name, food):
    print('这个叫{}的喜欢吃{}'.format(name, food))


offer('Pan.')
