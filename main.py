import random
import time
import loadUsers
import parsUserConfig
import pushMessage

def main():
    AllUsers = loadUsers.loadUserFiles()
    for user in AllUsers:
        try:
            delay = int(random.uniform(30, 120))
            # delay = int(1)
            print(f'{user["remark"]} 延时 ' + str(delay) + ' 秒')
            time.sleep(delay)
            print(f'{user["remark"]} 打卡时间 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            parsUserConfig.LoadUserConfig(user)
        except Exception as error:
            print('打卡失败' + str(error))
            pushMessage.pushMessage('职校家园打卡失败',
                                    '用户' + user["remark"] + user[
                                        "phone"] + '职校家园打卡失败,' + '具体错误信息：' + str(
                                        error), user["pushKey"])
if __name__ == '__main__':
    main()
