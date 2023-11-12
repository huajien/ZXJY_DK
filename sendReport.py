import pushMessage
import sha256Encode
import json
import random
import gptReport
import time
import datetime
import main
import requests



def report(user,uid,token):
    print(f"用户{user['remark']} 开启日报")
    currentDate = datetime.date.today()
    isLastDayOfMonth = (currentDate + datetime.timedelta(days=1)).month != currentDate.month

    jobTitleState, jobTitleReturnData = gptReport.getJobTitle(user, uid, token)
    if jobTitleState:
        # ----------------------------日报
        retry_count = 0
        while retry_count < 5:
            try:
                dailyRreportContent = gptReport.gptConfig(
                    f"写一个{time.strftime('%Y')}年{time.strftime('%m')}月{time.strftime('%d')}日"
                    f"{jobTitleReturnData}"
                    f"的工作日报只要一小段60字左右返回一段json数据数据中有 实习项目，实习记录，实习总结。三个不要其他的东西")

                dailyDataRreportContent = json.loads(dailyRreportContent)

                if dailyDataRreportContent['实习项目'] and dailyDataRreportContent['实习记录'] and \
                        dailyDataRreportContent['实习总结']:
                    print(f"日报信息gpt已完成准备填写日报")
                    data = {
                        "uid": uid,
                        "starttime": time.strftime("%Y-%m-%d"),
                        "project": dailyDataRreportContent['实习项目'],
                        "address": user['address'],
                        "record": dailyDataRreportContent['实习记录'],
                        "summary": dailyDataRreportContent['实习总结'],
                        "dtype": "1",
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

                    url = "https://sxbaapp.zcj.jyt.henan.gov.cn/api/ReportHandler.ashx"
                    try:
                        response = requests.post(url, headers=headers, data=json.dumps(data))
                        response.raise_for_status()
                        data = response.json()
                        if (data["code"] == 1001):
                            print(f'{user["remark"]} 日报填写完成')
                            pushMessage.pushMessage('职校家园日报填写完成',
                                                    f"日报项目{dailyDataRreportContent['实习项目']} "
                                                    f"实习记录内容{dailyDataRreportContent['实习记录']} "
                                                    f"实习总结内容{dailyDataRreportContent['实习总结']}",
                                                    user["pushKey"])
                        else:
                            print(f'日报状态失败{data["code"]} 错误代码{data["msg"]}')
                            pushMessage.pushMessage('职校家园日报失败',
                                                    f'日报账户 {user["remark"]} 日报状态代码{data["code"]} 错误信息{data["msg"]}',
                                                    user["pushKey"])
                            return False, f'日报账户 {user["remark"]} 日报状态代码{data["code"]} 错误信息{data["msg"]}'
                    except requests.exceptions.RequestException as error:
                        pushMessage.pushMessage('职校家园日报失败',
                                                f"发生请求异常：{error} 请求日报异常",
                                                user["pushKey"])
                        return False, f"发生请求异常：{error} 请求日报异常"
                    break
                else:
                    retry_count += 1
            except Exception as error:
                print(f"未找到 Error: {error}")
                retry_count += 1

        # ----------------------------周报
        if datetime.datetime.now().weekday() == 6:
            print(f"用户{user['remark']} 开启周报")
            retry_count = 0
            while retry_count < 5:
                try:
                    weeklyRreportContent = gptReport.gptConfig(
                        f"写一个{time.strftime('%Y')}年{time.strftime('%m')}月{time.strftime('%d')}每周"
                        f"{jobTitleReturnData}的工作周报只要一小段60字左右返回一段json数据数据中有 实习项目，实习记录，实习总结。三个不要其他的东西")
                    weekDataRreportContent = json.loads(weeklyRreportContent)
                    if weekDataRreportContent['实习项目'] and weekDataRreportContent['实习记录'] and \
                            weekDataRreportContent['实习总结']:
                        print(f"周报信息gpt已完成")
                        data = {
                            "uid": uid,
                            "starttime": (datetime.date.today() - datetime.timedelta(
                                days=7)).strftime('%Y-%m-%d'),
                            "project": weekDataRreportContent['实习项目'],
                            "address": user['address'],
                            "record": weekDataRreportContent['实习记录'],
                            "summary": weekDataRreportContent['实习总结'],
                            "dtype": "2",
                            "stype": "2",
                            "endtime": time.strftime("%Y-%m-%d")

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

                        try:
                            response = requests.post(url, headers=headers, data=json.dumps(data))
                            response.raise_for_status()
                            data = response.json()
                            if (data["code"] == 1001):
                                print(f'{user["remark"]} 周报填写完成')
                                pushMessage.pushMessage('职校家园周报填写完成',
                                                        f"周报项目{weekDataRreportContent['实习项目']} "
                                                        f"实习记录内容{weekDataRreportContent['实习记录']} "
                                                        f"实习总结内容{weekDataRreportContent['实习总结']}",
                                                        user["pushKey"])
                            else:
                                print(f'周报状态失败{data["code"]} 错误代码{data["msg"]}')
                                pushMessage.pushMessage('职校家园周报失败',
                                                        f'周报账户 {user["remark"]} 周报状态代码{data["code"]} 错误信息{data["msg"]}',
                                                        user["pushKey"])
                                return False, f'周报账户 {user["remark"]} 周报状态代码{data["code"]} 错误信息{data["msg"]}'
                        except requests.exceptions.RequestException as error:
                            pushMessage.pushMessage('职校家园周报失败',
                                                    f"发生请求异常：{error} 请求周报异常",
                                                    user["pushKey"])
                            return False, f"发生请求异常：{error} 请求周报异常"
                        break
                    else:
                        retry_count += 1
                except Exception as error:
                    print(f"未找到 Error: {error}")
                    retry_count += 1
        # ---------------------------- 月报
        if isLastDayOfMonth:
            print(f"用户{user['remark']} 开启月报")
            retry_count = 0
            while retry_count < 5:
                try:
                    monthlyRreportContent = gptReport.gptConfig(
                        f"写一个{time.strftime('%Y')}年{time.strftime('%m')}月{time.strftime('%d')}每周"
                        f"{jobTitleReturnData}的工作月报告只要一小段60字左右返回一段json数据数据中有 实习项目，实习记录，实习总结。三个不要其他的东西")
                    monthlyDataRreportContent = json.loads(monthlyRreportContent)
                    if monthlyDataRreportContent['实习项目'] and monthlyDataRreportContent[
                        '实习记录'] and monthlyDataRreportContent['实习总结']:
                        print(f"月报信息gpt已完成")
                        data = {
                            "uid": uid,
                            "starttime": (datetime.date.today() - datetime.timedelta(
                                days=31)).strftime('%Y-%m-%d'),
                            "project": monthlyDataRreportContent['实习项目'],
                            "address": user['address'],
                            "record": monthlyDataRreportContent['实习记录'],
                            "summary": monthlyDataRreportContent['实习总结'],
                            "dtype": "2",
                            "stype": "3",
                            "endtime": time.strftime("%Y-%m-%d")

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

                        try:
                            response = requests.post(url, headers=headers, data=json.dumps(data))
                            response.raise_for_status()
                            data = response.json()
                            if (data["code"] == 1001):
                                print(f'{user["remark"]} 月报填写完成')
                                pushMessage.pushMessage('职校家园月报填写完成',
                                                        f"月报项目{monthlyDataRreportContent['实习项目']} "
                                                        f"实习记录内容{monthlyDataRreportContent['实习记录']} "
                                                        f"实习总结内容{monthlyDataRreportContent['实习总结']}",
                                                        user["pushKey"])
                            else:
                                print(f'月报状态失败{data["code"]} 错误代码{data["msg"]}')
                                pushMessage.pushMessage('职校家园月报失败',
                                                        f'月报账户 {user["remark"]} 月报状态代码{data["code"]} 错误信息{data["msg"]}',
                                                        user["pushKey"])
                                return False, f'月报账户 {user["remark"]} 月报状态代码{data["code"]} 错误信息{data["msg"]}'
                        except requests.exceptions.RequestException as error:
                            pushMessage.pushMessage('职校家园月失败',
                                                    f"发生请求异常：{error} 请求月报异常",
                                                    user["pushKey"])
                            return False, f"发生请求异常：{error} 请求月报异常"
                        break
                    else:
                        retry_count += 1
                except Exception as error:
                    print(f"未找到 Error: {error}")
                    retry_count += 1
    return True
if __name__ == '__main__':
    main.main()