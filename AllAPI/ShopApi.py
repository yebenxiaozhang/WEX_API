"""
============================
Author: 潘师傅
Time: 2021/8/2 13:48
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import requests
import configparser

from Common.GlobalMap import GlobalMap
from Common.HandleRequests import HandleRequest
config = configparser.ConfigParser()
config.read("../Conf/wex.ini", encoding="UTF-8")


class ShopApi:

    def __init__(self):
        self.ShopText = GlobalMap()
        self.Request = HandleRequest()

    def GetPatient(self, keyword=None):
        """
        患者资料列表
        :param keyword:  关键字 姓名/电话/档案号
        :return:
        """

        self.Request.Request(url='/common/quickSearch',
                             data={
                                 'd': keyword
                             })

    def GetTemporaryPatient(self, keyword=None, page=1, rows=15, start=None, end=None):
        """
        临时患者列表
        :param keyword: 关键字  姓名/电话/档案号
        :param page:    第几页
        :param rows:    每页显示的数量
        :param start:   开始时间
        :param end:     结束时间
        :return:
        """
        self.Request.Request(url='/his/patient/getTemporaryData',
                             data={
                                 'search': keyword,
                                 'page': page,
                                 'rows': rows,
                                 'start': start,
                                 'end': end
                             })

    def AddPatient(self):
        self.Request.Request(url='/his/patient/patientAdd',
                             data={

                             })


if __name__ == '__main__':
    a = ShopApi()
