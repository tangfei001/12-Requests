**课时150-Requests之TOKEN的案例实战**

token的请求流程
1、发送请求登录
2、登录成功后，服务端返回给客户端的响应数据中，包含了token
   {"nick":"wuya","token":"rtyuio45678fdg"}
3、客户端再次发送请求（比如查看各个人主页），那么就需要在客户端里面带上token
   a、客户端的请求参数里面 {"user":3465,"token":"rtyuio45678fdg"}
   b、请求头里面
   headers={'Authorization':'jwt {0}'.format(login())}

已知条件

登录函数post login()
	url='http://127.0.0.1:5000/auth'
	json
	没有请求头
	请求数据 'username':'wuya','password':'asd888' 
token信息
	access_token

查看书籍函数book()
	url='http://127.0.0.1:5000/v1/api/books'
	headers={'Authorization':'jwt {0}'.format(login())}

案例实战:
import requests
#先写登陆函数login()
def login():
	#请求数据data
	data={'username':'wuya','password':'asd888'}
	#写post请求
	r=requests.post(url='http://127.0.0.1:5000/auth',
	                json=data)
	# #获取token值
	# print(r.text)
	#拿到这个token后返回来这个值
	return r.json()['access_token']

#在写一个查看书籍的函数books()
def books():
	#请求头别忘了-使用字符串格式化的方法
	headers={'Authorization':'jwt {0}'.format(login())}
	#写get函数
	r=requests.get(url='http://127.0.0.1:5000/v1/api/books',
	               headers=headers)
	print(r.text)
