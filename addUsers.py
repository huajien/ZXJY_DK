import json
import os
import random
import re
import string
import time
from urllib.parse import quote

import requests

import pushMessage

path = os.getcwd() + os.sep


def write_user(filename, newdata):
    with open(filename, 'r', encoding='utf-8') as f:
        olddata = f.read()
    olddata = json.loads(olddata)
    olddata.extend(newdata)
    with open(filename, 'w', encoding='utf-8') as write_f:
        write_f.write(json.dumps(olddata, indent=2, ensure_ascii=False))


def obtainCoordinates(address):
    key = "UGMBZ-CINWR-DDRW5-W52AK-D3ENK-ZEBRC"
    response = requests.get(
        f"https://apis.map.qq.com/jsapi?qt=geoc&addr={quote(address, safe='')}&key={key}&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb3.geocoder0",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36",
            "content-type": "application/json;charset=utf-8",
            "accept-encoding": "gzip, deflate",
            "Referer": "https://jingweidu.bmcx.com/"
        })
    return re.search(r'"pointx":"(.*?)"', response.text).group(1), re.search(r'"pointy":"(.*?)"', response.text).group(
        1)


def checkUserData(filename, enabled, remark, phone, password, deviceModel, address, PushPlus_token):
    deviceId = ''.join(random.choice(string.digits + 'abcdef') for _ in range(36))
    longitude, latitude = obtainCoordinates(address)
    newdata = [
        {
            "enabled": enabled,
            "remark": remark,
            "phone": phone,
            "password": password,
            "deviceModel": deviceModel,
            "deviceId": deviceId,
            "address": address,
            "longitude": longitude,
            "latitude": latitude,
            "pushKey": PushPlus_token,
        }
    ]
    write_user(filename=filename, newdata=newdata)


if __name__ == '__main__':
    filename = "userData.json"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    enabled = input("是否开启打卡y or n（默认y）：")
    if enabled == "y" or "Y":
        enabled = True
    elif enabled == "n" or "N":
        enabled = False
    else:
        enabled = True
    name = input("输入例如(张三)：")
    while True:
        pattern = re.compile(r'^1[3-9]\d{9}$')
        phone = input("输入账号(手机号)：")
        if pattern.search(phone):
            break
        else:
            print(f"手机号不正确！")
    # 密码
    while True:
        password = input("请输入密码：")
        password_confirm = input("请再次输入密码进行确认：")
        if password_confirm == password:
            print("密码设置成功！")
            break
        else:
            print(f"两次密码不一致")
    # 手机型号
    print("输入手机型号，例如 Redmi|22011211C|13 \n手机型号|设备号|安卓版本\n")
    deviceModel = input("输入手机型号：\n")
    # 打卡地址
    address = input("输入打卡地址例如 河南省郑州市郑东新区正光路11号:\n")
    # 推送push
    PushPlus_token = input("PushPlus_token: ")
    userdata = checkUserData(filename, enabled, name, phone, password,
                             deviceModel, address,
                             PushPlus_token)
    print(
        f"添加时间 {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 用户信息姓名{name} 手机号{phone} 密码{password} 手机型号{deviceModel} 打卡位置 {address}")
    pushMessage.pushMessage(f"添加{name}用户成功",
                            f"开关{enabled} 别名{name} 手机号 {phone} 密码{password} 设备型号{deviceModel} 打卡位置{address}",PushPlus_token)
