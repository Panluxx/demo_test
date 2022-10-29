# -*- coding: utf-8 -*-
# @Time     : 2021/4/12 22:10
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : handler_request.py
# Software  : PyCharm


import requests
from jsonpath import jsonpath

headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
login_url = 'http://api.lemonban.com/futureloan/member/login'
login_data = {"mobile_phone": "18377567762", "pwd": "123456789"}

res = requests.post(login_url, json=login_data, headers=headers)
print(res.json())
token = res.json()['data']['token_info']['token']
print(token)
id = res.json()['data']['id']
print(id)

recharge_url = 'http://api.lemonban.com/futureloan/member/recharge'
recharge_data = {"member_id": id, "amount": 5000}
headers['Authorization'] = 'Bearer ' + token

res = requests.post(recharge_url, json=recharge_data, headers=headers)
print(res.json())
