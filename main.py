import random
import time

import loadUsers
import parsUserConfig
import pushMessage

if __name__ == '__main__':
    AllUsers = loadUsers.loadUserFiles()
    for user in AllUsers:
        try:
            time.sleep(random.uniform(30, 120))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print(f'{user["remark"]} 打卡时间 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            parsUserConfig.LoadUserConfig(user)
        except Exception as error:
            print('打卡失败' + str(error))
            pushMessage.pushMessage('职校家园打卡失败',
                                    '用户' + user["remark"] + user[
                                        "phone"] + '职校家园打卡失败,' + '具体错误信息：' + str(
                                        error), user["pushKey"])
