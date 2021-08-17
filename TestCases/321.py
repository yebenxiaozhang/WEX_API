"""
============================
Author: 潘师傅
Time: 2021/8/16 16:44
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import random
import string
import csv
import xlrd
import xlwt
#注意这里的 excel 文件的后缀是 xls 如果是 xlsx 打开是会提示无效,新建excel表格后要选择文本格式保存
all_str = string.ascii_letters + string.digits
excelpath =('D:\\user.xls')  #新建excel文件
workbook = xlwt.Workbook(encoding='utf-8')  #写入excel文件
sheet = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)  #新增一个sheet工作表
headlist=[u'账号',u'密码',u'邮箱']   #写入数据头
row=0
col=0
for head in headlist:
    sheet.write(row,col,head)
    col=col+1
for i in range(1,4):#写入3行数据
    for j in range(1,3):#写入3列数据
        username = 111
        # password = random.randint(100000, 999999) 生成随机数
        password = 222
        Email= 333
        sheet.write(i,j-1,username)
        sheet.write(i,j,password)
        sheet.write(i,j+1,Email)
        # sheet.write(i-1, j-1, username)   没有写标题时数据从第一行开始写入
        # sheet.write(i-1, j, password)
    workbook.save(excelpath) #保存
    print(u"生成第[%d]个账号"%(i))