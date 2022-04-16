# i = 1
# j = 1
#
# while j < 10:
#     print(str(i) + 'X' + str(j) + '=' + str(i * j))
#     j = j + 1
#     if j == 10:
#         i = i + 1
#         j = i
#ecoding=utf-8
# import os
# import time
# # 2019/9/8 将大的csv文件拆分多个小的csv文件
#
# def mkSubFile(lines, head, srcName, sub):
#     [des_filename, extname] = os.path.splitext(srcName)
#     filename = des_filename + '_' + str(sub) + extname
#     print('make file: %s' % filename)
#     fout = open(filename, 'w')
#     try:
#         fout.writelines([head])
#         fout.writelines(lines)
#         return sub + 1
#     finally:
#         fout.close()
#
#
# def splitByLineCount(filename, count):
#     fin = open(filename,encoding="utf-8")
#     try:
#         head = fin.readline()
#         buf = []
#         sub = 1
#         for line in fin:
#             buf.append(line)
#             if len(buf) == count:
#                 sub = mkSubFile(buf, head, filename, sub)
#                 buf = []
#         if len(buf) != 0:
#             sub = mkSubFile(buf, head, filename, sub)
#     finally:
#         fin.close()
#
#
# if __name__ == '__main__':
#     begin = time.time()
#     splitByLineCount('csv_file.csv', 5000)#每个小的csv文件存放1000条
#     end = time.time()
#     print('time is %d seconds ' % (end - begin))

import requests

import json

A = requests.post(url='http://192.168.0.222:8082/his/patient/getPatientData',
                  headers={
                      'Cookie': 'wexShop=31ED3E53DF690A066B85365A6D036CF7; _jfinal_captcha=eb2f28d81c6d483ebdf7054586cf1c54; sysType=0; allowViewTableOfDay=0',
                      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
                        },
                  data={
                      'page': 1,
                      'rows': 15
                  }

                  )
print(A.status_code)
# print(A.text)
response = json.dumps(json.loads(A.text), indent=4, sort_keys=False, ensure_ascii=False)
print("post请求结果为：\n %s" % response)
