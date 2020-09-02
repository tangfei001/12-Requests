课时149-Requests之复杂请求参数处理

已知条件:
url:www.wuya.com
data={'name':'wuya','age':18,'data':[{'address':'xian'}]}
headers={'content-type':'application/json'}

import requests
import json

datas={'name':'wuya','age':18,'data':[{'address':'xian'}]}
headers={'content-type':'application'}
'''
01:通过这个content-type可以看出是json形式的字符串
02:使用json对字典的序列化来做
'''
#datas['data']:获取到字典中key对应的具体value值
datas['data']=json.dumps(datas['data'])
r=requests.post(url='xxxx',
                json=datas,
                heasers=headers)
print(r.text)
