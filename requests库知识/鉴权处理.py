#!/usr/bin/env python
#author:wuya

import  requests
from   requests.auth   import  HTTPBasicAuth


r=requests.get(
	url='http://127.0.0.1:5000/v1/api/books',
	auth=HTTPBasicAuth('admin','admin'))
print(r.text)