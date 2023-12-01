import loadUsers
import parsUserConfig
from inputimeout import inputimeout, TimeoutOccurred
import addUsers


def winmain(AllUsers):
    for user in AllUsers:
            parsUserConfig.LoadUserConfig(user)


def main():
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
        AllUsers = loadUsers.loadUserFiles()
        winmain(AllUsers)

if __name__ == '__main__':
    main()
