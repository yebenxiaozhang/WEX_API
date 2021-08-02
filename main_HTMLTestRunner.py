"""
============================
Author: 潘师傅
Time: 2021/8/2 11:50
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import unittest
import os
import time
import configparser

from Common.HTMLTestRunner import HTMLTestRunner
from Common.handle_path import cases_dir, reports_dir
from Common.mail import SendMail

config = configparser.ConfigParser()
config.read("./Conf/wex.ini", encoding="UTF-8")


# 收集用例

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # print(lists)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + "\\" + fn))
    # print("The latest report is:" + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file


if __name__ == '__main__':
    s = unittest.defaultTestLoader.discover(cases_dir)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = reports_dir + '/' + now + '_' + 'result.html'
    description = '环境：' + '\n' + '用例执行情况'
    with open(report_name, "wb") as f:
        runner = HTMLTestRunner(stream=f, title=config.get('EMAIL', 'E_mail_theme'), description=description)
        runner.run(s)
        f.close()

    # 发送邮件
    FS = SendMail(user=config.get('EMAIL', 'E_mail_user'),
                  password=config.get('EMAIL', 'E_mail_password'))
    FS.send_mail(theme=config.get('EMAIL', 'E_mail_theme'),
                 attachments=latest_report(reports_dir),
                 to=config.get('EMAIL', 'E_mail_to'))
