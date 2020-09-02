#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 8:41
# @Author  : Aries
# @Site    : 
# @File    : 07-Requests之SESSION的案例实战.py
# @Software: PyCharm
'''
session的处理过程
1、发送登录请求
2、登录成功后，把sessionID的信息返回给客户端
3、客户端再次发送请求，需要在请求头里面(cookie)带上返回的sessionID
'''
'''
已知条件
01-登录函数login()
	地址: 'https://www.680.com/inc_vk/login.asp'
	请求参数:
		'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"
	请求头:
	'content-type':"application/x-www-form-urlencoded",
	'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
	"Referer":"https://www.680.com/login.html"
	请求类型:get
02:profile()
	地址:'https://user.680.com/financelist.aspx'
	提示:此处有第三步
	请求类型:get
作业:
根据提示完成这个接口的编写
	
'''
import requests

def login():
	params={'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"}
	headers={'content-type':"application/x-www-form-urlencoded",
	'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
	"Referer":"https://www.680.com/login.html"}
	r=requests.get(url='https://www.680.com/inc_vk/login.asp',
	               params=params,
	               headers=headers)
	return r.cookies

def profile():
	r=requests.get(url='https://user.680.com/financelist.aspx',
	               cookies=login())
	print(r.text)


profile()