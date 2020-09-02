**课时145-Requests之params参数详解**

01:get请求

001-格式
def get(url, params=None, **kwargs):
	kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)

002-案例演示

已知一个地址: https://yuedu.baidu.com/search?word=%CE%DE%D1%C4&pbook=0

import requests

#对问号后面的内容进行分离
params={'word':'wuya','phook':0}
r= requests.get(
	url='https://yuedu.baidu.com/search',
	params=params)
print(r.content.decode('gbk'))

--------------------------------------------------------------------------
02:post请求
001-格式:
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
案例演示:
'''
post请求:
url:http://httpbin.org/post?wuya=name&age=18
data={'address':'xian'}
请求方法：POST
'''
002-案例演示

import requests

#分离数据
data={'address':'xian'}
params={'name':'wuya','age':18}

r=requests.post(
url='http://httpbin.org/post',
data=data,
params=params)