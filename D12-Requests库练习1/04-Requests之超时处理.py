#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 8:26
# @Author  : Aries
# @Site    : 
# @File    : 04-Requests之超时处理.py
# @Software: PyCharm
'''
已知条件
url:
	'http://httpbin.org/get'
超是处理关键字: timeout
请求类型:get
作业
01:要求超时60秒
02:完成接口测试
'''
import requests
r=requests.get(url='http://httpbin.org/get',
               timeout=60)
print(r.text)