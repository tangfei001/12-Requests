#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 9:50
# @Author  : Aries
# @Site    : 
# @File    : 09-Requests之鉴权案例实战.py
# @Software: PyCharm
'''
鉴权的处理思路
from   requests.auth   import  HTTPBasicAuth
auth={'asmin','asmin}

url='http://127.0.0.1:5000/v1/api/books'
请求类型:get
'''
import requests
from requests.auth import HTTPBasicAuth

r=requests.get(url='http://127.0.0.1:5000/v1/api/books',
               auth={'asmin':'asmin'})
print(r.text)