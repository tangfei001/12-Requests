**课时144-Requests之概述与源码解读**

import requests
def request(method, url, **kwargs):
	xxxx

'''
method--请求方法 get post put delete
url---地址
**kwargs--动态参数
'''
--------------------------------------------
返回的内容说明
print('请求地址:',r.url)
print('响应头:',r.headers)
print('json格式的数据:',r.json())
print('基本文本的数据:',r.text)
print('二进制的内容:',r.content)
print('状态:',r.status_code)
print('cookies:',r.cookies)
---------------------------------------------