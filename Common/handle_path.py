"""
============================
Author: 潘师傅
Time: 2021/8/1 12:18
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""

import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

# 测试用例路径
cases_dir = os.path.join(base_dir, "TestCases")
# print(cases_dir)
# 测试数据路径
datas_dir = os.path.join(base_dir, "TestTatas")
# print(datas_dir)
# 测试报告路径
reports_dir = os.path.join(base_dir, "Outputs\\reports")
# print(reports_dir)
# 日志路径
logs_dir = os.path.join(base_dir, "Outputs\\logs")
# print(logs_dir)
# 配置文件路径
conf_dir = os.path.join(base_dir, "Conf")
# print(conf_dir)


