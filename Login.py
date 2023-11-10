import json
import random
import time
from hashlib import md5

import requests

import pushMessage
import sha256Encode


def login(user, token):
    password = (md5(user["password"].encode('utf-8')).hexdigest())
    data = {
        "phone": user["phone"],
        "password": password,
        "dtype": 6,
        # "dToken": user["deviceId"] #请求那边是app那边是0所以改成0
        "dToken": "0"
    }

    Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data) + token)
    headers = {
        "os": "android",
        "phone": user["deviceModel"],
        "appversion": "57",
        "sign": Sign,
        "timestamp": str(int(time.time() * 1000)),
        "token": token,
        "cl_ip": f"192.168.31.{random.randint(10, 200)}",
        "content-type": "application/json;charset=utf-8",
        "Content-Length": str(len(str(data))),
        "accept-encoding": "gzip, deflate",
        "user-agent": "okhttp/3.14.9"
    }
    url = "https://sxbaapp.zcj.jyt.henan.gov.cn/api/relog.ashx"
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        data = response.json()
        if (data["code"] == 1001):
            print(f'登录账户 {user["remark"]} 成功')
            return True, data
        else:
            # print(f'登录状态失败{data["code"]} 错误代码{data["msg"]}')
            pushMessage.pushMessage('职校家园登录失败',
                                    f'登录账户 {user["remark"]} 登录状态代码{data["code"]} 错误代码{data["msg"]}',
                                    user["pushKey"])
            return False, f'登录账户 {user["remark"]} 登录状态代码{data["code"]} 错误代码{data["msg"]}'

    except requests.exceptions.RequestException as error:
        pushMessage.pushMessage('职校家园打卡失败', f"发生请求异常：{error} 请求登录异常", user["pushKey"])
        return False, f"发生请求异常：{error}", "请求登录异常"
