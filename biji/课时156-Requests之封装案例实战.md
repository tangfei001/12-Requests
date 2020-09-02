**课时156-Requests之封装案例实战**

请求方法的封装

'''
请求方法
请求地址
思路
方法 地址 **kwargs
'''

第一种封装方法-直接调用

import requests
class Method:
	def get(self,url,**kwargs):
		try:
			return requests.get(url=url,**kwargs)
		except BaseException as e:
			print(e.args[0])

	def post(self,url,**kwargs):
		try:
			return requests.post(url=url,**kwargs)
		except BaseException as e:
			print(e.args[0])

#调用方法:
obj=Method()
r=obj.get(url='http://www.baidu.com')
print(r.status_code)
print(r.text)
-----------------------
第二种封装方法:
对requests库的源码进行解

def request(method, url, **kwargs):
	return session.request(method=method, url=url, **kwargs)

def get(url, params=None, **kwargs):
	return request('get', url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):
	return request('post', url, data=data, json=json, **kwargs)
-------------------------------------------------------------------
案例演示
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

#进场初始化
obj=Requests()
#导入数据-post请求
url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'
data={'mobileCode':'18292016624','userID':''}
headers={'Content-Type':'application/x-www-form-urlencoded'}
#验证数据
r=obj.post(url=url,data=data,headers=headers)
print(r.text)