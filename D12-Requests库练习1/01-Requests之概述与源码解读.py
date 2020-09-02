#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 8:18
# @Author  : Aries
# @Site    : 
# @File    : 01-Requests之概述与源码解读.py
# @Software: PyCharm
'''
要求:
在看一遍课时144
说明:使用代码的方式进行接口测试
核心:用代码的方式执行接口测试用例
核心:requests
'''
import requests
def request(method, url, **kwargs):
	xxxx

'''
method--请求方法 get post put delete
url---地址
**kwargs--动态参数
'''
'''
返回的内容说明
print('请求地址:',r.url)
print('响应头:',r.headers)
print('json格式的数据:',r.json())
print('基本文本的数据:',r.text)
print('二进制的内容:',r.content)
print('状态:',r.status_code)
print('cookies:',r.cookies)
'''