import version
import Login
import apitoken
import punchCard
import time
import main
import sendReport
import random

def LoadUserConfig(user):
    if not user["enabled"]:
        print(user['remark'], '未启用打卡，即将跳过')
    else:
        print('用户' + user['remark'], '已启用，即将打卡')
        delay = int(random.uniform(30, 60))
        # delay = int(1)
        print(f'{user["remark"]} 延时 ' + str(delay) + ' 秒')
        time.sleep(delay)
        print(f'{user["remark"]} 打卡时间 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        getApiState, getApiToken = apitoken.get_apitoken()

        if not getApiState:
            print('用户', user['remark'], '获取Token失败', getApiToken)
        else:
            # print(version.AppVersion(user["pushKey"]))
            if (version.AppVersion(user["pushKey"]) == 1):
                loginState, loginReturnData = Login.login(user, getApiToken)
                if loginState:
                    uid = loginReturnData["data"]["uid"]
                    token = loginReturnData["data"]["UserToken"]
                    punchCard.clockIn(user, uid, token)
            else:
                print('app版本有变化停止自动打卡请前往\n https://github.com/huajien/ZXJY_DK \n 更新新版本')


    if not user["report"]:
        print(user['report'], '未启用日报周报月报，即将跳过')
    else:
        print('用户' + user['remark'], '已启用，即将填写日报周报月报')
        delay = int(random.uniform(10, 30))
        # delay = int(1)
        print(f'{user["remark"]} 延时 ' + str(delay) + ' 秒')
        time.sleep(delay)
        print(f'{user["remark"]} 报告时间 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        getApiState, getApiToken = apitoken.get_apitoken()

        if not getApiState:
            print('用户', user['remark'], '获取Token失败', getApiToken)
        else:
            # print(version.AppVersion(user["pushKey"]))
            if (version.AppVersion(user["pushKey"]) == 1):
                loginState, loginReturnData = (Login.login(user, getApiToken))
                if loginState:
                    uid = loginReturnData["data"]["uid"]
                    token = loginReturnData["data"]["UserToken"]
                    sendReport.report(user, uid, token)
            else:
                print('app版本有变化停止自动打卡请前往\n https://github.com/huajien/ZXJY_DK \n 更新新版本')

if __name__ == '__main__':
    main.main()
