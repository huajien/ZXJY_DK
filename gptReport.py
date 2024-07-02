# 来源openai接口来源 https://github.com/chatanywhere/GPT_API_free/blob/main/demo.py
import openai
import os
import json
import random
import time
import requests
import pushMessage
import sha256Encode
import main


def gpt_35_api_stream(messages: list):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            stream=False,
        )
        # print(response['choices'][0]['message']['content'])
        return response.choices[0].message.content
    except Exception as err:
        return {'error': f'OpenAI API 异常: {err}'}


def getJobTitle(user, uid, token):
    data = {
        "dtype": "1",
        "uid": uid
    }
    # Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data, separators=(',', ':')) + token)
    Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data) + token)
    headers = {
        "os": "android",
        "phone": user["deviceModel"],
        "appversion": "65",
        "sign": Sign,
        "timestamp": str(int(time.time() * 1000)),
        "token": token,
        "cl_ip": f"192.168.31.{random.randint(10, 200)}",
        "content-type": "application/json;charset=utf-8",
        "Content-Length": str(len(str(data))),
        "accept-encoding": "gzip, deflate",
        "user-agent": "okhttp/3.14.9"
    }
    url = "https://sxbaapp.dxtxl.com/api/shixi_student_check.ashx"
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        data = response.json()
        try:
            jobTitle = data['data']['bmlist'][0]['gwName']
            workingState = data['data']['bmlist'][0]['bmstatus']
            if workingState == "正在实习":
                print(f"当前状态是{workingState}")
                return True, jobTitle
            else:
                print(f"你没有实习中")
                pushMessage.pushMessage("职校家园提醒", f"你没有实习或者未开始", user["pushKey"])
                return False, f"你没有在实习中"
        except KeyError as error:
            print(f"找不到{error}键对应数据")
    except requests.exceptions.RequestException as error:
        return f"找不到{error}键对应数据"


def loadUserFiles():
    path = os.path.join(os.getcwd(), "aiReport.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    else:
        localPath = os.listdir(os.getcwd())
        print(f"\033[93m无法找到 {path} 文件，\n请先执行addUser.py：\n{localPath}\033[0m")
        return False


def gptConfig(reportType, jobTitleReturnData):
    apt_key = loadUserFiles()
    if apt_key:
        api_key = apt_key[0]['api_key']
        openai.api_key = api_key
        openai.api_base = "https://api.chatanywhere.com.cn/v1"
        ReturnGptData = gpt_35_api_stream(
            [
                {
                    'role': 'user',
                    'content': f'我是一个正在实习的学生，我的岗位是{jobTitleReturnData}'
                },
                {
                    'role': 'user',
                    'content': f'帮我写一份{jobTitleReturnData}岗位实习{reportType}，内容大概 60 字左右，要求包含：1、实习项目；2、实习记录；3、实习总结。不要出现比如“XXX项目”、“A项目”之类的，你的回答只需要以 JSON 格式返回给我。'
                }
            ]
        )
        time.sleep(int(random.uniform(15, 30)))
        return ReturnGptData


if __name__ == '__main__':
    main.main()
