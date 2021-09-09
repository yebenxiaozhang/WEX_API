"""
============================
Author: 潘师傅
Time: 2021/8/2 13:48
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import requests
import configparser

from Common.GlobalMap import GlobalMap
from Common.HandleRequests import HandleRequest

config = configparser.ConfigParser()
config.read("../Conf/wex.ini", encoding="UTF-8")


class ShopApi:

    def __init__(self):
        self.ShopText = GlobalMap()
        self.SendRequests = HandleRequest()

    def GetPatient(self, keyword=None):
        """
        患者资料列表
        :param keyword:  关键字 姓名/电话/档案号
        :return:
        """
        self.SendRequests.send_requests(url='/common/quickSearch',
                                        data={
                                            'd': keyword
                                        })

    def GetTemporaryPatient(self, keyword=None, page=1, rows=15, start=None, end=None):
        """
        临时患者列表
        :param keyword: 关键字  姓名/电话/档案号
        :param page:    第几页
        :param rows:    每页显示的数量
        :param start:   开始时间
        :param end:     结束时间
        :return:
        """
        self.SendRequests.send_requests(url='/his/patient/getTemporaryData',
                                        data={
                                            'search': keyword,
                                            'page': page,
                                            'rows': rows,
                                            'start': start,
                                            'end': end
                                        })

    def AddPatient(self, patientName, phone1, patientNameRemark=None, sex=None, phone1Belong=None, birthday=None,
                   age=None,phone2=None,phone2Belong=None,livingArea=None,workingCircle=None,remark=None, mutual=None,
                   origin=None, channel=None,source=None,profession=None,introducerType=None, introducerId=None,
                   introducer=None, relationship=None, educational=None, guarder=None, nationality=None, nation=None,
                   religion=None, addressArea=None, address=None,qq=None, bloodType=None, marry=None, email=None,
                   socialSecurityNumber=None, socialCardNumber=None, weChat=None, identityCard=None,
                   identityCardType=None, PATIENT_TAG2=None, category1=None, category2=None, bindEmployeeId=None,
                   taxpayer=None, enterprise=None, temperature=None, height=None, weight=None, pulse=None,
                   heartRate=None, bloodPressure=None, breathing=None, ALLERGY_HISTORY=None, PREVIOUS_HISTORY=None,
                   LIFE_HISTORY=None, TREATMENT_HISTORY=None, clearTeeth=None, drinkingHistory=None, rescue=None,
                   lastTreatHospital=None, smokePerDay=None, brushTimesPerDay=None, brushMinPerTime=None,
                   PATIENT_TAG1=None, black=None, fromTemp=None, sexcheckbox=None, blackcheckbox=None
                   ):
        """
        新增患者
        :param patientName:     患者姓名
        :param phone1:          患者电话
        :param patientNameRemark:   患者拼音
        :param sex:             患者性别    女：0 男：1
        :param phone1Belong:    电话归属1   填写ID
        :param birthday:        生日  2021-08-05
        :param age:             年龄
        :param phone2:          患者电话2
        :param phone2Belong:    患者电话归属2 填写ID
        :param livingArea:      填写ID
        :param workingCircle:   填写ID
        :param remark:          备注信息
        :param mutual:          0
        :param origin:          填写ID
        :param channel:         填写ID
        :param source:          填写ID
        :param profession:      填写ID
        :param introducerType:  32
        :param introducerId:    填写ID
        :param introducer:      人员名称？
        :param relationship:    填写ID
        :param educational:     填写ID
        :param guarder:         监护人？
        :param nationality:     未知？
        :param nation:          填写ID
        :param religion:        填写ID
        :param addressArea:     填写ID
        :param address:         详细地址
        :param qq:              QQ号码
        :param bloodType:       52？
        :param marry:           40？
        :param email:           电子邮箱
        :param socialSecurityNumber:    社会保险号
        :param socialCardNumber:        社保卡号
        :param weChat:          微信
        :param identityCard:    证件号码
        :param identityCardType:        证件类型
        :param PATIENT_TAG2:    填写ID
        :param category1:       填写ID
        :param category2:       填写ID
        :param bindEmployeeId:          填写ID
        :param taxpayer:        纳税人识别码
        :param enterprise:      刷牙次数
        :param temperature:     体温
        :param height:          身高  cm
        :param weight:          体重  kg
        :param pulse:           脉搏  次/分
        :param heartRate:       心率  次/分
        :param bloodPressure:   血压  mmHg
        :param breathing:       呼吸  次/分
        :param ALLERGY_HISTORY:     填写ID
        :param PREVIOUS_HISTORY:    填写ID
        :param LIFE_HISTORY:        填写ID
        :param TREATMENT_HISTORY:   填写ID
        :param clearTeeth:      洁牙史
        :param drinkingHistory:     填写ID
        :param rescue:          抢救史
        :param lastTreatHospital:   上次就诊医院
        :param smokePerDay:     吸烟
        :param brushTimesPerDay:    刷牙 N次/天
        :param brushMinPerTime:     每次刷牙分钟数
        :param PATIENT_TAG1:        填写ID
        :param black:           0？
        :param fromTemp:           0？
        :param sexcheckbox:           0？
        :param blackcheckbox:           0？
        :return:
        """
        self.SendRequests.send_requests(url='/his/patient/patientAdd',
                                        data={
                                            'patientName': patientName,
                                            'patientNameRemark': patientNameRemark,
                                            'sex': sex,
                                            'phone1': phone1,
                                            'phone1Belong': phone1Belong,
                                            'birthday': birthday,
                                            'age': age,
                                            'phone2': phone2,
                                            'phone2Belong': phone2Belong,
                                            'livingArea': livingArea,
                                            'workingCircle': workingCircle,
                                            'remark': remark,
                                            'mutual': mutual,
                                            'origin': origin,
                                            'channel': channel,
                                            'source': source,
                                            'profession': profession,
                                            'introducerType': introducerType,
                                            'introducerId': introducerId,
                                            'introducer': introducer,
                                            'relationship': relationship,
                                            'educational': educational,
                                            'guarder': guarder,
                                            'nationality': nationality,
                                            'nation': nation,
                                            'religion': religion,
                                            'addressArea': addressArea,
                                            'address': address,
                                            'qq': qq,
                                            'bloodType': bloodType,
                                            'marry': marry,
                                            'email': email,
                                            'socialSecurityNumber': socialSecurityNumber,
                                            'socialCardNumber': socialCardNumber,
                                            'weChat': weChat,
                                            'identityCard': identityCard,
                                            'identityCardType': identityCardType,
                                            'PATIENT_TAG2': PATIENT_TAG2,
                                            'category1': category1,
                                            'category2': category2,
                                            'bindEmployeeId': bindEmployeeId,
                                            'taxpayer': taxpayer,
                                            'enterprise': enterprise,
                                            'temperature': temperature,
                                            'height': height,
                                            'weight': weight,
                                            'pulse': pulse,
                                            'heartRate': heartRate,
                                            'bloodPressure': bloodPressure,
                                            'breathing': breathing,
                                            'ALLERGY_HISTORY': ALLERGY_HISTORY,
                                            'PREVIOUS_HISTORY': PREVIOUS_HISTORY,
                                            'LIFE_HISTORY': LIFE_HISTORY,
                                            'TREATMENT_HISTORY': TREATMENT_HISTORY,
                                            'clearTeeth': clearTeeth,
                                            'drinkingHistory': drinkingHistory,
                                            'rescue': rescue,
                                            'lastTreatHospital': lastTreatHospital,
                                            'smokePerDay': smokePerDay,
                                            'brushTimesPerDay': brushTimesPerDay,
                                            'brushMinPerTime': brushMinPerTime,
                                            'PATIENT_TAG1': PATIENT_TAG1,
                                            'black': black,
                                            'fromTemp': fromTemp,
                                            'sexcheckbox': sexcheckbox,
                                            'blackcheckbox': blackcheckbox,


                                        })

    def GetPatientData(self, keyword=None, page=1, rows=15):
        """
        患者列表
        :param keyword:     关键字  姓名/电话/档案号
        :param page:        第几页
        :param rows:        每页显示条数
        :return:
        """
        self.SendRequests.send_requests(url='/his/patient/getPatientData',
                                        data={
                                            'search': keyword,
                                            'page': page,
                                            'rows': rows

                                        })

    def GetMyAllPatientData(self, openType, startTime=None, endTime=None, page=1, rows=15):
        """
        获取我的客户
        :param openType: *必填 医生：doctor  咨询： consult 营销：market   护士：nurse
        :param startTime:   开始时间
        :param endTime:     结束时间
        :param page:        第几页
        :param rows:        每页显示条数
        :return:
        """
        self.SendRequests.send_requests(url='/his/frontWorkstation/getMyAllPatientData',
                                        data={
                                            'start': startTime,
                                            'end': endTime,
                                            'openType': openType,
                                            'page': page,
                                            'rows': rows
                                        })

    def GetBookingData(self, keyword=None, startTime=None, endTime=None, page=1, rows=15):
        """
        预约列表
        :param keyword:     关键字  姓名/电话/档案号
        :param startTime:   开始时间
        :param endTime:     结束时间
        :param page:        第几页
        :param rows:        每页显示条数
        :return:
        """
        self.SendRequests.send_requests(url='/his/booking/getBookingData',
                                        data={
                                            'start': startTime,
                                            'end': endTime,
                                            'page': page,
                                            'rows': rows,
                                            'search': keyword
                                        })

    def GetSelect(self, dictType):
        """
        获取各种小标签
        :param dictType:
        患者印象： PATIENT_TAG2    过敏史：ALLERGY_HISTORY     既往史：PREVIOUS_HISTORY
        生活史： LIFE_HISTORY   治疗史：TREATMENT_HISTORY   电话归属：PHONE_BELONG   来源/渠道：SOURCE
        职业： PROFESSION      介绍人类型：introducerType    介绍人关系：RELATIONSHIP  学历：EDUCATIONAL
        国籍：NATIONALITY  民族：NATION      宗教价值观：religion   血型：bloodType    婚姻状况：marry
        证件类型：IDENTITYCARD_TYPE  患者分类1：CATEGORY1     患者分类2：CATEGORY2     洁牙史：ClearTeeth
        饮酒史：MOUTH_wine      抢救史：RESCUE_HISTORY      上次就诊医院：RESCUE_HISTORY   患者标签：PATIENT_TAG1
        生活小区：LIVING_AREA    工作商圈：WORKING_CIRCLE     来源：origin   客户渠道：CHANNEL    客户地址：ADDRESS_AREA
        客户渠道：ADDRESS_AREA
        :return:
        """
        self.SendRequests.send_requests(url='/common/getSelect',
                                        data={
                                            'dictType': dictType
                                        })

    def SendSmsCode(self, user):
        """
        获取验证码
        :param user: 账号
        :return:
        """
        self.SendRequests.send_requests(url='/shop/login/sendSmsCode',
                                        data={
                                            'uName': user
                                        })

    def GetSQL(self):
        """

        :return: 获取SQL
        """
        self.SendRequests.send_requests(url='/druid/sql.json?orderBy=TotalTime&orderType=asc&page=1&perPageCount=10000',
                                        data={
                                            'orderBy': 'MaxTimespan',
                                            'orderType': 'asc',
                                            'page': 1,
                                            'perPageCount': 5
                                        })

    def GetCookie(self, uName, password, shopName):
        """
        一键获取COOKIE
        :param uName: 账号
        :param password: 密码
        :param shopName: 门店名称（非ID）
        :return:
        """
        self.SendRequests.send_requests(url='/demo/getLoginTicket',
                                        data={
                                            'uName': uName,
                                            'password': password,
                                            'shopName': shopName
                                        })

    # def PostRequest(self, url, data=None, method='POST', cookie=None):
    #     self.SendRequests.send_requests(self, url, data=data, method=method, cookie=cookie)


if __name__ == '__main__':
    a = ShopApi()
    # a.GetBookingData()
    # a.SendSmsCode(user=13062200304)
    import time
    while 1 != 0:
        # a = ShopApi()
        # time.sleep(50)
        a.SendSmsCode(user=13062200304)


