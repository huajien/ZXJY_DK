import json
import os
import random
import re
import string
import time
from urllib.parse import quote

import requests

import pushMessage

path = os.getcwd() + os.sep


def write_user(filename, newdata):
    with open(filename, 'r', encoding='utf-8') as f:
        olddata = f.read()
    olddata = json.loads(olddata)
    olddata.extend(newdata)
    with open(filename, 'w', encoding='utf-8') as write_f:
        write_f.write(json.dumps(olddata, indent=2, ensure_ascii=False))


def obtainCoordinates(address):
    key = "UGMBZ-CINWR-DDRW5-W52AK-D3ENK-ZEBRC"
    response = requests.get(
        f"https://apis.map.qq.com/jsapi?qt=geoc&addr={quote(address, safe='')}&key={key}&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb3.geocoder0",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36",
            "content-type": "application/json;charset=utf-8",
            "accept-encoding": "gzip, deflate",
            "Referer": "https://jingweidu.bmcx.com/"
        })
    return re.search(r'"pointx":"(.*?)"', response.text).group(1), re.search(r'"pointy":"(.*?)"', response.text).group(
        1)


def checkUserData(filename, enabled, remark, phone, password, deviceModel, address, PushPlus_token, report):
    deviceId = ''.join(random.choice(string.digits + 'abcdef') for _ in range(36))
    longitude, latitude = obtainCoordinates(address)
    newdata = [
        {
            "enabled": enabled,
            "remark": remark,
            "phone": phone,
            "password": password,
            "deviceModel": deviceModel,
            "deviceId": deviceId,
            "address": address,
            "longitude": longitude,
            "latitude": latitude,
            "pushKey": PushPlus_token,
            "report": report
        }
    ]
    write_user(filename=filename, newdata=newdata)


# 职家家园添加用户
# 来源 https://github.com/zycn0910/Sign-ZXJY

