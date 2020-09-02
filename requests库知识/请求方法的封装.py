#!/usr/bin/env python
#author:wuya


'''
请求方法
请求地址
方法，地址 **kwargs
'''

import  requests

class Method:
	def get(self,url,**kwargs):
		try:
			return requests.get(url=url, **kwargs)
		except BaseException as e:
			return e.args[0]

	def post(self,url,**kwargs):
		try:
			return requests.post(url=url, **kwargs)
		except BaseException as e:
			return e.args[0]

# url='http://www.renren.com/PLogin.do'
# data={'email':'13484545195','password':'asd888','icode':'','oriGurl':'http://www.renren.com/home',
#       'domain':'renren.com','key_id':1,'captcha_type':'web_login'
#       }
# headers={'Content-Type':'application/x-www-form-urlencoded',
#          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
#          }
# obj=Method()
# r=obj.post(url=url,data=data,headers=headers)
# print(r.text)


'''第二种封装的思路'''
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


# obj=Requests()
# url='http://www.renren.com/PLogin.do'
# data={'email':'13484545195','password':'asd888','icode':'','oriGurl':'http://www.renren.com/home',
#       'domain':'renren.com','key_id':1,'captcha_type':'web_login'
#       }
# headers={'Content-Type':'application/x-www-form-urlencoded',
#          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
#          }
# r=obj.post(url=url,data=data,headers=headers)
# print(r.text)



# def f1(a,b,c):
# 	return a+b+c
#
# def f2(a,b,c):
# 	return f1(a=a,b=b,c=c)
#
# def f3(a):
# 	return f2(a=a)
#
# print(f3('hello'))

class A:
	pass

def b():
	pass
