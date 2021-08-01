# import urllib3
# import requests
# urllib3.disable_warnings()
#
# # Fiddler抓取到的URL和Cookie值
# url = "http://116.63.143.113:8082/his/patient/getPatientData"
# Cookie = 'wexShop=04519E29DD49FD91D945BF84C9EAB020; sysType=1; _wex_captcha=f71aebd1f4d943dd954d741d1cc905e7'
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0",
#     'Cookie': Cookie    # 将Cookie值添加到header请求头中
# }
#
# # session = requests.session()
# response = requests.post(url=url, headers=header, verify=False)
# print(response.text)
# print(response.cookies)
# print(response.status_code)
# # 2710763f8b08fb149cefcb77d65b78b5c4c23b60b0ffbca7aaa0408d9b15e5271613bb148bdf1a0b2e7dfa572f47fe263d73a6520a5b73268033122bb859304f6def703079329d55a7371dd54ec724e3810792b544ac1ea1cf3e050da06b78cc5dd9ed863d4711d24e92527285a779f07c442681f5cf55b22526776102e7b62f
# # 67c4eea0ded2082ae689801999b21cf4b6bd7e435469870d9f698d54660bc388e2ea69b614be07b828dc8130bd64fc0bda80d198b78629918b6a792d0593bf9f538de0cc0f975f88fe6f7ac400345e320087f2a937fd286c0a8dff5a35113e3f96b8d903313baf6a923f89416fdb82596eb835cd6fc5c1039545acc56c41890f
# # ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413
#

com = None
if com is None:
    print('111')
else:
    print(22)