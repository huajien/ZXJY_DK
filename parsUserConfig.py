import version

import Login
import apitoken
import punchCard


def LoadUserConfig(user):
    if not user["enable"]:
        print(user['remark'], '未启用打卡，即将跳过')
        return False
    else:
        print('用户' + user['remark'], '已启用，即将打卡')
        state, token = apitoken.get_apitoken()

        if not state:
            print('用户', user['remark'], '获取Token失败', token)
        else:
            # print(version.AppVersion(user["pushKey"]))
            if (version.AppVersion(user["pushKey"]) == 1):
                state, returnData = (Login.login(user, token))
                if state:
                    uid = returnData["data"]["uid"]
                    token = returnData["data"]["UserToken"]
                    # print(uid)
                    state, returnData = punchCard.clockIn(user, uid, token)
                    if not state:
                        print(returnData)
                    else:
                        print(returnData)
                else:
                    print(returnData)
            else:
                print('app版本有变化停止自动打卡请前往\n https://github.com/huajien/ZXJY_DK \n 更新新版本')
