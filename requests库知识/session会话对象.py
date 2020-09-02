#!/usr/bin/env python
#author:wuya

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

