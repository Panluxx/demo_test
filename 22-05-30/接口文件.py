# -*- coding: utf-8 -*-
# @Time     : 2021/3/22 21:14
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : 接口文件.py
# Software  : PyCharm

from flask import Flask

app = Flask(__name__)


@app.route('/api')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
