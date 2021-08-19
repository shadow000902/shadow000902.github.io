---
title: Allure报告结果钉钉发送Python实现
date: '2020-10-10T12:33:01.000Z'
categories:
  - Tools
tags:
  - allure
  - python
---

# 2020-10-10-Ding-Allure-Detail-Report

### Jenkins中的Allure插件，增加Owner插件

1. Jenkins中配置Allure插件，目录为`System Configuation -> Global Tool Configuration`，从中找到`Allure Commandline`
2. 下载`owners-failed-plugin`插件 [插件地址](https://pan.baidu.com/s/1qJF5V2Eb8w946DgYtgNUkA) 提取码: ifqw
3. 把插件加入`Allure Commandline`的安装目录中 安装完插件后，可以在Jenkins任务的执行机上，也就是jenkins任务真正执行的机器上，会有一个`workspace/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/Allure_Commandline/plugins`目录，这个`workspace`也就是Jenkins的一个工作空间 `plugins`目录下，就是`Allure`插件自带的一些插件 我们把第二步下载的插件解压后的文件夹，放到该目录下，`owners-failed-plugin`展示如下：

   ```bash
    # shadow @ domain in ~/jenkins_slave/workspace/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/Allure_Commandline/plugins [15:55:35] 
    $ ll
    total 48K
    drwxrwxr-x 3 shadow shadow 4.0K Sep  9 14:45 behaviors-plugin
    drwxrwxr-x 3 shadow shadow 4.0K Sep  9 14:45 custom-logo-plugin
    drwxrwxr-x 3 shadow shadow 4.0K Sep  9 14:45 jira-plugin
    drwxrwxr-x 2 shadow shadow 4.0K Sep  9 14:45 junit-xml-plugin
    drwxr-xr-x 3 shadow shadow 4.0K Sep 10 09:31 owners-failed-plugin
    drwxrwxr-x 3 shadow shadow 4.0K Sep  9 14:45 packages-plugin
    -rwxrwxr-x 1 shadow shadow   85 Jul  7 10:18 README.txt
    drwxrwxr-x 3 shadow shadow 4.0K Sep  9 14:45 screen-diff-plugin
    drwxrwxr-x 2 shadow shadow 4.0K Sep  9 14:45 trx-plugin
    drwxrwxr-x 3 shadow shadow 4.0K Sep  9 14:45 xctest-plugin
    drwxrwxr-x 3 shadow shadow 4.0K Sep  9 14:45 xray-plugin
    drwxrwxr-x 2 shadow shadow 4.0K Sep  9 14:45 xunit-xml-plugin
   ```

   然后需要退一层目录，把插件的配置写入配置文件中，不然就无法被调用到 \`\`\`shell script

   **shadow @ domain in ~/jenkins\_slave/workspace/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/Allure\_Commandline/plugins \[15:55:51\]**

   $ cd ..

   **shadow @ domain in ~/jenkins\_slave/workspace/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/Allure\_Commandline \[16:03:19\]**

   $ ll total 16K drwxrwxr-x 2 shadow shadow 4.0K Sep 9 14:45 bin drwxrwxr-x 2 shadow shadow 4.0K Sep 10 09:32 config drwxrwxr-x 3 shadow shadow 4.0K Sep 10 09:06 lib drwxrwxr-x 13 shadow shadow 4.0K Sep 10 09:31 plugins

   **shadow @ domain in ~/jenkins\_slave/workspace/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/Allure\_Commandline \[16:03:20\]**

   $ cd config

   **shadow @ domain in ~/jenkins\_slave/workspace/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/Allure\_Commandline/config \[16:03:25\]**

   $ ll total 8.0K -rwxrwxr-x 1 shadow shadow 0 Jul 7 10:18 allure-cucumber.yml -rwxrwxr-x 1 shadow shadow 46 Jul 7 10:18 allure-junit.yml -rwxrwxr-x 1 shadow shadow 205 Sep 10 09:32 allure.yml

   ```text
   编辑allure.yml文件，写入`owners-failed-plugin`配置如下：
    ```yaml
    plugins:
      - junit-xml-plugin
      - xunit-xml-plugin
      - trx-plugin
      - behaviors-plugin
      - packages-plugin
      - screen-diff-plugin
      - xctest-plugin
      - jira-plugin
      - xray-plugin
      - owners-failed-plugin
   ```

### 读取报告信息

* 报告总体信息："[http://jenkins.shadow.com/job/](http://jenkins.shadow.com/job/)" + JOB\_NAME + "/allure/widgets/summary.json"
* Owner具体信息："[http://jenkins.shadow.com/job/](http://jenkins.shadow.com/job/)" + JOB\_NAME + "/allure/data/owners.json"

### 脚本主要方法说明

1. `getSummary()` 方法返回总体信息

   ```javascript
    {
        "failed": 108,
        "broken": 25,
        "skipped": 196,
        "passed": 1055,
        "unknown": 0,
        "total": 1384
    }
   ```

2. `getResultDetails()` 方法返回Owner具体信息，并对异常数据做清理

   ```javascript
    [
        {
            "name": "张三",
            "children": [{"": "", "status": "passed"}, {"": "", "status": "failed"}, {"": "", "status": "broken"}, {"": "", "status": "skipped"}],
            "uid": "e1aaed47c8239f38d3450e9dfd3e7646"
        },
        {
            "name": "李四",
            "children": [{"": "", "status": "passed"}, {"": "", "status": "failed"}, {"": "", "status": "broken"}, {"": "", "status": "skipped"}],
            "uid": "90e00f4c3e58fc50b3766d36fe294203"
        }
    ]
   ```

3. `getPersonCounts()` 方法返回每个Owner的具体用例数据

   ```javascript
    [
      {
        "name": "张三",
        "total": 111,
        "passed": 110,
        "broken": 0,
        "skipped": 1,
        "failed": 0
      },
      {
        "name": "李四",
        "total": 56,
        "passed": 56,
        "broken": 0,
        "skipped": 0,
        "failed": 0
      }
    ]
   ```

4. `spillDingText()` 方法返回钉钉发送消息体中的`text`
5. `sendMarkdownDing()` 方法以markdown格式组织消息体，发送钉钉通知

### 完整脚本

```python
# -*- coding: utf-8 -*-
import json
import sys

import requests


'''
执行方式：python sendDingSummary.py Jenkins_Job webhook mobiles
'''

# Jenkins任务的名称
JOB_NAME = str(sys.argv[1])

# 只需要最后那个Token
WEBHOOK_TOKEN = str(sys.argv[2])

# 手机号用英文逗号分隔，可以不传
try:
    MOBILES = str(sys.argv[3])
except:
    MOBILES = None

reportUrl = 'http://jenkins.shadow.com/job/' + JOB_NAME + '/allure/'

mobiles = ""
if MOBILES:
    atMobiles = MOBILES.split(',')
    for mobile in atMobiles:
        mobiles += "@" + mobile
else:
    atMobiles = None


def getSummary():
    url = 'http://jenkins.shadow.com/job/' + JOB_NAME + '/allure/widgets/summary.json'
    summary = requests.get(url).json()['statistic']
    print(summary)
    return summary


def getResultDetails():
    url = 'http://jenkins.shadow.com/job/' + JOB_NAME + '/allure/data/owners.json'
    resultDetails = requests.get(url).json()['children']
    for resultDetail in resultDetails:
        if resultDetail.get("children") is None:
            resultDetails.remove(resultDetail)

    print(resultDetails)
    return resultDetails


def getPersonCounts():
    resultDetails = getResultDetails()
    personCounts = []
    for resultDetail in resultDetails:
        passed = 0
        broken = 0
        skipped = 0
        failed = 0
        for detail in resultDetail['children']:
            if detail['status'] == 'passed':
                passed += 1
            if detail['status'] == 'broken':
                broken += 1
            if detail['status'] == 'skipped':
                skipped += 1
            if detail['status'] == 'failed':
                failed += 1
        personCounts.append(
            {
                'name': resultDetail['name'],
                'total': len(resultDetail['children']),
                'passed': passed,
                'broken': broken,
                'skipped': skipped,
                'failed': failed
            }
        )

    print(personCounts)
    return personCounts


def spillDingText():
    summary = getSummary()
    Failed = summary['failed']
    Broken = summary['broken']
    Skipped = summary['skipped']
    Passed = summary['passed']
    Total = summary['total']
    PassRate = '%.2f%%' % (Passed / (Total - Skipped) * 100)
    summaryText = "### **『%s』项目接口自动化每日报告！**\n\n" \
                  " >%s\n\n" \
                  " >**[<font color=#0A83D1 >PassRate:%s</font>](%s)**\n\n" \
                  " >**<font color=#000000 >Total:%d</font>**\n\n" \
                  " >**<font color=#97CC64 >Passed:%d</font>, <font color=#AAAAAA >Skipped:%d</font>**\n\n" \
                  " >**<font color=#FF0000 >Failed:%d</font>, <font color=#FFD050 >Broken:%d</font>**\n\n" \
                  % (JOB_NAME, mobiles, PassRate, reportUrl, Total, Passed, Skipped, Failed, Broken)

    personCounts = getPersonCounts()
    personCountsText = ''
    for personCount in personCounts:
        Name = personCount['name']
        Total = personCount['total']
        Failed = personCount['failed']
        Broken = personCount['broken']
        Skipped = personCount['skipped']
        Passed = personCount['passed']
        PassRate = '%.2f%%' % (Passed / (Total - Skipped) * 100)
        personCountText = "**『%s』：**\n\n" \
                          " ><font color=#000000 >Total:%d</font>, <font color=#0A83D1 >PassRate:%s</font>\n\n" \
                          " ><font color=#97CC64 >Passed:%d</font>, <font color=#AAAAAA >Skipped:%d</font>, " \
                          " <font color=#FF0000 >Failed:%d</font>, <font color=#FFD050 >Broken:%d</font>\n\n" \
                          % (Name, Total, PassRate, Passed, Skipped, Failed, Broken)
        personCountsText += personCountText
    text = summaryText + personCountsText
    print(text)
    return text


def sendMarkdownDing():
    # 1、构建url
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=" + WEBHOOK_TOKEN
    # 2、构建一下请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 3、构建请求数据
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "接口自动化执行报告，请及时跟进处理！",
            "text": spillDingText()
        },
        "at": {
            "atMobiles": atMobiles,
            "isAtAll": False
        }
    }
    print(data)
    # 4、对请求的数据进行json封装
    sendData = json.dumps(data)  # 将字典类型数据转化为json格式
    sendData = sendData.encode("utf-8")  # python3的Request要求data为byte类型
    # 5、发送请求
    resp = requests.post(url=webhook, data=sendData, headers=header)
    print(resp.json())
    return resp.json()


if __name__ == '__main__':
    sendMarkdownDing()
```