def getDeviceModel():
    models = [
        #一加手机
        "OnePlus|ONEPLUS A6010|10",
        "OnePlus|GM1900|10",
        "OnePlus|GM1910|10",
        "OnePlus|HD1900|10",
        "OnePlus|HD1910|10",
        "OnePlus|IN2010|10",
        "OnePlus|IN2020|10",
        "OnePlus|KB2000|10",
        "OnePlus|LE2100|10",
        "OnePlus|LE2110|10",
        "OnePlus|LE2120|10",
        "OnePlus|MT2110|10",
        "OnePlus|NE2210|10",
        "OnePlus|PGKM10|10",
        "OnePlus|PGZ110|10",
        "OnePlus|PGP110|10",
        "OnePlus|PHB110|10",
        "OnePlus|PHK110|10",
        "OnePlus|PHP110|10",
        "OnePlus|PJA110|10",
        "OnePlus|PJD110|10",
        #OPPO手机
        "OPPO|PAFM00|12",
        "OPPO|PDEM10|12",
        "OPPO|PDEM30|12",
        "OPPO|PEDM00|12",
        "OPPO|PEEM00|12",
        "OPPO|PFFM10|12",
        "OPPO|PFEM10|12",
        "OPPO|PFFM20|12",
        "OPPO|PGFM10|12",
        "OPPO|PGEM10|12",
        "OPPO|PEUM00|12",
        "OPPO|PGU110|12",
        "OPPO|PGT110|12",
        "OPPO|PHN110|12",
        "OPPO|PHT110|12",
        "OPPO|PCAM00|12",
        "OPPO|PCCM00|12",
        "OPPO|PCDM10|12",
        "OPPO|PCKM00|12",
        "OPPO|PCKM80|12",
        "OPPO|PDCM00|12",
        "OPPO|PCRM00|12",
        "OPPO|PCLM50|12",
        "OPPO|PDPM00|12",
        "OPPO|PDNM00|12",
        "OPPO|PEAM00|12",
        "OPPO|PEGM00|12",
        "OPPO|PEGM10|12",
        "OPPO|PDSM00|12",
        "OPPO|PDRM00|12",
        "OPPO|PEQM00|12",
        "OPPO|PEPM00|12",
        "OPPO|PENM00|12",
        "OPPO|PFJM10|12",
        "OPPO|PFDM00|12",
        "OPPO|PFCM00|12",
        "OPPO|PGBM10|12",
        "OPPO|PGAM10|12",
        "OPPO|PFZM10|12",
        "OPPO|PHM110|12",
        "OPPO|PGX110|12",
        "OPPO|PGW110|12",
        "OPPO|PHW110|12",
        "OPPO|PHV110|12",
        "OPPO|PHU110|12",
        "OPPO|PCLM10|12",
        "OPPO|PDHM00|12",
        "OPPO|PACM00|12",
        "OPPO|PAAM00|12",
        "OPPO|PBCM10|12",
        "OPPO|PBEM00|12",
        "OPPO|PBDM00|12",
        "OPPO|PADM00|12",
        "OPPO|PBAM00|12",
        "OPPO|PBFM00|12",
        "OPPO|PBBM00|12",
        "OPPO|PCDM00|12",
        "OPPO|PDBM00|12",
        "OPPO|PCAM10|12",
        "OPPO|PCEM00|12",
        "OPPO|PCHM10|12",
        "OPPO|PCHM30|12",
        "OPPO|PCHM00|12",
        "OPPO|PDVM00|12",
        "OPPO|PDVM00|12",
        "OPPO|PEFM00|12",
        "OPPO|PESM10|12",
        "OPPO|PDAM10|12",
        "OPPO|PECM20|12",
        "OPPO|PEMM00|12",
        "OPPO|PEMM00|12",
        "OPPO|PFVM10|12",
        "OPPO|PFTM20|12",
        "OPPO|PFTM20|12",
        "OPPO|PHJ110|12",
        "OPPO|PHJ110|12",
        "OPPO|PDYM20|12",
        "OPPO|PDYM10|12",
        "OPPO|PCPM00|12",
        "OPPO|PDKM00|12",
        "OPPO|PEHM00|12",
        "OPPO|PFGM00|12",
        "OPPO|PELM00|12",
        "OPPO|PFUM10|12",
        "OPPO|PFTM10|12",
        "OPPO|PHS110|12",
        "OPPO|PHQ110|12",
        "OPPO|PHJ110|12",
        "OPPO|PJB110|12",
        "OPPO|PJU110|12",
        "OPPO|PJS110|12",
        "OPPO|PJG110|12",
        "OPPO|PBCM30|12",
        "OPPO|PCGM00|12",
        "OPPO|PCNM00|12",
        "OPPO|PCLM50|12",
        "OPPO|PERM00|12",
        "OPPO|PEXM00|12",
        "OPPO|PERM10|12",
        "OPPO|PEYM00|12",
        "OPPO|PGCM10|12",
        "OPPO|PGJM10|12",
        "OPPO|PGIM10|12",
        "OPPO|PGGM10|12",
        "OPPO|PJC110|12",
        "OPPO|PHF110|12",
        #华为手机
        "HUAWEI|HUAWEI MT1-T00|12",
        "HUAWEI|HUAWEI MT2-U071|12",
        "HUAWEI|HUAWEI MT7-TL00|12",
        "HUAWEI|HUAWEI CRR-TL00|12",
        "HUAWEI|HUAWEI NXT-AL10|12",
        "HUAWEI|MHA-AL00|12",
        "HUAWEI|LON-AL00|12",
        "HUAWEI|LON-AL00|12",
        "HUAWEI|ALP-AL00|12",
        "HUAWEI|BLA-AL00|12",
        "HUAWEI|BLA-AL00|12",
        "HUAWEI|NEO-AL00|12",
        "HUAWEI|HMA-AL00|12",
        "HUAWEI|LYA-AL00|12",
        "HUAWEI|EVR-AL00|12",
        "HUAWEI|LYA-AL00P|12",
        "HUAWEI|TAS-AL00|12",
        "HUAWEI|LIO-AL00|12",
        "HUAWEI|LIO-AN00m|12",
        "HUAWEI|LIO-AN00P|12",
        "HUAWEI|OCE-AN10|12",
        "HUAWEI|OCE-AN50|12",
        "HUAWEI|NOH-AN00|12",
        "HUAWEI|NOH-AN50|12",
        "HUAWEI|NOP-AN00|12",
        "HUAWEI|NOP-AN00|12",
        "HUAWEI|CET-AL00|12",
        "HUAWEI|CET-AL60|12",
        "HUAWEI|DCO-AL00|12",
        "HUAWEI|DCO-AL00|12",
        "HUAWEI|BRA-AL00|12",
        "HUAWEI|ALN-AL00|12",
        "HUAWEI|ALN-AL10|12",
        "HUAWEI|ALN-AL10|12",
        "HUAWEI|TAH-AN00|12",
        "HUAWEI|TAH-AN00m|12",
        "HUAWEI|TET-AN00|12",
        "HUAWEI|PAL-AL00|12",
        "HUAWEI|ALT-AL00|12",
        "HUAWEI|ALT-AL10|12",
        "HUAWEI|HUAWEI U9200|12",
        "HUAWEI|HUAWEI P2-0000|12",
        "HUAWEI|HUAWEI P6-T00|12",
        "HUAWEI|HUAWEI P6 S-U06|12",
        "HUAWEI|HUAWEI P7-L00|12",
        "HUAWEI|HUAWEI GRA-TL00|12",
        "HUAWEI|HUAWEI ALE-TL00|12",
        "HUAWEI|DAV-703L|12",
        "HUAWEI|EVA-AL00|12",
        "HUAWEI|VIE-AL10|12",
        "HUAWEI|VTR-AL00|12",
        "HUAWEI|VKY-AL00|12",
        "HUAWEI|EML-AL00|12",
        "HUAWEI|CLT-AL00|12",
        "HUAWEI|ELE-AL00|12",
        "HUAWEI|VOG-AL00|12",
        "HUAWEI|ANA-AL00|12",
        "HUAWEI|ELS-AN00|12",
        "HUAWEI|ELS-AN10|12",
        "HUAWEI|ABR-AL00|12",
        "HUAWEI|ABR-AL60|12",
        "HUAWEI|JAD-AL00|12",
        "HUAWEI|BAL-AL00|12",
        "HUAWEI|LNA-AL00|12",
        "HUAWEI|MNA-AL00|12",
        "HUAWEI|MNA-AL00|12",
        "HUAWEI|HUAWEI CAZ-AL00|12",
        "HUAWEI|WAS-AL00|12",
        "HUAWEI|PIC-AL00|12",
        "HUAWEI|BAC-AL00|12",
        "HUAWEI|HWI-AL00|12",
        "HUAWEI|ANE-AL00|12",
        "HUAWEI|PAR-AL00|12",
        "HUAWEI|INE-AL00|12",
        "HUAWEI|VCE-AL00|12",
        "HUAWEI|MAR-AL00|12",
        "HUAWEI|SEA-AL00|12",
        "HUAWEI|SEA-AL10|12",
        "HUAWEI|GLK-AL00|12",
        "HUAWEI|SPN-AL00|12",
        "HUAWEI|SPN-AL00|12",
        "HUAWEI|WLZ-AL10|12",
        "HUAWEI|WLZ-AN00|12",
        "HUAWEI|JNY-AL10|12",
        "HUAWEI|JEF-AN00|12",
        "HUAWEI|JER-AN10|12",
        "HUAWEI|CDY-AN00|12",
        "HUAWEI|CND-AN00|12",
        "HUAWEI|CDL-AN50|12",
        "HUAWEI|ANG-AN00|12",
        "HUAWEI|BRQ-AN00|12",
        "HUAWEI|JSC-AN00|12",
        "HUAWEI|CHL-AL60|12",
        "HUAWEI|NAM-AL00|12",
        "HUAWEI|RTE-AL00|12",
        "HUAWEI|JLN-AL00|12",
        "HUAWEI|NCO-AL00|12",
        "HUAWEI|GLA-AL00|12",
        "HUAWEI|CHA-AL80|12",
        "HUAWEI|BNE-AL00|12",
        "HUAWEI|JLN-AL00|12",
        "HUAWEI|FOA-AL00|12",
        "HUAWEI|GOA-AL80|12",
        "HUAWEI|GOA-AL80U|12",
        "HUAWEI|BON-AL00|12",
        #Vivo手机
        "Vivo|V1821A|13",
        "Vivo|V1923A|13",
        "Vivo|V1924A|13",
        "Vivo|V1950A|13",
        "Vivo|V1814A|13",
        "Vivo|V1809A|13",
        "Vivo|V1816A|13",
        "Vivo|V1829A|13",
        "Vivo|V1838A|13",
        "Vivo|V1836A|13",
        "Vivo|V1938CA|13",
        "Vivo|V1938A|13",
        "Vivo|V2001A|13",
        "Vivo|V2005A|13",
        "Vivo|V2011A|13",
        "Vivo|V2046A|13",
        "Vivo|V2059A|13",
        "Vivo|V2085A|13",
        "Vivo|V2047A|13",
        "Vivo|V2120A|13",
        "Vivo|V2056A|13",
        "Vivo|V2056A|13",
        "Vivo|V2133A|13",
        "Vivo|V2132A|13",
        "Vivo|V2134A|13",
        "Vivo|V2145A|13",
        "Vivo|V2178A|13",
        "Vivo|V2170A|13",
        "Vivo|V2183A|13",
        "Vivo|V2185A|13",
        "Vivo|V2186A|13",
        "Vivo|V2229A|13",
        "Vivo|V2241A|13",
        "Vivo|V2241HA|13",
        "Vivo|V2242A|13",
        "Vivo|V2227A|13",
        "Vivo|V2266A|13",
        "Vivo|V2256A|13",
        "Vivo|V2309A|13",
        "Vivo|V2324A|13",
        "Vivo|V1831A|13",
        "Vivo|V1832A|13",
        "Vivo|V1932A|13",
        "Vivo|V1962A|13",
        "Vivo|V2020A|13",
        "Vivo|V2080A|13",
        "Vivo|V2031A|13",
        "Vivo|V2031EA|13",
        "Vivo|V2072A|13",
        "Vivo|V2048A|13",
        "Vivo|V2121A|13",
        "Vivo|V2121A|13",
        "Vivo|V2130A|13",
        "Vivo|V2162A|13",
        "Vivo|V2163A|13",
        "Vivo|V2203A|13",
        "Vivo|V2207A|13",
        "Vivo|V2190A|13",
        "Vivo|V2244A|13",
        "Vivo|V2245A|13",
        "Vivo|V2239A|13",
        "Vivo|V2283A|13",
        "Vivo|V2282A|13",
        "Vivo|V2284A|13",
        "Vivo|V2285A|13",
        "Vivo|V1801A0|13",
        "Vivo|V1730DA|13",
        "Vivo|V1730EA|13",
        "Vivo|V1813BA|13",
        "Vivo|V1813A|13",
        "Vivo|V1813A|13",
        "Vivo|V1730GA|13",
        "Vivo|V1921A|13",
        "Vivo|V1911A|13",
        "Vivo|V1990A|13",
        "Vivo|V1941A|13",
        "Vivo|V1963A|13",
        "Vivo|V1824BA|13",
        "Vivo|V1922A|13",
        "Vivo|V1916A|13",
        "Vivo|V1955A|13",
        "Vivo|V2024A|13",
        "Vivo|V2025A|13",
        "Vivo|V2049A|13",
        "Vivo|V2136A|13",
        "Vivo|V2141A|13",
        "Vivo|V2171A|13",
        "Vivo|V2172A|13",
        "Vivo|V2217A|13",
        "Vivo|V2218A|13",
        "Vivo|V2243A|13",
        "Vivo|V2254A|13",
        "Vivo|V2304A|13",
        "Vivo|V2307A|13",
        "Vivo|V2329A|13",
        "Vivo|V1914A|13",
        "Vivo|V1936A|13",
        "Vivo|V1936AL|13",
        "Vivo|V1981A|13",
        "Vivo|V2055A|13",
        "Vivo|V2118A|13",
        "Vivo|V2154A|13",
        "Vivo|V2157A|13",
        "Vivo|V2196A|13",
        "Vivo|V2199A|13",
        "Vivo|V2231A|13",
        "Vivo|V2232A|13",
        "Vivo|V2238A|13",
        "Vivo|V2301A|13",
        "Vivo|V2302A|13",
        "Vivo|V1986A|13",
        "Vivo|V2012A|13",
        "Vivo|V2073A|13",
        "Vivo|V2148A|13",
        "Vivo|V2131A|13",
        "Vivo|V2220A|13",
        "Vivo|V2164KA|13",
        "Vivo|V2270A|13",
        "Vivo|V2272A|13",
        "Vivo|V2230EA|13",
        "Vivo|V2314A|13",
        "Vivo|V2312A|13",

        #小米手机
        "Xiaomi|MCE16|13",
        "Xiaomi|M1803E1A|13",
        "Xiaomi|M1807E8S|13",
        "Xiaomi|M1807E8A|13",
        "Xiaomi|M1805E2A|13",
        "Xiaomi|M1808D2TE|13",
        "Xiaomi|M1902F1A|13",
        "Xiaomi|M1908F1XE|13",
        "Xiaomi|M1903F2A|13",
        "Xiaomi|M1903F10G|13",
        "Xiaomi|M1903F11G|13",
        "Xiaomi|M1904F3BG|13",
        "Xiaomi|M2001J2E|13",
        "Xiaomi|M2001J1E|13",
        "Xiaomi|M2002J9E|13",
        "Xiaomi|M2002J9G|13",
        "Xiaomi|M2007J1SC|13",
        "Xiaomi|M2007J3SY|13",
        "Xiaomi|M2007J3SG|13",
        "Xiaomi|M2007J17G|13",
        "Xiaomi|M2102J2SC|13",
        "Xiaomi|M2011K2C|13",
        "Xiaomi|M2102K1AC|13",
        "Xiaomi|M2102K1C|13",
        "Xiaomi|M2101K9C|13",
        "Xiaomi|M2101K9AG|13",
        "Xiaomi|2107119DC|13",
        "Xiaomi|M2012K11G|13",
        "Xiaomi|21081111RG|13",
        "Xiaomi|2107113SG|13",
        "Xiaomi|2201123C|13",
        "Xiaomi|2112123AC|13",
        "Xiaomi|2201122C|13",
        "Xiaomi|2207122MC|13",
        "Xiaomi|2203129G|13",
        "Xiaomi|2206123SC|13",
        "Xiaomi|2206122SC|13",
        "Xiaomi|2203121C|13",
        "Xiaomi|22071212AG|13",
        "Xiaomi|22081212UG|13",
        "Xiaomi|2211133C|13",
        "Xiaomi|2210132C|13",
        "Xiaomi|2304FPN6DC|13",
        "Xiaomi|2210129SG|13",
        "Xiaomi|2306EPN60G|13",
        "Xiaomi|23078PND5G|13",
        "Xiaomi|23127PN0CC|13",
        "Xiaomi|23116PN5BC|13",
        "Xiaomi|M1810E5E|13",
        "Xiaomi|M1810E5GG|13",
        "Xiaomi|M2011J18C|13",
        "Xiaomi|2106118C|13",
        "Xiaomi|22061218C|13",
        "Xiaomi|2308CPXD0C|13",
        "Xiaomi|M1904F3BC|13",
        "Xiaomi|M1904F3BT|13",
        "Xiaomi|M1906F9SC|13",
        "Xiaomi|M1910F4E|13",
        "Xiaomi|2109119BC|13",
        "Xiaomi|2109119BC|13",
        "Xiaomi|2209129SC|13",
        "Xiaomi|23046PNC9C|13",
        # Redmi手机
        "Redmi|21121119SC|13",
        "Redmi|2201117TG|13",
        "Redmi|2201117TY|13",
        "Redmi|21091116AC|13",
        "Redmi|22041219C|13",
        "Redmi|2201117SG|13",
        "Redmi|2201117SY|13",
        "Redmi|22031116BG|13",
        "Redmi|21091116C|13",
        "Redmi|2201116TG|13",
        "Redmi|2201116SC|13",
        "Redmi|21091116UC|13",
        "Redmi|22041216C|13",
        "Redmi|22041216UC|13",
        "Redmi|22095RA98C|13",
        "Redmi|23021RAAEG|13",
        "Redmi|23021RAA2Y|13",
        "Redmi|22101317C|13",
        "Redmi|23076RA4BC|13",
        "Redmi|2303CRA44A|13",
        "Redmi|23030RAC7Y|13",
        "Redmi|2209116AG|13",
        "Redmi|22101316C|13",
        "Redmi|22101316UCP|13",
        "Redmi|22101316UC|13",
        "Redmi|22101320C|13",
        "Redmi|23054RA19C|13",
        "Redmi|23049RAD8C|13",
        "Redmi|2312DRAABC|13",
        "Redmi|2312DRA50C|13",
        "Redmi|23090RA98C|13",
        "Redmi|M1903F10A|13",
        "Redmi|M1903F10I|13",
        "Redmi|M1903F11A|13",
        "Redmi|M1903F11I|13",
        "Redmi|M1903F11A|13",
        "Redmi|M2001G7AE|13",
        "Redmi|M2001G7AC|13",
        "Redmi|M1912G7BE|13",
        "Redmi|M2001J11C|13",
        "Redmi|M2001J11C|13",
        "Redmi|M2006J10C|13",
        "Redmi|M2007J3SC|13",
        "Redmi|M2012K11AC|13",
        "Redmi|M2012K11C|13",
        "Redmi|M2012K10C|13",
        "Redmi|22021211RC|13",
        "Redmi|22041211AC|13",
        "Redmi|22011211C|13",
        "Redmi|21121210C|13",
        "Redmi|22081212C|13",
        "Redmi|22041216I|13",
        "Redmi|23013RK75C|13",
        "Redmi|22127RK46C|13",
        "Redmi|22122RK93C|13",
        "Redmi|23078RKD5C|13",
    ]
    return random.choice(models)

