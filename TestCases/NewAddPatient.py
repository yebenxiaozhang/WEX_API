"""
============================
Author: 潘师傅
Time: 2021/8/2 15:24
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""

import unittest
from ddt import file_data
from AllAPI.ShopApi import *
from Common.GlobalMap import GlobalMap
import json
from Common.GetNewPatient import new_patient


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

    def test_add_patient(self):
        """新建患者"""
        patient_name, patient_phone = new_patient()
        print(patient_name, patient_phone)
        self.A.add_patient(patient_name=patient_name, phone1=patient_phone)
