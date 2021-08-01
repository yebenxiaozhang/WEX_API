"""
============================
Author: 潘师傅
Time: 2021/7/31 16:25
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import urllib3
import requests
import json
from Common.my_logger import logger
urllib3.disable_warnings()


class HandleRequest:
    def __init__(self, cookie=None):
        # self.requests = requests.Session()
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        if cookie is None:
            self.headers['Cookie'] = 'wexShop=04519E29DD49FD91D945BF84C9EAB020; ' \
                                     'sysType=1; ' \
                                     '_wex_captcha=f71aebd1f4d943dd954d741d1cc905e7'

    def Request(self, url, data=None, method='POST'):
        """

        :param url: 请求地址
        :param data: 字典形式的数据
        :param method: 请求方式
        :return:
        """
        logger.info("发起一次HTTP请求")
        logger.info("请求头为：{}".format(self.headers))
        logger.info("请求方法为：{}".format(method))
        logger.info("请求url为：{}".format(url))
        logger.info("请求数据为：{}".format(data))
        method = method.upper()
        if method == "GET":
            try:
                resp = requests.get(url=url, params=data, headers=self.headers)
                # resp = requests.get(url=_url, params=data, headers=self.headers)
                # response = json.loads(r.text)
                response = json.dumps(json.loads(resp.text), indent=4, sort_keys=False,
                                      ensure_ascii=False)
                # print("get请求结果为：\n %s" % response)
            except BaseException as e:
                print("get请求错误，错误原因：%s" % e)
        elif method == "POST":
            """变成双引号"""
            # data = json.dumps(data)
            try:
                resp = requests.post(url=url, data=data, headers=self.headers)
                # response = json.loads(r.text)
                response = json.dumps(json.loads(resp.text), indent=4, sort_keys=False, ensure_ascii=False)
                # print("post请求结果为：\n %s" % response)
            except BaseException as e:
                print("post请求错误，错误原因：%s" % e)
        else:
            resp = None
            print(f"暂不支持{method}方法")
        # self.TEXT.set_map('text', response)
        logger.info("相应状态码为：{}".format(resp.status_code))
        logger.info("响应数据为：{}".format(resp.json()))
        return resp


if __name__ == '__main__':
    a = HandleRequest()
    r = a.Request(url='http://116.63.143.113:8082/his/patient/getPatientData')
    # A = HandleRequest(cookie=1)
    # a = A.Request(url='http://116.63.143.113:8082/his/patient/getPatientData')








