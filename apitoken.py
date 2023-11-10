import requests


def get_apitoken():
    url = "https://sxbaapp.zcj.jyt.henan.gov.cn/api/getApitoken.ashx"
    headers = {
        'content-type': 'application/json;charset=UTF-8',
        'os': 'android',
        # ‘appversion’: ''
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
