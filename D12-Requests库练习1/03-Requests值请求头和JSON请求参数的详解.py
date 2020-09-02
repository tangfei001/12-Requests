#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 8:23
# @Author  : Aries
# @Site    : 
# @File    : 03-Requests值请求头和JSON请求参数的详解.py
# @Software: PyCharm
'''
已知条件
POST /WebServices/MobileCodeWS.asmx/getMobileCodeInfo HTTP/1.1
Host: ws.webxml.com.cn
Content-Type: application/x-www-form-urlencoded
Content-Length: length

mobileCode=string&userID=string

作业:
1:headers
2:post请求json请求参数的运用
3:完成这个接口的练习
'''
import requests

data={'mobileCode':'18292016624','userID':''}
headers={'Content-Type':'application/x-www-form-urlencoded'}
r=requests.post(url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
                data=data,
                headers=headers)
print(r.text)