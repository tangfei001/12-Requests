#!/usr/bin/env python
#author:wuya


import  requests

def login():
	s=requests.Session()
	url='http://www.renren.com/PLogin.do'
	data={'email':'13484545195','password':'asd888','icode':'','oriGurl':'http://www.renren.com/home',
	      'domain':'renren.com','key_id':1,'captcha_type':'web_login'
	      }
	headers={'Content-Type':'application/x-www-form-urlencoded',
	         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
	         }
	r=s.post(url=url,data=data,headers=headers)
	return s


def profile():
	r=login().get(url='http://www.renren.com/967004081')
	print(r.text)

def upload():
	url='http://upload.renren.com/upload.fcgi?pagetype=addpublishersingle&hostid=967004081&callback=window.parent.handlePhotoData&uploadid=profile_publisher_photo_1581214721178'
	data={'upload':'提交','__channel':'renren','privacyParams':'{"sourceControl": 99}',
	      'hostid':'967004081','requestToken':'-1453954216','_rtk':'751769b2'
	      }
	files={'file':('logo.jpg',open('C:/logo.jpg','rb'),'image/jpeg',{})}
	headers={'Content-Type':'multipart/form-data'}
	r=login().post(url=url,data=data,files=files,headers=headers)
	print(r.text)

upload()