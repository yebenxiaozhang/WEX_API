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
import configparser
from Common.my_logger import logger
from Common.GlobalMap import GlobalMap
urllib3.disable_warnings()

config = configparser.ConfigParser()
config.read("../Conf/wex.ini", encoding="UTF-8")


class HandleRequest:
    def __init__(self):
        self.ShopText = GlobalMap()

    def __handle_header(self, cookie=None):
        """
        处理请求头。加上项目当中必带的请求头。如果有cookie，加上cookie。
        :param cookie: 值
        :return: 处理之后headers字典
        """

        self.ShopText.set_map('cookie', 'wexShop=476935F32313B7EE347AC1EE2657568E; '
                                        '_wex_captcha=fb7b0b3b0cd840639dc3549368288f34; sysType=0')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        if cookie is None:
            headers[
                # 'ticket'] = self.ShopText.get('cookie')
                'cookie'] = self.ShopText.get('cookie')
        return headers

    def __pre_url(self, url):
        """
        拼接接口的url地址
        :param url:
        :return: 拼接接口的url地址
        """

        base_url = config.get("server", "base_url")
        if url.startswith("/"):
            return base_url + url
        else:
            return base_url + "/" + url

    def __pre_data(self, data):
        """
        如果data是字符串，则转换成字典对象
        :param data:
        :return:
        """
        if data is not None and isinstance(data, str):
            # 如果有null，则替换为None
            if data.find("null") != -1:
                data = data.replace("null", "None")
            # 使用eval转成字典.eval过程中，如果表达式有涉及计算，会自动计算。
            data = eval(data)
        return data

    def send_requests(self, url, data, method='POST', cookie=None):
        """

        :param url: 请求地址
        :param data: 字典形式的数据
        :param method: 请求方式
        :param cookie:
        :return:
        """

        logger.info("发起一次HTTP请求")
        # 得到请求头
        headers = self.__handle_header(cookie)
        # 得到完整的url - 拼接url
        url = self.__pre_url(url)
        # 请求数据的处理 - 如果是字符串，则转换成字典对象。
        data = self.__pre_data(data)
        logger.info("请求头为：{}".format(headers))
        logger.info("请求方法为：{}".format(method))
        logger.info("请求url为：{}".format(url))
        logger.info("请求数据为：{}".format(data))
        method = method.upper()
        if method == "GET":
            try:
                resp = requests.get(url=url, params=data, headers=headers)
                # resp = requests.get(url=_url, params=data, headers=self.headers)
                # response = json.loads(r.text)
                # response = json.dumps(json.loads(resp.text), indent=4, sort_keys=False,
                #                       ensure_ascii=False)
                # print("get请求结果为：\n %s" % response)
            except BaseException as e:
                print("get请求错误，错误原因：%s" % e)

        elif method == "POST":
            """变成双引号"""
            # data = json.dumps(data)
            try:
                resp = requests.post(url, data=data, headers=headers)
                # response = json.loads(r.text)
                # response = json.dumps(json.loads(resp.text), indent=4, sort_keys=False, ensure_ascii=False)
                # print("post请求结果为：\n %s" % response)
            except BaseException as e:
                print("post请求错误，错误原因：%s" % e)
        else:
            resp = None
            print(f"暂不支持{method}方法")
        # self.TEXT.set_map('text', response)
        logger.info("相应状态码为：{}".format(resp.status_code))
        # if resp.json():
        #     logger.info("响应数据为：{}".format(resp.json()))
        self.ShopText.set_map('TEXT', resp.text)
        return resp


if __name__ == '__main__':
    A = HandleRequest()
    resp = A.send_requests('/his/patient/getPatientData')
    # print(resp.text)
    # print(resp.status_code)
