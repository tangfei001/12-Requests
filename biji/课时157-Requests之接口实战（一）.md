**课时157-Requests之接口实战（一）**

编写api测试点两种思路:
1.基于业务的复杂性考虑:每个测试点之间有依赖性
2:基于业务的考虑:每个测试点之间户型没有依赖性

问题:代码级别的编写接口测试用例

'''
代码解析:
第一步:对Requests库进行封装
第二步:将所要测试的类放到一个类中 ApiTest(unittest.TestCase)
	01:对Requests库进行实例化
	02:使用面向对象中对象的特性获取token值
	03:使用面向对象中对象的特性方法获取请求头(要带上token)
	04:写两个函数获取动态参数
	05:编写我们的接口测试用例
		001:编写对应的接口测试用例
		002:在添加书籍函数中吧id的值写进去
		003:在所有测试的接口用例的url中加入id的值
		004:对每个测试用例进行断言
第三步:主函数进行执行

'''
import requests
import unittest

#第一步
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
#第二步
class ApiTest(unittest.TestCase):
	#01
	def setUp(self) -> None:
		self.obj=Requests()
	#02
	@property
	def getToken(self):
		data={'username':'wuya','password':'asd888'}
		r=self.obj.post(url='http://127.0.0.1:5000/auth',json=data)
		return r.json()['access_token']
	
	#03
	@property
	def getHeaders(self):
		headers = {
			'Authorization': 'jwt {0}'.format(self.getToken),
			'Content-Type':'application/json'}
		return headers
	#04
	def write(self,bookID):
		with open('bookID','w') as f:
			f.write(str(bookID))
	
	def read(self):
		with open('bookID','r') as f:
			return f.read()
	
	#05
	def test_book_001(self):
		'''添加书籍'''
		data={"author":"测试","done":True,"name":"API测试实战"}
		r=self.obj.post(
			url='http://127.0.0.1:5000/v1/api/books',
			json=data,
			headers=self.getHeaders)
		#002--验证书籍食发鬼添加成功
		self.write(r.json()[0]['datas']['id'])
		#004
		self.assertEqual(r.json()[0]['status'],1002)
		self.assertEqual(r.status_code,200)

	def test_book_002(self):
		'''查询'''
		#003
		r=self.obj.get(
			url='http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read()),
			headers=self.getHeaders)
		#004
		self.assertEqual(r.json()['datas'][0]['author'], '测试')
		self.assertEqual(r.json()['status'],0)
		self.assertEqual(r.status_code, 200)

	def test_book_003(self):
		'''删除'''
		#003
		r=self.obj.delete(
			url='http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read()),
			headers=self.getHeaders)
		#004
		self.assertEqual(r.json()['status'],1009)
		self.assertEqual(r.status_code, 200)

	def test_book_004(self):
		r=self.obj.get(
			url='http://127.0.0.1:5000/v1/api/books',
			headers=self.getHeaders)
#第三步
if __name__ == '__main__':
    unittest.main(verbosity=2)



