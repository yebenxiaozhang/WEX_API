"""
============================
Author: 潘师傅
Time: 2021/8/2 15:24
Project: wex_api
Company: 厦门微尔笑网络科技有限公司
============================
"""
import random
import time
from Common.HendleDB import HandleDB
from Common.HandleRequests import send_requests


def __get_phone():
    phone_prefix = [
        133, 149, 153, 173, 177, 180, 181, 189, 199, 130, 131, 132, 145, 155, 156, 166, 171, 175,
        176, 185, 186, 166, 134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172,
        178, 182, 183, 184, 187, 188, 198]
    new_phone = str(phone_prefix[random.randint(0, len(phone_prefix) - 1)]) + str(int(time.time()))[2:10]
    return new_phone


def __unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def __gbk2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    val1 = bytes.fromhex(val).decode('gb2312')
    return val1


def __get_name():
    surname = [
        "赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩",
        "杨", "朱", "秦", "尤", "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏",
        "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水", "窦", "章", "云", "苏", "潘", "葛", "奚",
        "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳",
        "酆", "鲍", "史", "唐", "费", "廉", "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗",
        "毕", "郝", "邬", "安", "常", "乐", "于", "时", "傅", "皮", "卞", "齐", "康", "伍", "余",
        "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹", "姚", "邵", "湛", "汪", "祁",
        "毛", "禹", "狄", "米", "贝", "明", "臧", "计", "伏", "成", "戴", "谈", "宋", "茅", "庞",
    ]
    new_name = random.choice(surname) + __unicode() + __gbk2312()
    return new_name


def new_patient():
    return __get_name(), __get_phone()


if __name__ == '__main__':
    pass
    new_patient()
    xm, phone = new_patient()
    # print(new_patient())
    print(xm, phone)
    # a = GetNewPatient()
    # a.GetName()
    # print(GetNewPatient.GBK2312())
    # print(a.GetPhone())
    # # print(a.GBK2312() + a.Unicode())
    # # print(a.Unicode())
    # print(a.GetName)
    # # a.GetPhone()
    # import random
    #
    # first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
    # second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文",
    #                "明浩", "光", "超", "军", "达"]
    #
    # print(random.choice(first_name))
    # print(random.choice(first_name))
    # name = random.choice(first_name) + random.choice(second_name)
    # print(name)

#
# def get_new_phone():
#     db = HandleDB()
#     while True:
#         # 1生成
#         phone = __generator_phone()
#         # 2校验，有
#         count = db.get_count('select * from member where mobile_phone="{}"'.format(phone))
#         if count == 0:  # 如果手机号码没有在数据库查到。表示是未注册的号码。
#             db.close()
#             return phone
#
#
# def get_old_phone():
#     """
#     从配置文件获取指定的用户名和密码
#     确保此帐号，在系统当中是注册了的。
#     返回：用户名和密码。
#     """
#     from Common.handle_config import conf
#     user = conf.get("general_user", "user")
#     passwd = conf.get("general_user", "passwd")
#     # 如果数据库查找到user，就直接返回。如果没有，则调用注册接口注册一个。
#     # 不管注册与否，直接调用注册接口。
#     send_requests("POST", "member/register", {"mobile_phone": user, "pwd": passwd})
#     return user, passwd
#
#
# def __generator_phone():
#     index = random.randint(0, len(prefix) - 1)
#     phone = str(prefix[index])  # 前3位
#     for _ in range(0, 8):  # 生成后8位
#         phone += str(random.randint(0, 9))
#     return phone
#
# print(get_new_phone())
