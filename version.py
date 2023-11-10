from bs4 import BeautifulSoup
import requests
import pushMessage

def AppVersion(pushKey):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url = 'https://app.mi.com/details?id=com.wyl.exam'
    try:
        response = requests.get(url, headers=header)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        version = soup.select('.main .float-left')[1].find('div', {'style': 'float:right;'}).get_text().strip()
        if version == 'v1.3.9':
            return True
        else:
            pushMessage.pushMessage('职校家园版本',
                                    f'此版本适配v1.3.9 当前版本{version}',pushKey)
            return False, "职校家园版本获取失败"
    except requests.exceptions.RequestException as error:
        pushMessage.pushMessage('职校家园版本',
                                f'职校家园版本获取错误{error}', pushKey)
        return False, f'职校家园版本获取失败{error}'
