## 更新信息
### 2024年6月14日更新
- **版本升级至0.499**：版本号更新<br>
- 替换新的职校家园域名
- app版本晚会更新这个电脑没有安卓开发环境我需要配置一下找时间更新
- 建议将crontab 替换如下 可以自动更新<br>
```bash
26 10 * * * cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1
```

### 2024年6月9日更新
- **版本升级至0.498**：版本号更新<br>
- 感谢[XYZ](https://github.com/321930869)建议升级 gpt 的Prompt [[SUGGESTION] 优化 ChatGPT 生成实习报告的提示词 #21
](https://github.com/huajien/ZXJY_DK/issues/21)
- 建议将crontab 替换如下 可以自动更新<br>
```bash
26 10 * * * cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1
```

### 2024年5月12日更新
- **版本升级至0.497**：版本号更新<br>
- 建议将crontab 替换如下 可以自动更新<br>
```bash
26 10 * * * cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1
```

### 2024年5月2日更新
- **版本升级至0.496**：版本号更新<br>
- 修复gpt 日报周报月报失败问题<br>
- **此版本强制升级**<br>
- 建议将crontab 替换如下 可以自动更新<br>
```bash
26 10 * * * cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1
```

### 2024年3月28日更新
- **version** 升级为v1.4.6<br>
- **版本升级至0.495**：版本号更新<br>
- 建议将crontab 替换如下根据自身情况调整<br>
```bash
26 10 * * * cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1
```

###  2024年2月24日更新
- 更新说明文档<br>
- 建议将crontab 替换如下根据自身情况调整<br>
```bash
26 10 * * * cd ~/ZXJY_DK && git fetch --all && git reset --hard origin/master && mkdir -p log && python3 main.py >> log/$(date +"\%Y-\%m-\%d").log 2>&1
```
- **version** 升级为v1.4.5<br>
- **版本升级至0.494**：版本号更新<br>




###  2024年1月27日更新
- 更新说明文档<br>
- 优化crontab运行前自动更新代码<br>
- **version** 优化版本控制<br>
- **main.py** inputimeout改为30秒 <br>
- **版本升级至0.493**：版本号更新<br>


###  2024年1月17日更新
- 增加微信赞赏码 <br>
- 新增app端 暂时只有打卡功能<br>
- **punchCard.py** 修复打卡使用参数错误 phonetype <br>
- **版本升级至0.492**：版本号更新<br>




###  2024年1月14日更新
- 感谢 [321930869](https://github.com/321930869) 提出问题和解决方案目<br>
- **sendReport.py** 已解决周报开始时间计算逻辑错误<br>
- **版本升级至0.491**：版本号更新<br>


###  2024年1月13日更新
- version.py**调整为1.4.4版本**<br>
- 新版本没有更换东西正常运行<br>
- **版本升级至0.49**：版本号更新<br>



###  2024年1月1日更新
- 新年快乐🎉<br>
- 更新说明文档<br>
- sendReport.py**报告重试次数更新为10次，优化提示词**<br>
- **版本升级至0.48**：版本号更新，日报重试次数更新为10次，月报错误等<br>

###  2023年12月25日更新
- 更新说明文档<br>
- 优化一下gpt问题<br>


###  2023年12月02日更新
- sendReport.py**修复无法日报问题,加入三次ChatGPT重试**<br>
- parsUserConfig.py**减少等待时间**<br>
- **版本升级至0.47**：版本号更新，包含了最新的修复日报错误。<br>


###  2023年12月01日更新
- addUsers.py**文件优化对其**<br>
- gptReport.py**增加ChatGPT请求时间**<br>
- main.py**去除无用的库和代码**<br>
- parsUserConfig.py**去除无用的库添加random和延迟执行代码**<br>
- sendReport.py**重构整个ChatGPT报告转换**<br>
- requirements.txt**添加urllib3将固定固定在1.25版本**<br>
- **版本升级至0.46**：版本号更新，包含了最新的改进。<br>

###  2023年11月24日更新
- 优化crontab 日志信息<br>
- 优化README.md文件更好阅读<br>
- 去除cChardet库<br>

###  2023年11月19日晚更新
- 优化消息推送提示<br>
- 优化登录提示<br>
- 调整用户可以**只打卡或者只写日报周报月报**<br>
- **优化登录提示**<br>
- 修复**main.py**来回调用<br>
- 固定openai版本定在**0.28.0**<br>
- **版本升级至0.45**：版本号更新，包含了最新的改进。<br>
- 暂停几天更新，如有大问题会看情况更新代码<br>

###  2023年11月19日更新
- 清空**（zy***10）**作者adduser.py代码<br>
- 不升级版本号<br>
- 很不爽好自大的**（zy***10）**作者<br>
- 修复其他函数调用main.py报错问题<br>

###  2023年11月18日更新

- **addUsers.py文件优化**：通过简化调用方式，使其更易使用。
- **loadUsers.py文件提示优化**：提高用户友好性。
- **inputimeout库应用**：引入了inputimeout库，实现了超时功能的用户输入处理。
- **版本升级至0.44**：标明版本号升级。

### 2023年11月15日更新

- **addUsers.py文件优化**：对文件进行了调整以提升效率。
- **版本升级至0.43**：版本号更新，包含了最新的改进。
- **README优化**：对README文件进行了更新以提供更好的使用教程。

### 2023年11月14日晚更新

- **addUsers.py文件优化**：对文件进行了调整以提升效率。
- **版本升级至0.42**：版本号更新，包含了最新的改进。
- **README使用教程优化**：进一步优化README文件，使得使用更加方便。

### 2023年11月14日更新

- **请求头优化**：对token请求头进行了优化。
- **问题报告优化**：优化了gpt提问报告问题的处理。
- **版本升级至0.41**：版本号更新，包含了最新的改进。

### 2023年11月12日更新

- **脚本优化**：对脚本进行了一些优化。
- **版本升级至0.4**：版本号更新，包含了最新的改进。
- **Bug修复**：修复了不打卡的bug。

### 2023年11月12日更新

- **日报周报月报内容优化**：内容由岗位使用gpt自动生成。
- **版本升级至0.3**：版本号更新，包含了最新的改进。
- **小问题修复**：修复了一些小问题。

### 2023年11月11日更新

- **适配新版本v.1.4.1**：脚本适配了新的版本v.1.4.1。
- **请求头信息更新**：更新了请求头信息以保持兼容性。
- **版本控制软件加入**：引入了版本控制软件以更好地管理版本。
- **版本升级至0.2**：版本号更新，包含了最新的改进。
- **小bug优化**：优化了一些小bug。

### 2023年11月10日 初版：

- **适配v.1.3.9版本**：脚本适配了v.1.3.9版本。
