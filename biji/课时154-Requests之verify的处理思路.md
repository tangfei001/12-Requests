**课时154-Requests之verify的处理思路**

verify(错误的提示信息)

解决思路: verifty=True

案例演示:
import requests
r=requests.get(url='xxxxx',verifty=True)
print(r.text)
