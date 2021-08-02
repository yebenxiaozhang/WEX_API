"""
======================
Author: 柠檬班-小简
Time: 2020/6/29 21:12
Project: py30-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""

import requests
import json

from Common.my_logger import logger
from Common.handle_config import conf


#
def send_requests(method, url, data=None, cookie=None):
    """

    :param method:
    :param url:
    :param data:字典形式的数据。
    :param cookie:
    :return:
    """
    logger.info("发起一次HTTP请求")
    # 得到请求头
    headers = __handle_header(cookie)
    # 得到完整的url - 拼接url
    url = __pre_url(url)
    # 请求数据的处理 - 如果是字符串，则转换成字典对象。
    data = __pre_data(data)
    # 将请求数据转换成字典对象。
    logger.info("请求头为：{}".format(headers))
    logger.info("请求方法为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(data))
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理
    if method == "GET":
        resp = requests.get(url, data, headers=headers)
    else:
        resp = requests.post(url, json=data, headers=headers)
    logger.info("响应状态码为：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.json()))
    return resp


def __handle_header(cookie=None):
    """
    处理请求头。加上项目当中必带的请求头。如果有token，加上token。
    :param cookie: token值
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
    base_url = conf.get("server", "base_url")
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


if __name__ == '__main__':
    login_url = "http://116.63.143.113:8082/his/patient/getPatientData"
    login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
    resp = send_requests("POST", login_url, login_datas)
    print(resp.text)
    print(resp.status_code)
