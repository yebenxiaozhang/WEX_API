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
from Common.HandleRequests import HandleRequest


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
    print(xm, phone)
