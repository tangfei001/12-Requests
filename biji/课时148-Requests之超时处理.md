**课时148-Requests之超时处理**

01-固定时间--time

解决思路:添加timeout

import requests

r=requests.get('http://httpbin.org/get',timeout=60)
print(r.text)
