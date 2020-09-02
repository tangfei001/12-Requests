#!/usr/bin/env python
#author:wuya

import  requests

'''
application/x-www-form-urlencoded-->data json!=
application/json-->json格式的字符串数据类型-->字符串
data
json
'''


# data={'mobileCode':'13487659846','userID':''}
# headers={'Content-Type':'application/x-www-form-urlencoded'}
# r=requests.post(
# 	url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
# 	data=data,
# 	headers=headers)
# print(r.text)

'''
json:
1、满足的要求：application/json-->json格式的字符串数据类型
2、请求参数必须是字典
但是2必须在1的条件下才可以
'''

import json

# data={'author':'⽆涯','done':True,'name':'API测试实战'}
# # headers={'Content-Type':'application/json'}
# # r=requests.post(
# # 	url='http://localhost:5000/v1/api/books',
# # 	data=data,
# # 	headers=headers)
# # print(r.text)


'''
url:www.wuya.com
data={'name':'wuya','age':18,'data':[{''}]}
'''
datas={'name':'wuya','age':18,'data':[{'address':'xian'}]}

data1={'name':'wuya','age':18,'data':'books'}
headers={'content-type':'application'}
#--->json格式的字符串-->str

datas['data']=json.dumps(datas['data'])
r=requests.post(url='',json=datas,headers=headers)
#


