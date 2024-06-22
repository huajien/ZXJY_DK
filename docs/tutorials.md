

## 使用教程

一个基于 python的打卡项目。

已支持的平台：

- Windows
- Mac OS
- Linux
- 等平台
- `推荐Linux环境下运行`
- `python >= 3.8`

#### 特点

软件更新自动停止打卡不会出现异常等情况随机延迟<br>
接入gpt自动填写日报周报月报<br>


使用方式
**需要提前下载`Python3`**
1. 下载项目

```bash
cd ~
git clone https://mirror.ghproxy.com/https://github.com/huajien/ZXJY_DK
```
不打卡的请使用命令<br>
```
git remote set-url origin https://mirror.ghproxy.com/https://github.com/huajien/ZXJY_DK
```
将源换位https://mirror.ghproxy.com 之前的域名商关了<br>


2. 安装依赖 <br>

```bash
cd ZXJY_DK

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
**如果不行使用**
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```
3. 单独添加用户<br>
```bash
python3 addUsers.py
**tips：可以直接执行main添加用户更加人性化😎**
```

4. 执行单此多用户打卡 <br>
```bash
 python3 main.py
```

### 配置每天定时自动打卡

Linux 下使用推荐使用 `crontab`
Windows 定时任务 不推荐使用（服务器除外）

```bash
crontab -e
最后下面添加

26 10 * * * cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1
```
跳过周六周日 执行的crontab 
<br>
每天周1-周5 月底最后一天运行
```bash
26 10 L * 1-5 cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1

```


```bash
解释上面crontab


每天早上10点26分，在~/ZXJY_DK目录下执行以下操作：
执行git fetch --all命令，从远程仓库中获取最新的更新。
执行git reset --hard origin/master命令，将本地分支指向与远程origin/master分支相同的位置，并完全覆盖本地分支的内容。
执行mkdir -p log命令，如果不存在log目录则创建一个。
执行python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1命令，将main.py的输出追加到以当前日期为名称的日志文件中。
```
例子：
```text

    # 每月的最后1天
    0 0 L * * *

    说明：
    Linux
    *    *    *    *    *
    -    -    -    -    -
    |    |    |    |    |
    |    |    |    |    +----- day of week (0 - 7) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    |    |    |    +---------- month (1 - 12) OR jan,feb,mar,apr ...
    |    |    +--------------- day of month (1 - 31)
    |    +-------------------- hour (0 - 23)
    +------------------------- minute (0 - 59)
```

整体**userData.json**文件结构
```python
  {
    #总开关
    "enabled": True,
    #别名
    "remark": "张三",
   #手机号就是职校家园手机号
    "phone": "18888888888",
    #密码职校家密码
    "password": "admin",
    #手机设备型号
    "deviceModel": "Redmi|22011211C|13",
    #设备id
    "deviceId": "io6tkwgdz2mxcsrv0lupq84a9n51j37fhbye",
    #打卡的位置
    "address": "河南省郑州市郑东新区正光路11号",
    #经纬度
    "longitude": "113.752490",
    "latitude": "34.768420",
    #pushplus的推送key用于通知打卡成功和失败记得认真填写哦
    "pushKey": "fffe8fdb8d49490fa6213fc94b9365da",
    #报告开关
    "report": True
  }
```
