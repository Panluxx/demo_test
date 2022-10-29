# -*- coding: utf-8 -*-
# @Time     : 2022/7/12 21:00
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test2.py
# Software  : PyCharm


import yaml

with open('demo1.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    print(data['login']['data'])
    for dic in data['login']['data']:
        print(dic)


# with open('demo1.yaml', 'a+') as f:
#     yaml.dump(data={'a': 1}, stream=f)
