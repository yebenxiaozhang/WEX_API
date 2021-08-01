"""
============================
Author: 潘师傅
Time: 2021/8/1 13:39
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
from configparser import ConfigParser
import os

from Common.handle_path import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(conf_dir, "wex.ini")
conf = HandleConfig(file_path)

# if __name__ == '__main__':
#     conf = HandleConfig("wex.ini")
#     conf.get("log", "name")
