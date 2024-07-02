from bs4 import BeautifulSoup
import requests
import pushMessage
from inputimeout import inputimeout, TimeoutOccurred
import subprocess


def AppVersion(pushKey):
    AdaptedVersion = 'v1.4.9'
    ZxjyVersion = 0.5
    print('正在检查版本...')
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url = "https://www.yuque.com/huaji-kiyl5/kb/br0dfuykwe7ryku3"
    response = requests.get(url, headers=header).content
    description = BeautifulSoup(response, 'html.parser').find('meta', attrs={'name': 'description'})['content']
    result = float(description.split('#')[0].replace(' ', ''))
    if result <= ZxjyVersion:
        url = 'https://app.mi.com/details?id=com.wyl.exam'
        try:
            response = requests.get(url, headers=header)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            version = soup.select('.main .float-left')[1].find('div', {'style': 'float:right;'}).get_text().strip()
            if version == AdaptedVersion:
                return True
            else:
                pushMessage.pushMessage('职校家园版本',
                                        f'此版本适配{AdaptedVersion} 当前版本{version}', pushKey)
                print(f'此版本适配{AdaptedVersion} 当前版本{version}')
                return False, "职校家园版本获取失败"
        except requests.exceptions.RequestException as error:
            pushMessage.pushMessage('职校家园版本',
                                    f'职校家园版本获取错误{error}', pushKey)
            print(f'职校家园版本获取错误{error}')
            return False, f'职校家园版本获取失败{error}'
    else:
        print('app版本有变化停止自动打卡请前往\nhttps://github.com/huajien/ZXJY_DK\n更新新版本')
        try:
            print('不输入默认30秒自动更新')
            print('您确定要将ZXJY_DK更新最新版本吗?(y/n)')
            confirmation = inputimeout(timeout=30).lower()
        except TimeoutOccurred:
            confirmation = "y"
        if confirmation.lower() == 'y':
            # 执行 Git 命令，并捕获标准输出和错误输出
            result = subprocess.run(
                "git fetch --all && git reset --hard origin/master",
                shell=True,
                text=True,
                capture_output=True
            )
            # 检查命令是否成功执行
            if result.returncode == 0:
                print("更新成功。输出:\n", result.stdout)
                return True
            else:
                print("更新失败。错误信息:\n", result.stderr)
        else:
            print("取消更新结束任务")