import pushMessage
import sha256Encode
import json
import random
import gptReport
import time
import datetime
import main
import requests
import re
def header(user,token,Sign,data):
    return {
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

def sendReportData(user,RreportData,headers,data):
    url = "https://sxbaapp.dxtxl.com/api/ReportHandler.ashx"
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        data = response.json()
        if (data["code"] == 1001):
            print(f'{user["remark"]} 报告填写完成')
            pushMessage.pushMessage('职校家园报告填写完成',
                                    f"报告项目{RreportData['实习项目']} "
                                    f"实习记录内容{RreportData['实习记录']} "
                                    f"实习总结内容{RreportData['实习总结']}",
                                    user["pushKey"])
        else:
            print(f'报告状态失败{data["code"]} 错误代码{data["msg"]}')
            pushMessage.pushMessage('职校家园报告失败',
                                    f'报告账户 {user["remark"]} 报告状态代码{data["code"]} 错误信息{data["msg"]}',
                                    user["pushKey"])
            return False
    except requests.exceptions.RequestException as error:
        pushMessage.pushMessage('职校家园报告失败',
                                f"发生请求异常：{error} 请求报告异常",
                                user["pushKey"])
        return False



def report(user,uid,token):
    print(f"用户{user['remark']} 开启日报")
    currentDate = datetime.date.today()
    isLastDayOfMonth = (currentDate + datetime.timedelta(days=1)).month != currentDate.month

    jobTitleState, jobTitleReturnData = gptReport.getJobTitle(user, uid, token)
    if jobTitleState:
        # ----------------------------日报
        retry_count = 1
        while retry_count <= 10:
            dailyRreportContent = gptReport.gptConfig(jobTitleReturnData,"日报")
            try:
                pattern = r'\{([^{}]+)\}'
                match = re.search(pattern, dailyRreportContent, re.DOTALL)

                if match:
                    formatData = '{' + match.group(1) + '}'
                    RreportData = json.loads(formatData)
                if RreportData['实习项目'] and RreportData['实习记录'] and \
                        RreportData['实习总结']:
                    print(f"日报信息gpt已完成准备填写日报")
                    data = {
                        "uid": uid,
                        "starttime": time.strftime("%Y-%m-%d"),
                        "project": RreportData['实习项目'],
                        "address": user['address'],
                        "record": RreportData['实习记录'],
                        "summary": RreportData['实习总结'],
                        "dtype": "1",
                    }
                    Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data) + token)
                    headers = header(user,token,Sign,data)
                    sendReportData(user,RreportData,headers,data)
                    break
            except KeyError as error:
                print(f"ChatGPT中缺少键: {error}第{retry_count}重试")
                retry_count += 1
            except Exception as error:
                print(f"日报发生错误异常未找到第{retry_count}重试：{error}")
                retry_count += 1
            except json.JSONDecodeError as error:
                print(f"ChatGPT JSON中解析错误: {error}")
                retry_count += 1
            if retry_count == 10:
                print(f"日报填写失败，尝试第{retry_count}重试")
                pushMessage.pushMessage('职校家园日报失败',
                f"日报填写失败，请联系管理员重新填写日报，尝试第{retry_count}重试",user["pushKey"])
                break
        # ----------------------------周报
        if datetime.datetime.now().weekday() == 4:
            print(f"用户{user['remark']} 开启周报")
            retry_count = 1
            while retry_count <= 10:
                    weeklyRreportContent = gptReport.gptConfig(jobTitleReturnData,"周报")
                    try:
                        pattern = r'\{([^{}]+)\}'
                        match = re.search(pattern, weeklyRreportContent, re.DOTALL)
                        if match:
                            formatData = '{' + match.group(1) + '}'
                            RreportData = json.loads(formatData)

                        if RreportData['实习项目'] and RreportData['实习记录'] and \
                                RreportData['实习总结']:
                            print(f"周报信息gpt已完成")
                            data = {
                                "uid": uid,
                                "starttime": (datetime.date.today() - datetime.timedelta(
                                    days=6)).strftime('%Y-%m-%d'),
                                "project": RreportData['实习项目'],
                                "address": user['address'],
                                "record": RreportData['实习记录'],
                                "summary": RreportData['实习总结'],
                                "dtype": "2",
                                "stype": "2",
                                "endtime": time.strftime("%Y-%m-%d")
                            }
                        Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data) + token)
                        headers = header(user, token, Sign, data)
                        sendReportData(user, RreportData, headers, data)
                        break
                    except KeyError as error:
                        print(f"ChatGPT中缺少键: {error}第{retry_count}重试")
                        retry_count += 1
                    except Exception as error:
                        print(f"周报发生错误异常未找到第{retry_count}重试：{error}")
                        retry_count += 1
                    except json.JSONDecodeError as error:
                        print(f"ChatGPT JSON中解析错误: {error}")
                        retry_count += 1
                    if retry_count == 10:
                        print(f"周报填写失败，尝试第{retry_count}重试")
                        pushMessage.pushMessage('职校家园周报失败',
                        f"周报填写失败，请联系管理员重新填写周报，尝试第{retry_count}重试",user["pushKey"])
                        break
        # ---------------------------- 月报
        if isLastDayOfMonth:
            print(f"用户{user['remark']} 开启月报")
            retry_count = 1
            while retry_count <= 10:
                monthlyRreportContent = gptReport.gptConfig(jobTitleReturnData,"月报")
                try:
                    pattern = r'\{([^{}]+)\}'
                    match = re.search(pattern, monthlyRreportContent, re.DOTALL)

                    if match:
                        formatData = '{' + match.group(1) + '}'
                        RreportData = json.loads(formatData)
                    if RreportData['实习项目'] and RreportData['实习记录'] and RreportData['实习总结']:

                        print(f"月报信息gpt已完成")
                        data = {
                            "uid": uid,
                            "starttime": (datetime.date.today() - datetime.timedelta(
                                days=31)).strftime('%Y-%m-%d'),
                            "project": RreportData['实习项目'],
                            "address": user['address'],
                            "record": RreportData['实习记录'],
                            "summary": RreportData['实习总结'],
                            "dtype": "2",
                            "stype": "3",
                            "endtime": time.strftime("%Y-%m-%d")
                        }
                        Sign = sha256Encode.encodeSha256('Anything_2023', json.dumps(data) + token)
                        headers = header(user, token, Sign, data)
                        sendReportData(user, RreportData, headers, data)
                        break
                except KeyError as error:
                    print(f"ChatGPT中缺少键: {error}第{retry_count}重试")
                    retry_count += 1
                except Exception as error:
                    print(f"日报发生错误异常未找到第{retry_count}重试：{error}")
                    retry_count += 1
                except json.JSONDecodeError as error:
                    print(f"ChatGPT JSON中解析错误: {error}")
                    retry_count += 1
                if retry_count == 10:
                    print(f"月报填写失败，尝试第{retry_count}重试")
                    pushMessage.pushMessage('职校家园月报失败',
                    f"月报填写失败，请联系管理员重新填写月报，尝试第{retry_count}重试",user["pushKey"])
                    break
if __name__ == '__main__':
    main.main()