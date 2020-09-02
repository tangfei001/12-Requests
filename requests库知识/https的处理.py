#!/usr/bin/env python
#author:wuya

import  requests

r=requests.get(
	url='https://www.wuya.com/',verify=True)
print(r.text)


