import json
import os


def loadUserFiles():
    allUsers = ""
    path = os.getcwd() + os.sep + "userData.json"
    if os.path.exists(path):
        print("存在userData.json文件")
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                allUsers = allUsers + line + '\n'
        return json.loads(allUsers)
    else:
        # localPath = os.listdir(os.getcwd())
        print(f"\033[93m无法找到 {path} 文件。\n或者使用 addUser.py 文件添加用户\033[0m")
        return False
