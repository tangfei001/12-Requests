**课时153-Requests之鉴权案例实战**

import  requests
from   requests.auth   import  HTTPBasicAuth


r=requests.get(
	url='http://127.0.0.1:5000/v1/api/books',
	auth=('admin','admin'))
print(r.text)


鉴权-就是认证
postman--工具
jmeter---工具
requests---代码

