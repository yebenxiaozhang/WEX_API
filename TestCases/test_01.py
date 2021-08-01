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


class Test(unittest.TestCase):

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
        pass

