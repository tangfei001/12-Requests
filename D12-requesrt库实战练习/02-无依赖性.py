#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 10:13
# @Author  : Aries
# @Site    : 
# @File    : 02-无依赖性.py
# @Software: PyCharm


import  unittest
import  requests

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

class ApiTest(unittest.TestCase):
	def setUp(self) -> None:
		self.obj=Requests()

	@property
	def getToken(self):
		data={'username':'wuya','password':'asd888'}
		r=self.obj.post(url='http://127.0.0.1:5000/auth',json=data)
		return r.json()['access_token']

	@property
	def getHeaders(self):
		headers = {
			'Authorization': 'jwt {0}'.format(self.getToken),
			'Content-Type':'application/json'}
		return headers

	def write(self,bookID):
		with open('bookID','w') as f:
			f.write(str(bookID))

	def read(self):
		with open('bookID','r') as f:
			return f.read()
	#将添加和删除单独写一个方法
	def addBook(self):
		data={"author":"测试","done":True,"name":"API测试实战"}
		r=self.obj.post(
			url='http://127.0.0.1:5000/v1/api/books',
			json=data,
			headers=self.getHeaders)
		return r

	def delBook(self):
		r=self.obj.delete(
			url='http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read()),
			headers=self.getHeaders)
		return r

	def selBook(self):
		r = self.obj.get(
			url='http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read()),
			headers=self.getHeaders)
		return r
	#
	def test_book_c(self):
		'''添加书籍'''
		r=self.addBook()
		self.delBook()
		self.write(r.json()[0]['datas']['id'])
		self.assertEqual(r.json()[0]['status'],1002)
		self.assertEqual(r.status_code,200)

	def test_book_b(self):
		'''查询'''
		self.addBook()
		r=self.selBook()
		self.delBook()
		self.assertEqual(r.json()['datas'][0]['author'], '测试')
		self.assertEqual(r.json()['status'],0)
		self.assertEqual(r.status_code, 200)

	def test_book_a(self):
		'''删除'''
		self.addBook()
		r=self.delBook()
		self.assertEqual(r.json()['status'],1009)
		self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main(verbosity=2)
