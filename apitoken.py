import requests
import time
import random
def get_apitoken():
    url = "https://sxbaapp.dxtxl.com/api/getApitoken.ashx"
    headers = {
        "os": "android",
        "appversion": "65",
        "timestamp": str(int(time.time() * 1000)),
        "cl_ip": f"192.168.31.{random.randint(10, 200)}",
        "content-type": "application/json;charset=utf-8",
        "Content-Length": str(0),
        "accept-encoding": "gzip, deflate",
        "user-agent": "okhttp/3.14.9"
    }
    try:
        response = requests.post(url, headers=headers)
        # 检查
        response.raise_for_status()
        data = response.json()

        if data["code"] == 1001:
            return True, data["data"]["apitoken"]
        else:
            return False, "apitoken获取失败" + data["msg"]

    except requests.exceptions.RequestException as error:
        return False, str(error), "请求apitoken异常"
