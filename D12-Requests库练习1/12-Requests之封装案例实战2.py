#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 9:52
# @Author  : Aries
# @Site    : 
# @File    : 12-Requests之封装案例实战2.py
# @Software: PyCharm
'''
第二种封装的套路
思路:重新对源码进行解释
def request(method, url, **kwargs):
	return session.request(method=method, url=url, **kwargs)

def get(url, params=None, **kwargs):
	return request('get', url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):
	return request('post', url, data=data, json=json, **kwargs)
'''
import requests

class Requests:
	def request(self,url,method='get',**kwargs):
		if method=='get':
			return requests.request(url=url,method=method,**kwargs)
		elif method=='post':
			return requests.request(url=url,method=method,**kwargs)
	def get(self,url,**kwargs):
		return self.request(url=url,**kwargs)
	def post(self,url,**kwargs):
		return self.request(url=url,method='post',**kwargs)

#对类进行初始化
obj=Requests()
#导入数据
url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'
data={'mobileCode':'18292016624','userID':''}
headers={'Content-Type':'application/x-www-form-urlencoded'}
#验证是否正确
r=obj.post(url=url,data=data,headers=headers)
print(r.text)