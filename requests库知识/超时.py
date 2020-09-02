#!/usr/bin/env python
#author:wuya


'''
固定时间---》time
'''


import requests

r=requests.get('http://httpbin.org/get',
               timeout=60)
print(r.text)