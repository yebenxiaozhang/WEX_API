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

urllib3.disable_warnings()

config = configparser.ConfigParser()
config.read("../Conf/wex.ini", encoding="UTF-8")


def __handle_header(cookie=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有cookie，加上cookie。
    :param  cookie:cookie值
    :return: 处理之后headers字典
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    if cookie is None:
        headers[
            'Cookie'] = 'wexShop=04519E29DD49FD91D945BF84C9EAB020; sysType=1; _wex_captcha=f71aebd1f4d943dd954d741d1cc905e7'
    return headers


def __pre_url(url):
    """
    拼接接口的url地址。
    """
    base_url = config.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url


def __pre_data(data):
    """
    如果data是字符串，则转换成字典对象。
    """
    if data is not None and isinstance(data, str):
        # 如果有null，则替换为None
        if data.find("null") != -1:
            data = data.replace("null", "None")
        # 使用eval转成字典.eval过程中，如果表达式有涉及计算，会自动计算。
        data = eval(data)
    return data


def send_requests(url, data=None, method='POST', cookie=None):
    """
    :param url: 请求地址
    :param data: 字典形式的数据
    :param method: 请求方式
    :return:
    """
    logger.info("发起一次HTTP请求")
    # 得到请求头
    headers = __handle_header(cookie)
    # 得到完整的url - 拼接url
    url = __pre_url(url)
    # 请求数据的处理 - 如果是字符串，则转换成字典对象。
    data = __pre_data(data)
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
            response = json.dumps(json.loads(resp.text), indent=4, sort_keys=False,
                                  ensure_ascii=False)
            # print("get请求结果为：\n %s" % response)
        except BaseException as e:
            print("get请求错误，错误原因：%s" % e)
    elif method == "POST":
        """变成双引号"""
        # data = json.dumps(data)
        try:
            resp = requests.post(url, data=data, headers=headers)
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
    if resp.json():
        logger.info("响应数据为：{}".format(resp.json()))
    return resp


if __name__ == '__main__':
    resp = send_requests('http://116.63.143.113:8082/his/patient/getPatientData')
    print(resp.text)
    print(resp.status_code)

    # A = HandleRequest(cookie=1)
    # a = A.Request(url='http://116.63.143.113:8082/his/patient/getPatientData')
