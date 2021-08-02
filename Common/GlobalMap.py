"""
============================
Author: 潘师傅
Time: 2021/8/2 13:52
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import json
import logging


class GlobalMap:
    # 拼装成字典构造全局变量  借鉴map  包含变量的增删改查
    map = {}

    def set_map(self, key, value):

        if isinstance(value, dict):
            value = json.dumps(value)
        self.map[key] = value

    def set(self, **keys):
        try:
            for key_, value_ in keys.items():
                self.map[key_] = str(value_)
                logging.debug(key_ + ":" + str(value_))
        except BaseException as msg:
            logging.error(msg)
            raise msg

    def del_map(self, key):
        try:
            del self.map[key]
            return self.map
        except KeyError:
            logging.error("key:'" + str(key) + "'  不存在")

    def get(self, *args):
        try:
            dic = {}
            for key in args:
                if len(args) == 1:
                    dic = self.map[key]
                    logging.debug(key + ":" + str(dic))
                elif len(args) == 1 and args[0] == 'all':
                    dic = self.map
                else:
                    dic[key] = self.map[key]
            return dic
        except KeyError:
            logging.warning("key:'" + str(key) + "'  不存在")
            return 'Null_'
