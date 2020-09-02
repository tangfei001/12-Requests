#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 9:52
# @Author  : Aries
# @Site    : 
# @File    : 12-Requests之封装案例实战1.py
# @Software: PyCharm
'''
第一种封装思路:直接调用
固定数据: 请求方法 请求地址
剩余的数据 **kwargs
'''
import requests

class Requests:
	def get(self, url, **kwargs):
		try:
			return requests.get(url=url, **kwargs)
		except BaseException as e:
			print(e.args[0])

	def post(self, url, **kwargs):
		try:
			return requests.post(url=url, **kwargs)
		except BaseException as e:
			print(e.args[0])

#对类进行初始化
obj=Requests()
#导入我们的数据-post请求
url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'
data={'mobileCode':'18292016624','userID':''}
headers={'Content-Type':'application/x-www-form-urlencoded'}
#验证封装是否完成
r=obj.post(url=url,data=data,headers=headers)
print(r.text)
