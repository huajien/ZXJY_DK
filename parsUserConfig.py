import version
import pushMessage
import Login
import apitoken
import punchCard
import time

def LoadUserConfig(user):
    if not user["enabled"]:
        print(user['remark'], '未启用打卡，即将跳过')
        return False
    else:
        print('用户' + user['remark'], '已启用，即将打卡')
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
                    # print(uid)
                    state, returnData = punchCard.clockIn(user, uid, token)
                    if not state:
                        print(f"{returnData}{time.strftime('%Y')}年{time.strftime('%m')}月{time.strftime('%d')}日 打卡失败" )
                        pushMessage.pushMessage('职校家园打卡失败提醒',
                                                f"{returnData}{time.strftime('%Y')}年{time.strftime('%m')}月{time.strftime('%d')}日 打卡失败",
                                                user["pushKey"])
                    else:
                        print(f"{returnData}打卡成功")
                        pushMessage.pushMessage('职校家园打卡成功提醒',
                                                f"职校家园 {user['remark']} {time.strftime('%Y')}年{time.strftime('%m')}月{time.strftime('%d')}日 {user['remark']} ",
                                                user["pushKey"])
                else:
                    print(f'职校家园 {user["remark"]} {loginReturnData}')
                    pushMessage.pushMessage('职校家园登录失败提醒',
                                            f'职校家园 {user["remark"]} {loginReturnData}',
                                            user["pushKey"])
            else:
                print('app版本有变化停止自动打卡请前往\n https://github.com/huajien/ZXJY_DK \n 更新新版本')