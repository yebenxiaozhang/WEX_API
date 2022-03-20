"""
============================
Author: 潘师傅
Time: 2021/8/1 21:42
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""

import unittest
from ddt import file_data
from AllAPI.ShopApi import *
from Common.GlobalMap import GlobalMap

A = ShopApi()
ShopText = GlobalMap()

import csv
import warnings
warnings.simplefilter('ignore', ResourceWarning)
#  1.创建文件对象
f = open('221csv_file.csv', 'w+', encoding='utf-8')

#  2.基于文件对象构建csv写入对象
csv_write = csv.writer(f)
import time
#  3.构建列表头
csv_write.writerow(['序号', '执行时间', 'SQL'])
dome = 1
while dome != -1:
    time.sleep(5)
    A.GetSQL()
    import json
    globals()['text'] = json.loads(ShopText.get('TEXT'))
    demo1 = 0
    while globals()['text']['Content'][demo1]['TotalTime'] > 3000:
        csv_write.writerow([dome, globals()['text']['Content'][demo1]['TotalTime'],
                            globals()['text']['Content'][demo1]['SQL']])
        demo1 = demo1 + 1
        print(demo1)
        if demo1 == 100:
            globals()['text']['Content'][demo1]['TotalTime'] = 3000
    dome = dome + 1

f.close()
