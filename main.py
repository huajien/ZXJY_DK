import random
import time
import loadUsers
import parsUserConfig
import pushMessage
from inputimeout import inputimeout, TimeoutOccurred
import addUsers


def main(AllUsers):
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
    AllUsers = loadUsers.loadUserFiles()
    if not AllUsers:
        addUsers.main()
    try:
        print('不输入默认60秒自动进行打卡当前用户列表')
        print('是否添加新用户 y or n（默认n执行单次打卡）：')
        addUserChoice = inputimeout(timeout=60).lower()
    except TimeoutOccurred:
        addUserChoice = "n"
    if addUserChoice == "y":
        addUsers.main()
    else:
        main(AllUsers)