if __name__ == '__main__':
    filename = "userData.json"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    enabled = input("是否开启打卡y or n（默认y）：")
    if enabled == "y" or enabled == "Y":
        enabled = True
    elif enabled == "n" or enabled == "N":
        enabled = False
    else:
        enabled = True
    name = input("输入例如(张三)：")
    while True:
        pattern = re.compile(r'^1[3-9]\d{9}$')
        phone = input("输入账号(手机号)：")
        if pattern.search(phone):
            break
        else:
            print(f"手机号不正确！")
    # 密码
    while True:
        password = input("请输入密码：")
        password_confirm = input("再次输入密码进行确认：")
        if password_confirm == password:
            print("密码设置成功！")
            break
        else:
            print(f"两次密码不一致")
    # 手机型号
    deviceModel = getDeviceModel()
    # 打卡地址
    address = input("输入打卡地址请输入公司地址\n例如河南省郑州市郑东新区正光路\n:")
    # 推送push
    PushPlus_token = input("PushPlus_token: ")
    # 报告开关
    report = input("是否开启日报周报月报 y or n（默认y）：")
    if report == "y" or report == "Y":
        report = True
    elif report == "n" or report == "N":
        report = False
    else:
        report = True
    path = os.getcwd() + os.sep + "aiReport.json"
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
        for entry in data:
            if "api_key" in entry:
                reportSwitch = 0
                break
            else:
                reportSwitch = 1
    else:
        reportSwitch = 1

    if reportSwitch and report:
        pattern = re.compile(r'^sk-[a-zA-Z0-9]{48}$')
        while True:
            print("获取 key https://api.chatanywhere.org/v1/oauth/free/github/render ")
            api_key = input("输入你的key：")
            if pattern.search(api_key):
                newdata = [{
                    "api_key": api_key
                }]
                with open(path, 'w') as f:
                    json.dump(newdata, f, indent=2)
                break
            else:
                print("key格式错误，请重新输入。\n")

    userdata = checkUserData(filename, enabled, name, phone, password,
                                 deviceModel, address,
                                 PushPlus_token, report)
    print(
        f"添加时间 {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} "
        f"打卡开关{enabled} 报告开关{report} 别名{name} 手机号 {phone} 密码{password} 打卡位置{address}")
    pushMessage.pushMessage(f"添加{name}用户成功",
                            f"打卡开关{enabled} 报告开关{report} 别名{name} 手机号 {phone} 密码{password} 打卡位置{address}",
                            PushPlus_token)
