#!/usr/bin/env python
#author:wuya

import  requests

# r=requests.request(
# 	method='GET',
# 	url='http://httpbin.org/get')
# print(r.text)

# r=requests.get(
# 	url='http://httpbin.org/get',
# 	params=None)
# print('请求地址:',r.url)
# print('响应头:',r.headers)
# print('json格式的数据:',r.json())
# print('基本文本的数据:',r.text)
# print('二进制的内容:',r.content)
# print('状态:',r.status_code)
# print('cookies:',r.cookies)

'''R.JSON的错误演示'''
# r=requests.get('http://www.baidu.com/')
# print(r.status_code)
# print(r.text)

'''r.content的演示'''
# r=requests.get('http://www.weather.com.cn/')
# print(r.content.decode('utf-8'))

'''r.cookies'''
# r=requests.get('http://www.weather.com.cn/')
# print(r.cookies.get_dict())


'''http://httpbin.org/get?name=wuya?age=18'''

r=requests.post(url='http://httpbin.org/post')
print(r.status_code)
print(r.text)




