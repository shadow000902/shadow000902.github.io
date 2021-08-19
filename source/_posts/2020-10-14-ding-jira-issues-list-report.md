---
title: Jira问题列表转图片钉钉发送Python实现
date: '2020-10-14T18:43:13.000Z'
categories:
  - Tools
tags:
  - jira
  - python
---

# 2020-10-14-Ding-Jira-Issues-List-Report

## 主要用到的开源API

1. 公司内部JIRA的API文档地址：[https://jira.shadow.com/plugins/servlet/restbrowser\#/](https://jira.shadow.com/plugins/servlet/restbrowser#/)
2. JIRA官方提供的API文档地址：[https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)

    官方已经出到第三个版本，使用时需要根据自己公司使用的API版本来进行调用

    官方提供了各个语言的调用示例，可以进行参考

3. 图床服务的API文档地址：[https://doc.sm.ms/](https://doc.sm.ms/) 如果自己公司有影像件服务的话，可以传到公司的oss上进行保存

## 具体使用到的API

1. 获取JIRA筛选器详情：[https://jira.shadow.com/rest/api/2/filter/{id}](https://jira.shadow.com/rest/api/2/filter/{id})
2. 获取问题列表：[https://jira.shadow.com/rest/api/2/search](https://jira.shadow.com/rest/api/2/search)
3. 上传图片到图床：[https://sm.ms/api/v2/upload](https://sm.ms/api/v2/upload)

## 脚本主要方法说明

1. `getIssuesList()` 方法获取问题列表 首先调用`filter`接口，获取到筛选器的详情，从中取出`jql`字段值 然后调用`search`接口，获取问题列表
2. `getShowWords()` 方法获取问题列表中所需的字段，并构建新的`jsonList` 从原有复杂的问题列表的json返回接口中，提取出所需的字段

   ```javascript
    [
        {
            "类型": "缺陷",
            "关键字": "ZSY-844",
            "链接": "https://jira.shadow.com/browse/ZSY-844",
            "概要": "【H5】工单失败",
            "报告人": "XX「测试」",
            "经办人": "XX「开发」",
            "优先级": "P1",
            "状态": "Close",
            "创建时间": "2020-10-12 16:37:23",
            "更新时间": "2020-10-12 19:03:20"
        },
        {
            "类型": "缺陷",
            "关键字": "ZSY-843",
            "链接": "https://jira.shadow.com/browse/ZSY-843",
            "概要": "【H5】未显示指定门店",
            "报告人": "XX「测试」",
            "经办人": "XX「开发」",
            "优先级": "P3",
            "状态": "Close",
            "创建时间": "2020-10-12 16:02:58",
            "更新时间": "2020-10-12 17:55:15"
        }
    ]
   ```

3. `json2Excel()` 方法把第二点中得到的json转换成`Excel`，返回写入内容的`Excel`文件
4. `excel2Image.py`自定义类中的`excel_html()` 方法把`Excel`文件转换为`HTML`文件
5. `excel2Image.py`自定义类中的`html_image()` 方法把`HTML`文件转换为`.png`格式的图片
6. `getBugImageUrl()` 方法把图片上传到图床服务，并获取到对应的图片`URL`
7. `sendMarkdownDing()` 方法以markdown格式组织消息体，发送钉钉通知

## 完整脚本

### `excel2Image.py`自定义类文件

```python
# -*- coding:utf-8 -*-

import pandas as pd
import codecs
import imgkit


# ReportImage -> report convert include multiple sheets into pictures
class ReportImage:

    def __init__(self):
        pass

    # excel_html -> convert excel include multiple sheets into multiple html file
    # excel_file -> file
    # html_path -> path
    @staticmethod
    def excel_html(excel_file, html_path):
        html_list = []
        excel_obj = pd.ExcelFile(excel_file)
        sheet_list = excel_obj.sheet_names
        index = 0
        for i in sheet_list:
            html_file = html_path + i + ".html"
            excel_data = excel_obj.parse(excel_obj.sheet_names[index])
            with codecs.open(html_file, 'w', 'utf-8') as html:
                html.write(excel_data.to_html(header=True, index=True))
            html_list.append(html_file)
            index += 1
        return html_list

    # html_image -> convert htmls into pictures file
    # html_list -> list
    # image_path -> path
    @staticmethod
    def html_image(html_list, image_path):
        index = 0
        for i in html_list:
            img_obj = image_path + str(index) + ".png"
            with open(i, 'r') as html_file:
                # options内的参数，具体可以通过命令  `wkhtmltoimage --extended-help`  获取到详细的信息
                imgkit.from_file(html_file, img_obj, options={"encoding": "UTF-8", "width": 1920, "quality": 100})
            index += 1


if __name__ == '__main__':
    html_list = ReportImage.excel_html("data.xlsx", "./")
    ReportImage.html_image(html_list, "./")
```

### `jiraSearch.py`脚本实现文件

```python
# -*- coding: utf-8 -*-


# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import json
import sys

import requests
import tablib
from requests.auth import HTTPBasicAuth

import excel2Image

'''
执行方式：python jiraSearch.py webhook mobiles
'''

WEBHOOK_TOKEN = str(sys.argv[1])

try:
    MOBILES = str(sys.argv[2])
except:
    MOBILES = None

mobiles = ""
if MOBILES:
    atMobiles = MOBILES.split(',')
    for mobile in atMobiles:
        mobiles += "@" + mobile
else:
    atMobiles = None


def getIssuesList():
    issuesSearchUrl = "https://jira.shadow.com/rest/api/2/search"
    filterUrl = "https://jira.shadow.com/rest/api/2/filter/26517"
    auth = HTTPBasicAuth("taoyi", "XXXXXXXXXXXXXXXX")
    headers = {
        "Accept": "application/json"
    }

    filterResp = requests.request(
        "GET",
        filterUrl,
        headers=headers,
        auth=auth
    )

    jql = filterResp.json()['jql']

    query = {'jql': jql}

    response = requests.request(
        "GET",
        issuesSearchUrl,
        headers=headers,
        params=query,
        auth=auth
    )
    issuesList = response.json()['issues']
    # print(issuesList)
    return issuesList


def getShowWords():
    issueWords = []
    issuesList = getIssuesList()
    for issue in issuesList:
        issueWords.append({'类型': issue['fields']['issuetype']['name'],
                           '关键字': issue['key'],
                           '概要': issue['fields']['summary'],
                           '报告人': issue['fields']['reporter']['displayName'],
                           '经办人': issue['fields']['assignee']['displayName'],
                           '优先级': issue['fields']['priority']['name'],
                           '状态': issue['fields']['status']['name'],
                           '创建时间': issue['fields']['created'].replace('T', ' ').split('.')[0],
                           '更新时间': issue['fields']['updated'].replace('T', ' ').split('.')[0]})

    print(issueWords)
    return issueWords


def json2Excel():
    rows = getShowWords()
    # 将json中的key作为header, 也可以自定义header（列名）
    header = tuple([i for i in rows[0].keys()])
    # print('header',header)
    data = []
    # 循环里面的字典，将value作为数据写入进去
    for row in rows:
        body = []
        for v in row.values():
            body.append(v)
        data.append(tuple(body))
    # print('data',data)
    data = tablib.Dataset(*data, headers=header)
    print(data)
    open('data.xlsx', 'wb').write(data.xlsx)


def getBugImageUrl():
    url = 'https://sm.ms/api/v2/upload'
    headers = {'Authorization': 'dq2u9BXgV2AzsZm7UUzxz8heTxl4ojmM'}
    file_obj = open('./0.png', 'rb')
    file = {'smfile': file_obj}  # 参数名称必须为smfile
    response = requests.post(url, files=file, headers=headers)
    print(response.json())
    if not response.json()['success']:
        bugImageUrl = response.json()['images']
    else:
        bugImageUrl = response.json()['data']['url']
    print(bugImageUrl)
    return bugImageUrl


# 钉钉自定义机器人文档地址：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
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
            "title": "未解决BUG列表，请及时处理！",
            "text": '#### **未解决BUG列表，请及时处理！**\n\n'
                    ' >https://jira.shadow.com/issues/?filter=26517\n\n'
                    ' >%s\n\n' % mobiles
                    + '![](' + getBugImageUrl() + ')'
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
    # print(resp.json())
    return resp.json()


if __name__ == '__main__':
    json2Excel()
    html_list = excel2Image.ReportImage.excel_html("data.xlsx", "./")
    excel2Image.ReportImage.html_image(html_list, "./")
    sendMarkdownDing()
```

## 最后图片效果如下

