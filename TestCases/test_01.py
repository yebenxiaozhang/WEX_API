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
import json


class Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.A = ShopApi()
        self.ShopText = GlobalMap()

    @classmethod
    def setUpClass(cls) -> None:
        # cls.key = key()
        cls.token = None
        cls.openid = None
        cls.userid = None

    def assignment(self, kwargs):
        for key, value in kwargs.items():
            if type(value) is dict:
                self.assignment(value)
            if value:
                pass
            else:
                kwargs[key] = None

        return kwargs

    def test_02(self):
        """
        :return:
        """
        import csv
        import warnings
        warnings.simplefilter('ignore', ResourceWarning)
        #  1.创建文件对象
        f = open('csv_file.csv', 'w+', encoding='utf-8')

        #  2.基于文件对象构建csv写入对象
        csv_write = csv.writer(f)
        import time
        #  3.构建列表头
        csv_write.writerow(['序号', '执行时间', 'SQL'])
        dome = 1
        banana = 1
        while dome != -1:
            self.A.GetSQL()
            time.sleep(5)
            globals()['text'] = json.loads(self.ShopText.get('TEXT'))
            demo1 = 0
            while globals()['text']['Content'][demo1]['TotalTime'] > 3000:
                csv_write.writerow([dome, globals()['text']['Content'][demo1]['TotalTime'],
                                    globals()['text']['Content'][demo1]['SQL']])
                demo1 = demo1 + 1
                if demo1 == 40 and banana == 1:
                    banana = banana + 1
                    self.A.SendMail()
                if demo1 == 100:
                    globals()['text']['Content'][demo1]['TotalTime'] = 100
            dome = dome + 1

        f.close()

    def test_0031(self):
        # 去重CSV 重复项
        import shutil
        import pandas as pd
        frame = pd.read_csv('D:/wex_api/TestCases/csv_file.csv', engine='python')

        data = frame.drop_duplicates(subset=['SQL'], keep='first', inplace=False)
        # 如subset=['A','B']去A列和B列重复的数据
        # subset: column label or sequence of  labels, optional
        # 用来指定特定的列，默认所有列
        # keep: {‘first’, ‘last’, False}, default ‘first’
        # 删除重复项并保留第一次出现的项
        # inplace: boolean, default False
        # 是直接在原来数据上修改还是保留一个副本
        data.to_csv('D:/wex_api/TestCases/2022042802庞氏口腔慢查询SQL.csv', encoding='utf8')
    #
    # def test_03(self):
    #     """
    #
    #     :return:
    #     """
    #     from Common.GetNewPatient import new_patient
    #     dome = 0
    #     while dome != 66:
    #         import time
    #         time.sleep(0.5)
    #         x, y = new_patient()
    #         # print(x, y)
    #         # self.A.GetCookie(uName=13062200300, password='Pan19951105', shopName='胡里店')
    #         # self.A.GetSelect(dictType='PATIENT_TAG2')
    #         self.A.AddPatient(patientName=x, phone1=y, phone1Belong='b807385b4a6e4899a5b6a5013d7dbd8d',
    #                           introducerType=30,
    #                           mutual=0, black=0, fromTemp=0, sexcheckbox=0, blackcheckbox=0)
    #         dome = dome + 1
    #
    # def test_04(self):
    #     """
    #
    #     :return:
    #     """
    #
    #     import csv
    #     import warnings
    #     warnings.simplefilter('ignore', ResourceWarning)
    #     #  1.创建文件对象
    #     f = open('csv_file.csv', 'w', encoding='utf-8')
    #
    #     #  2.基于文件对象构建csv写入对象
    #     csv_write = csv.writer(f)
    #     import time
    #     #  3.构建列表头
    #     csv_write.writerow(['patientId', 'patientName'])
    #     dome = 100
    #     while dome != 1:
    #         # time.sleep(5)
    #         demo1 = 0
    #         self.A.GetPatientData(page=dome)
    #         import json
    #         globals()['text'] = json.loads(self.ShopText.get('TEXT'))
    #         while demo1 != 15:
    #             csv_write.writerow([globals()['text']['rows'][demo1]['patientId'],
    #                                 globals()['text']['rows'][demo1]['patientName']])
    #             demo1 = demo1 + 1
    #         dome = dome + 1
    #
    #     f.close()
