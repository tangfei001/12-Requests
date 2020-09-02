#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 8:20
# @Author  : Aries
# @Site    : 
# @File    : 02-Requests之params参数练习.py
# @Software: PyCharm
'''
已知条件:
url:
	https://yuedu.baidu.com/search?word=wuya4&pbook=0
请求类型:get
解码方式:gbk
要求:使用代码的方式完成这个接口的编写
'''
import requests

params={'word':'wuya','phook':0}
r=requests.get(url='https://yuedu.baidu.com/search',
               params=params)
print(r.content.decode('gbk'))
