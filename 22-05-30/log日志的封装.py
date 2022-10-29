# -*- coding: utf-8 -*-
# @Time     : 2021/3/14 9:55
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : log日志的封装.py
# Software  : PyCharm


import logging


# # 初始化日志收集器
# logger = logging.getLogger('python22期日志收集器')
#
# # 设置日志收集器的级别
# logger.setLevel(logging.DEBUG)
#
# # 设置日志处理器
# # 控制台输出
# console_handler = logging.StreamHandler()
# # 文件输出
# file_handler = logging.FileHandler('demo.log', encoding='utf-8')
#
# # 设置处理器级别
# console_handler.setLevel(logging.DEBUG)
# file_handler.setLevel(logging.WARNING)
#
# # 添加处理器到收集器里面
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
#
#
# # 添加日志格式
# console_fmt = logging.Formatter('%(asctime)s-%(filename)s')
# file_fmt = logging.Formatter('%(asctime)s-%(filename)s')
#
#
# # 设置格式与处理器关联
# console_handler.setFormatter(console_fmt)
# file_handler.setFormatter(file_fmt)
#
#
# # 调用
# logger.debug('debug日志级别')
# logger.warning('warning日志级别')


class LoggerHandler(logging.Logger):

    def __init__(self, name, level, log_file, handler_level, fmt='%(asctime)s-%(filename)s-%(levelname)s-%(message)s', **kw):
        super().__init__(name, level=level)

        if not log_file:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(log_file, encoding='utf-8')

        handler.setLevel(handler_level)

        self.addHandler(handler)

        handler_fmt = logging.Formatter(fmt)
        handler.setFormatter(handler_fmt)


logger = LoggerHandler('python22', level=0, log_file='demo.log', handler_level=0)
