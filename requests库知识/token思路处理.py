#!/usr/bin/env python
#author:wuya


import  requests

'''
1、发送请求登录
2、登录成功后，服务端返回给客户端的响应数据中，包含了token
   {"nick":"wuya","token":"rtyuio45678fdg"}
3、客户端再次发送请求（比如查看各个人主页），那么就需要在客户端里面带上token
   a、客户端的请求参数里面 {"user":3465,"token":"rtyuio45678fdg"}
   b、请求头里面
'''
#
# r=requests.get('http://127.0.0.1:5000/v1/api/books')
# print(r.text)

def login():
	data={"username":"wuya","password":"asd888"}
	r=requests.post(
		url='http://127.0.0.1:5000/auth',
		json=data)
	return r.json()['access_token']

def books():
	headers={'Authorization':'jwt {0}'.format(login())}
	r=requests.get(
		url='http://127.0.0.1:5000/v1/api/books',
		headers=headers)
	print(r.text)

