#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 0:42
# @Author  : Aries
# @Site    : 
# @File    : 01-有依赖性.py
# @Software: PyCharm
'''
已知条件
01-测试类  ApiTest()
	001-获取token的函数 getToken()
		请求类型:post
		请求数据 'username':'wuya','password':'asd888'
		url='http://127.0.0.1:5000/auth'
	002-公用的请求头
		'Content-Type':'application/json'
		'Authorization': 'jwt {0}'.format(self.getToken)
02-接口测试用例
	001-添加书籍 test_book_001()
		请求类型:post
		请求数据:"author":"测试","done":True,"name":"API测试实战"
		url='http://127.0.0.1:5000/v1/api/books'
		请求头:公用的请求头
	002-查询书籍 test_book_002()
		请求类型:get
		请求头:公用的请求头
		url='http://127.0.0.1:5000/v1/api/book/1  1:是动态参数
	003-删除书籍 test_book_003
		请求类型 delete
		url='http://127.0.0.1:5000/v1/api/book/3'
		请求头:公用请求头
	004- 查看书籍  test_book_004()
		请求类型:get
		url='http://127.0.0.1:5000/v1/api/books'
03-四个接口测试用例的断言
	01-使用 assertEqual()
	02-返回的数据形式 json
	03-test_book_001
		status 1002
		响应状态吗  200
	04-test_book_002
		响应状态吗 200
		author 测试
		status 0
	05- test_book_003
		status 1009
		响应状态吗 200
'''
import unittest
import requests

#对Requests库进行封装
class Requests:
	def request(self,url,method='get',**kwargs):
		if method=='get':
			return requests.request(url=url,method=method,**kwargs)
		elif method=='post':
			return requests.request(url=url,method=method,**kwargs)
		elif method=='delete':
			return requests.request(url=url, method=method, **kwargs)

	def get(self,url,**kwargs):
		return self.request(url=url,**kwargs)

	def post(self,url,**kwargs):
		return self.request(url=url,method='post',**kwargs)

	def delete(self,url,**kwargs):
		return self.request(url=url,method='delete',**kwargs)

#编写测试类ApiTest()
class ApiTest(unittest.TestCase):
	#对requests进行实例化
	def setUp(self) -> None:
		self.obj=Requests()
	#获取token的值-写成特性方法
	@property
	def getToken(self):
		data={'username':'wuya','password':'asd888'}
		r=self.obj.post(url='http://127.0.0.1:5000/auth',json=data)
		return r.json()['access_token']
	#将请求头单独提出来-使用特性方法
	@property
	def getHeaders(self):
		headers={'Authorization': 'jwt {0}'.format(self.getToken),
		         'Content-Type':'application/json'}
	#写两个方法获取动态参数id-使用Open函数
	def write(self,bookID):
		with open('bookID','W') as f:
			f.write(str(bookID))
	def read(self):
		with open('bookID','r') as f:
			return f.read()
	'''
	05:写接口测试用例
    06:加入断言
    07:注意事项
        01-将得到的请求头放到对应的请求中
        02-对应请求的url中的ID是动态参数-
	001-吧获取到的id代入到url中去
	002-使用字符串的格式化方法
        03-将获取到的id放到对应的接口请求中去
	'''
	def test_book_001(self):
		'''添加书籍'''
		url='http://127.0.0.1:5000/v1/api/books'
		data={"author":"测试","done":True,"name":"API测试实战"}
		r=self.obj.post(url=url,json=data,headers=self.getHeaders)
		'''加入获取的id'''
		self.write(r.json()[0]['datas']['id'])
		'''断言'''
		self.assertEqual(r.json()[0]['status'],1002)
		self.assertEqual(r.status_code,200)
	def test_book_002(self):
		'''查询书籍'''
		url='http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read())
		r=self.obj.get(url=url,headers=self.getHeaders)
		'''断言'''
		self.assertEqual(r.json()[0]['author'],'测试')
		self.assertEqual(r.status_code,200)
	def test_book_003(self):
		'''删除书籍'''
		url = 'http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read())
		r=self.obj.delete(url=url,headers=-self.getHeaders)
		'''断言'''
		self.assertEqual(r.json()[0]['status'],1009)
		self.assertEqual(r.status_code,200)
	def test_book_004(self):
		'''查看数据'''
		url ='http://127.0.0.1:5000/v1/api/books'
		r=self.obj.get(url=url,headers=self.getHeaders)

#主函数
if __name__ == '__main__':
    unittest.main(verbosity=2)

