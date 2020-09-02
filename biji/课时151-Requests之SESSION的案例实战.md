**课时151-Requests之SESSION的案例实战**

session的处理过程
1、发送登录请求
2、登录成功后，把sessionID的信息返回给客户端
3、客户端再次发送请求，需要在请求头里面(cookie)带上返回的sessionID

已知条件
登录函数login()
	url='https://www.680.com/inc_vk/login.asp'
	请求参数params
	'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"
	headers:
	'content-type':"application/x-www-form-urlencoded",
	'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
	"Referer":"https://www.680.com/login.html"
	get请求

 profile()函数
	url='https://user.680.com/financelist.aspx'
	cookie
------------------------------------------------
案例演示
import requests
def login(url='https://www.680.com/inc_vk/login.asp'):
	params={'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"}
	headers={'content-type':"application/x-www-form-urlencoded",
	'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
	"Referer":"https://www.680.com/login.html"}
	r=requests.get(url=url,
	               params=params,
	               headers=headers)
	return r.cookies

def profile():
	r=requests.get(url='https://user.680.com/financelist.aspx',
	               cookies=login())
	print(r.text)
#调用函数
profile()