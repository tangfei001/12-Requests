#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 8:29
# @Author  : Aries
# @Site    : 
# @File    : 05-Requests之复杂请求参数处理.py
# @Software: PyCharm
'''
已知条件:
请求类型:post
url: www.wuya.com
请求数据: {'name':'wuya','age':18,'data':[{'address':'xian'}]}
请求头: 'content-type':'application'
提示:此处使用json
	使用json的序列化对address数据进行处理
	datas['data']:获取到字典中key对应的具体value值
作业:
01-完成这个接口的编写
02-写出你的处理思路
'''
import requests
import json

datas={'name':'wuya','age':18,'data':[{'address':'xian'}]}
headers={ 'content-type':'application'}
#复杂参数的处理
'''
处理思路
01:使用json库
02:使用json调字典的序列化和反序列化进行处理
'''
datas['data']=json.dumps(datas['data'])

r=requests.post(url='www.wuya.com',
                json=datas,
                headers=headers)
print(r.text)
