#!/usr/bin/env python
#author:wuya

import requests

'''
https://yuedu.baidu.com/search?word=%CE%DE%D1%C4&pbook=0
'''
# params={'word':'无涯','pbook':0}
# r=requests.get(
# 	url='https://yuedu.baidu.com/search',
# 	params=params)
# print(r.url)
# print(r.content.decode('gbk'))

'''
post请求:
url:http://httpbin.org/post?wuya=name&age=18
data={'address':'xian'}
请求方法：POST
'''


data={'address':'xian'}
params={'name':'wuya','age':18}
r=requests.post(
	url='http://httpbin.org/post',
	data=data,
	params=params)


