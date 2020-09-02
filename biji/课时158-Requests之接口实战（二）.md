课时158-Requests之接口实战（二）

2:基于业务的考虑:每个测试点之间户型没有依赖性

'''
代码解析
第一步:对Requests库进行封装
第二步:将所要测试的类放到一个类中 ApiTest(unittest.TestCase)
	01:对Requests库进行实例化
	02:使用面向对象中对象的特性获取token值
	03:使用面向对象中对象的特性方法获取请求头(要带上token)
	04:写两个函数获取动态参数
	05:将添加,删除,查看的函数单独写成方法
	06:调用各自的函数
		001:每次调用完成后都需要进行删除函数
'''



import  unittest
import  requests

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
	#06
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
3主函数
if __name__ == '__main__':
    unittest.main(verbosity=2)
