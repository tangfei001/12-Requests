#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 9:51
# @Author  : Aries
# @Site    : 
# @File    : 10-Requests之verify的处理思路.py
# @Software: PyCharm
'''
verify(错误的提示信息)
解决思路: verifty=True
'''
import requests

r=requests.get(url='xxxxxx',
               verify=True)
print(r.text)
