**课时147-Requests之JSON请求参数详解**

def post(url, data=None, json=None, **kwargs):


问题:在post请求中,什么时候使用data 什么时候使用json

解决:
	application/x-www-form-urlencoded-->data json!=
    application/json-->json格式的字符串数据类型-->字符串(字典的序列化)

使用json的条件
1、满足的要求：application/json-->json格式的字符串数据类型
2、请求参数必须是字典
但是2必须在1的条件下才可以


案例演示
import requests
import json

data={'author':'⽆涯','done':True,'name':'API测试实战'}
headers={'Content-Type':'application/json'}
r=requests.post(
	url='http://localhost:5000/v1/api/books',
	data=json.dumps(data),
	headers=headers)
print(r.text)