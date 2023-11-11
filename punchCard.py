import json
import random
import time
import requests
import pushMessage
import sha256Encode


def clockIn(user, uid, token):
    longitude = round(float(user["longitude"]) + random.uniform(-0.00005, 0.00005), 6)
    latitude = round(float(user["latitude"]) + random.uniform(-0.00005, 0.00005), 6)
    data = {
        "dtype": 1,
        "uid": uid,
        "address": user["address"],
        "phonetype": user["phone"],
        "probability": 0,
        "longitude": longitude,
        "latitude": latitude
    }
    # Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data, separators=(',', ':')) + token)
    Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data) + token)
    headers = {
        "os": "android",
        "phone": user["deviceModel"],
        "appversion": "59",
        "sign": Sign,
        "timestamp": str(int(time.time() * 1000)),
        "token": token,
        "cl_ip": f"192.168.31.{random.randint(10, 200)}",
        "content-type": "application/json;charset=utf-8",
        "Content-Length": str(len(str(data))),
        "accept-encoding": "gzip, deflate",
        "user-agent": "okhttp/3.14.9"
    }
    # print(Sign, user["phone"], token)
    url = 'https://sxbaapp.zcj.jyt.henan.gov.cn/api/clockindaily20221202.ashx'
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        data = response.json()
        if (data["code"] == 1001):
            print(f'{user["remark"]} 打卡成功')
            return True, data
        else:
            print(f'打卡状态失败{data["code"]} 错误代码{data["msg"]}')
            pushMessage.pushMessage('职校家园打卡失败',
                                    f'打卡账户 {user["remark"]} 打卡状态代码{data["code"]} 错误信息{data["msg"]}',
                                    user["pushKey"])
            return False, f'打卡账户 {user["remark"]} 打卡状态代码{data["code"]} 错误信息{data["msg"]}'
    except requests.exceptions.RequestException as error:
        pushMessage.pushMessage('职校家园打卡失败', f"发生请求异常：{error} 请求打卡异常", user["pushKey"])
        return False, f"发生请求异常：{error} 请求登录异常"
