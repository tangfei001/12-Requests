#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 9:52
# @Author  : Aries
# @Site    : 
# @File    : 11-Requests之文件上传案例实战.py
# @Software: PyCharm
'''
文件上传关键字 file
files={'file':('logo.jpg',open('C:/logo.jpg','rb'),'image/jpeg',{})}
		'logo.jpg':文件名称
		open('C:/logo.jpg','rb'):以二进制方式读取文件
		'image/jpeg':文件类型
		{}:固定写法
'''
import requests
'''
已知条件
01:登录函数login()
   01:url='http://www.renren.com/PLogin.do'
   02:请求参数
	'email':'13484545195','password':'asd888','icode':'','oriGurl':'http://www.renren.com/home',
	      'domain':'renren.com','key_id':1,'captcha_type':'web_login'
   03:请求头:
	'Content-Type':'application/x-www-form-urlencoded',
	         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
   04:请求类型post
   05:提示需要用到session回话技术
02:profile()
	01:url='http://www.renren.com/967004081'
	02:请求类型:get

03:函数upload():
	01:地址:url='http://upload.renren.com/upload.fcgi?pagetype=addpublishersingle&hostid=967004081&callback=window.parent.handlePhotoData&uploadid=profile_publisher_photo_1581214721178'
	02:请求数据:
		'upload':'提交','__channel':'renren','privacyParams':'{"sourceControl": 99}',
	      'hostid':'967004081','requestToken':'-1453954216','_rtk':'751769b2'
	03:请求头:
		{'Content-Type':'multipart/form-data'
	04:files 文件上传关键字	{'file':(文件名称,open('文件路径','rb'),文件类型,{})}
		files={'file':('logo.jpg',open('C:/logo.jpg','rb'),'image/jpeg',{})}
	05:请求类型 post
'''
def login():
	#加入session()回话
	s=requests.Session()
	#正常的接口
	url='http://www.renren.com/PLogin.do'
	data={'email':'13484545195','password':'asd888','icode':'','oriGurl':'http://www.renren.com/home',
	      'domain':'renren.com','key_id':1,'captcha_type':'web_login'}
	headers={'Content-Type':'application/x-www-form-urlencoded',
	         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
	r=s.post(url=url,
	         data=data,
	         headers=headers)
	return s

#第二个函数
def profile():
	r=login().get(url='http://www.renren.com/967004081')
	print(r.text)

#第三个函数
def upload():
	url='http://upload.renren.com/upload.fcgi?pagetype=addpublishersingle&hostid=967004081&callback=window.parent.handlePhotoData&uploadid=profile_publisher_photo_1581214721178'
	data={'upload':'提交','__channel':'renren','privacyParams':'{"sourceControl": 99}',
	      'hostid':'967004081','requestToken':'-1453954216','_rtk':'751769b2'}
	#重点部分
	'''
	files={'file':('logo.jpg',open('C:/logo.jpg','rb'),'image/jpeg',{})}
	'logo.jpg':文件名称
	open('C:/logo.jpg','rb'):以二进制方式读取文件
	'image/jpeg':文件类型
	{}:固定写法
	'''
	files={'file':('logo.jpg',open('C:/logo.jpg','rb'),image/jpeg,{})}
	headers={'Content-Type':'multipart/form-data'}
	r=login().post(url=url,
	               data=data,
	               files=files,
	               headers=headers)
	print(r.text)
#调用函数upload()
upload()
