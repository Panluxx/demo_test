# -*- coding: utf-8 -*-
# @Time     : 2022/7/6 22:11
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test2.py
# Software  : PyCharm


def get_score():
    try:
        score = float(input('请输入你的分数：'))
        if score < 60:
            print('不合格')
        elif 60 <= score <= 80:
            print('良好')
        else:
            print('优秀')
    except Exception as e:
        raise Exception('输入值错误', e)




get_score()
