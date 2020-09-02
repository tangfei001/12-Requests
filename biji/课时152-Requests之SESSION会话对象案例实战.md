**课时152-Requests之SESSION会话对象案例实战**

已知条件

01-登录函数login()
    请求类型:get
	地址:'https://www.680.com/inc_vk/login.asp'
	请求参数
			'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"
	请求头:
		'content-type':"application/x-www-form-urlencoded",
		'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
		"Referer":"https://www.680.com/login.html"
02-查看数据profile()
	请求类型:get
	请求地址:'https://user.680.com/financelist.aspx'

-----------------------------------------------------------
回话对象具有主要的Request APU的所有方法

回话对象的用法
def login():
   s=requests.Session()
   r=s.get(xxxx)
   return s

def login2():
   r=login2.get()
   print(r.text)

login2()
------------------------
案例实战:
import  requests

def login(url='https://www.680.com/inc_vk/login.asp'):
	s=requests.Session()
	params={'yz':0,'yzm':"","uid":"13484545195","pwd":"asd888",
	        "lgs":0,"callback":"jsonp1580910280481","rnd":"0.2264766513954488"}
	headers={
		'content-type':"application/x-www-form-urlencoded",
		'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
		"Referer":"https://www.680.com/login.html"
	}
	r=s.get(url=url,params=params,headers=headers)
	return s

def profile():
	r=login().get(
		url='https://user.680.com/financelist.aspx')
	print(r.text)

profile()
