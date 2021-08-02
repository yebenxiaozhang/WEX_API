"""
============================
Author: 潘师傅
Time: 2021/8/2 18:23
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import requests
# import selenium



R = requests.get(url='http://www.baidu.com')

print(R.text)
print(R.status_code)