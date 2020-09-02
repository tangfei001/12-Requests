#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 8:34
# @Author  : Aries
# @Site    : 
# @File    : 06-Requests之TOKEN的案例实战.py
# @Software: PyCharm

'''
token的请求流程
1、发送请求登录
2、登录成功后，服务端返回给客户端的响应数据中，包含了token
   {"nick":"wuya","token":"rtyuio45678fdg"}
3、客户端再次发送请求（比如查看各个人主页），那么就需要在客户端里面带上token
   a、客户端的请求参数里面 {"user":3465,"token":"rtyuio45678fdg"}
   b、请求头里面
'''
'''
已知条件:
01:登录函数login()
	01:地址 'http://127.0.0.1:5000/auth'
	02:请求数据  'username':'wuya','password':'asd888' 
	03:请求类型: post
	04:json
02:查看书籍函数books()
	01:地址:'http://127.0.0.1:5000/v1/api/books'
	02:请求头: Authorization':'jwt {0}
		提示:此处要使用字符串格式虎,
	03:请求类型: get
03:返回的token信息
	access_token
	格式:json
作业:
	完成这个接口的练习
'''
import requests

def login():
	data={'username':'wuya','password':'asd888'}
	r=requests.post(url='http://127.0.0.1:5000/auth',
	                json=data)
	#拿到这个返回值
	return r.json()['access_token']

def profile():
	'''
	在请求头里面带上我们得到的token值
	因为token是个动态值所以这样处理
	'''
	headers={'Authorization':'jwt {0}'.format(login())}
	r=requests.get(url='http://127.0.0.1:5000/v1/api/books',
	               headers=headers)
	print(r.text)
profile()