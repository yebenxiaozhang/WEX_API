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

    def test_01(self):
        """
        dddd
        :return:
        """
        pass

    def test_02(self):
        """
        :return:
        """

        import csv
        import warnings
        warnings.simplefilter('ignore', ResourceWarning)
        #  1.创建文件对象
        f = open('csv_file.csv', 'w', encoding='utf-8')

        #  2.基于文件对象构建csv写入对象
        csv_write = csv.writer(f)
        import time
        #  3.构建列表头
        csv_write.writerow(['序号', '执行时间', 'SQL'])
        dome = 1
        while dome != -1:
            time.sleep(5)
            self.A.GetSQL()
            import json
            globals()['text'] = json.loads(self.ShopText.get('TEXT'))
            demo1 = 0
            while globals()['text']['Content'][demo1]['TotalTime'] > 4000:
                csv_write.writerow([dome, globals()['text']['Content'][demo1]['TotalTime'],
                                    globals()['text']['Content'][demo1]['SQL']])
                demo1 = demo1 + 1
            dome = dome + 1

        f.close()

    def test_03(self):
        """

        :return:
        """
        from Common.GetNewPatient import new_patient
        dome = 0
        while dome != 66:
            import time
            time.sleep(0.5)
            x, y = new_patient()
            print(x, y)
            # self.A.GetCookie(uName=13062200300, password='Pan19951105', shopName='胡里店')
            self.A.GetSelect(dictType='PATIENT_TAG2')
            # self.A.AddPatient(patientName=x, phone1=y, phone1Belong='b807385b4a6e4899a5b6a5013d7dbd8d', introducerType=30,
            #                   mutual=0, black=0, fromTemp=0, sexcheckbox=0, blackcheckbox=0)
            dome = dome + 1

    def test_04(self):
        """

        :return:
        """

        import csv
        import warnings
        warnings.simplefilter('ignore', ResourceWarning)
        #  1.创建文件对象
        f = open('csv_file.csv', 'w', encoding='utf-8')

        #  2.基于文件对象构建csv写入对象
        csv_write = csv.writer(f)
        import time
        #  3.构建列表头
        csv_write.writerow(['patientId', 'patientName'])
        dome = 100
        while dome != 1:
            # time.sleep(5)
            demo1 = 0
            self.A.GetPatientData(page=dome)
            import json
            globals()['text'] = json.loads(self.ShopText.get('TEXT'))
            while demo1 != 15:
                csv_write.writerow([globals()['text']['rows'][demo1]['patientId'],
                                    globals()['text']['rows'][demo1]['patientName']])
                demo1 = demo1 + 1
            dome = dome + 1

        f.close()
