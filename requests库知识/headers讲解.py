#!/usr/bin/env python
#author:wuya

import  requests
import json

'''查询电话所在地'''
# data={'mobileCode':'13487659846','userID':''}
# headers={'Content-Type':'application/x-www-form-urlencoded'}
# r=requests.post(
# 	url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
# 	data=data,headers=headers)
# print(r.text)

data={'first':False,'pn':2,'kd':'测试架构师'}
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
	'Referer':'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E6%9E%B6%E6%9E%84%E5%B8%88?labelWords=&fromSearch=true&suginput=',
	'Cookie':'_ga=GA1.2.1192073820.1565486994; user_trace_token=20190811092953-851f62ea-bbd7-11e9-8906-525400f775ce; LGUID=20190811092953-851f65d0-bbd7-11e9-8906-525400f775ce; LG_HAS_LOGIN=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d7d6c57e0142-0d7b7654397f4d-5b123211-1049088-16d7d6c57e1403%22%2C%22%24device_id%22%3A%2216d7d6c57e0142-0d7b7654397f4d-5b123211-1049088-16d7d6c57e1403%22%7D; LG_LOGIN_USER_ID=6da1e8450385538577fbd5d6908f612e07e591546bfa997a; JSESSIONID=ABAAABAAAEEAAII25CDF5E1B47B7AD123A98D1A9FFC2592; WEBTJ-ID=20200203220306-1700b5ca76e64c-03050a8803827e-33365801-1049088-1700b5ca76f5a2; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1578193819,1578837638,1580738587; LGSID=20200203220307-e724bbb4-468d-11ea-af22-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.104755060.1580738588; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=e97fc2efd9d54ae980c0a23dfcee7086; X_HTTP_TOKEN=c83880c5c002968c3958370851cf8ec4c2f46da814; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1580738594; LGRID=20200203220314-eb70ccc0-468d-11ea-af22-5254005c3644'
}

params={'needAddtionalResult':False}
r=requests.post(
	url='https://www.lagou.com/jobs/positionAjax.json',
	data=data,
	params=params,
	headers=headers)
print(json.dumps(r.json(),indent=True,ensure_ascii=False))