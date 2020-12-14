---
title: JIRA常用的API使用介绍
date: 2020-12-03 19:24:12
categories: [Jira]
tags: [jira, api]
---

### 获取Issue详情
接口名：`https://jira.shadow.com/rest/api/2/issue/{issueIdOrKey}`

  <!--more-->

#### 接口介绍
Returns a full representation of the issue for the given issue key.
An issue JSON consists of the issue key, a collection of fields, a link to the workflow transition sub-resource, and (optionally) the HTML rendered values of any fields that support it (e.g. if wiki syntax is enabled for the description or comments).

The fields param (which can be specified multiple times) gives a comma-separated list of fields to include in the response. This can be used to retrieve a subset of fields. A particular field can be excluded by prefixing it with a minus.

By default, all (*all) fields are returned in this get-issue resource. Note: the default is different when doing a jql search -- the default there is just navigable fields (*navigable).

  - *all - include all fields
  - *navigable - include just navigable fields
  - summary,comment - include just the summary and comments
  - -comment - include everything except comments (the default is *all for get-issue)
  - *all,-comment - include everything except comments

The {@code properties} param is similar to {@code fields} and specifies a comma-separated list of issue properties to include. Unlike {@code fields}, properties are not included by default. To include them all send {@code ?properties=*all}. You can also include only specified properties or exclude some properties with a minus (-) sign.

  - {@code *all} - include all properties
  - {@code *all, -prop1} - include all properties except {@code prop1}
  - {@code prop1, prop1} - include {@code prop1} and {@code prop2} properties

JIRA will attempt to identify the issue by the issueIdOrKey path parameter. This can be an issue id, or an issue key. If the issue cannot be found via an exact match, JIRA will also look for the issue in a case-insensitive way, or by looking to see if the issue was moved. In either of these cases, the request will proceed as normal (a 302 or other redirect will not be returned). The issue key contained in the response will indicate the current value of issue's key.

The expand param is used to include, hidden by default, parts of response. This can be used to include:

  - renderedFields - field values in HTML format
  - names - display name of each field
  - schema - schema for each field which describes a type of the field
  - transitions - all possible transitions for the given issue
  - operations - all possibles operations which may be applied on issue
  - editmeta - information about how each field may be edited. It contains field's schema as well.
  - changelog - history of all changes of the given issue
  - versionedRepresentations - REST representations of all fields. Some field may contain more recent versions. RESET representations are numbered. The greatest number always represents the most recent version. It is recommended that the most recent version is used. version for these fields which provide a more recent REST representation. After including versionedRepresentations "fields" field become hidden.

#### Request Options

Parameter|Value|Type|Style|Description
---|---|---|---|---
issueIdOrKey*| |string|template|the issue id or key to update (i.e. JRA-1330)
fields| |string|query|the list of fields to return for the issue. By default, all fields are returned.
expand| |string|query| 
properties| |string|query|the list of properties to return for the issue. By default no properties are returned.
updateHistory| |boolean|query|

#### 常用参数说明
主要说明`expand`字段
  - changelog  - 填写参数为`changelog`时，对应这个接口获取到的数据为`JIRA`的`Issue详情页`的`活动日志-改动记录`

#### 返回结果示例
```json
{
  "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",
  "id": "236714",
  "self": "https://jira.shadow.com/rest/api/2/issue/236714",
  "key": "SHADOW-123123",
  "fields": {
    "summary": "测试JIRA单子状态活动日志-改动记录"
  },
  "changelog": {
    "startAt": 0,
    "maxResults": 4,
    "total": 4,
    "histories": [
      {
        "id": "1126652",
        "author": {
          "self": "https://jira.shadow.com/rest/api/2/user?username=shadow",
          "name": "shadow",
          "key": "shadow",
          "emailAddress": "shadow@shadow.com",
          "avatarUrls": {
            "48x48": "https://jira.shadow.com/secure/useravatar?ownerId=shadow&avatarId=11436",
            "24x24": "https://jira.shadow.com/secure/useravatar?size=small&ownerId=shadow&avatarId=11436",
            "16x16": "https://jira.shadow.com/secure/useravatar?size=xsmall&ownerId=shadow&avatarId=11436",
            "32x32": "https://jira.shadow.com/secure/useravatar?size=medium&ownerId=shadow&avatarId=11436"
          },
          "displayName": "shadow",
          "active": true,
          "timeZone": "Asia/Shanghai"
        },
        "created": "2020-04-01T17:01:33.000+0800",
        "items": [
          {
            "field": "status",
            "fieldtype": "jira",
            "from": "1",
            "fromString": "待受理",
            "to": "10207",
            "toString": "待办事项"
          }
        ]
      },
      {
        "id": "1126653",
        "author": {
          "self": "https://jira.shadow.com/rest/api/2/user?username=shadow",
          "name": "shadow",
          "key": "shadow",
          "emailAddress": "shadow@shadow.com",
          "avatarUrls": {
            "48x48": "https://jira.shadow.com/secure/useravatar?ownerId=shadow&avatarId=11436",
            "24x24": "https://jira.shadow.com/secure/useravatar?size=small&ownerId=shadow&avatarId=11436",
            "16x16": "https://jira.shadow.com/secure/useravatar?size=xsmall&ownerId=shadow&avatarId=11436",
            "32x32": "https://jira.shadow.com/secure/useravatar?size=medium&ownerId=shadow&avatarId=11436"
          },
          "displayName": "shadow",
          "active": true,
          "timeZone": "Asia/Shanghai"
        },
        "created": "2020-04-01T17:01:36.000+0800",
        "items": [
          {
            "field": "status",
            "fieldtype": "jira",
            "from": "10207",
            "fromString": "待办事项",
            "to": "11404",
            "toString": "开发开始"
          }
        ]
      },
      {
        "id": "1126661",
        "author": {
          "self": "https://jira.shadow.com/rest/api/2/user?username=shadow",
          "name": "shadow",
          "key": "shadow",
          "emailAddress": "shadow@shadow.com",
          "avatarUrls": {
            "48x48": "https://jira.shadow.com/secure/useravatar?ownerId=shadow&avatarId=11436",
            "24x24": "https://jira.shadow.com/secure/useravatar?size=small&ownerId=shadow&avatarId=11436",
            "16x16": "https://jira.shadow.com/secure/useravatar?size=xsmall&ownerId=shadow&avatarId=11436",
            "32x32": "https://jira.shadow.com/secure/useravatar?size=medium&ownerId=shadow&avatarId=11436"
          },
          "displayName": "shadow",
          "active": true,
          "timeZone": "Asia/Shanghai"
        },
        "created": "2020-04-01T17:02:18.000+0800",
        "items": [
          {
            "field": "status",
            "fieldtype": "jira",
            "from": "11404",
            "fromString": "开发开始",
            "to": "11201",
            "toString": "开发结束"
          },
          {
            "field": "完工方案",
            "fieldtype": "custom",
            "from": null,
            "fromString": null,
            "to": null,
            "toString": "判断，如果客户没有收整车款，也可以继续开票"
          }
        ]
      },
      {
        "id": "1126662",
        "author": {
          "self": "https://jira.shadow.com/rest/api/2/user?username=shadow",
          "name": "shadow",
          "key": "shadow",
          "emailAddress": "shadow@shadow.com",
          "avatarUrls": {
            "48x48": "https://jira.shadow.com/secure/useravatar?ownerId=shadow&avatarId=11436",
            "24x24": "https://jira.shadow.com/secure/useravatar?size=small&ownerId=shadow&avatarId=11436",
            "16x16": "https://jira.shadow.com/secure/useravatar?size=xsmall&ownerId=shadow&avatarId=11436",
            "32x32": "https://jira.shadow.com/secure/useravatar?size=medium&ownerId=shadow&avatarId=11436"
          },
          "displayName": "shadow",
          "active": true,
          "timeZone": "Asia/Shanghai"
        },
        "created": "2020-04-01T17:02:25.000+0800",
        "items": [
          {
            "field": "WorklogId",
            "fieldtype": "jira",
            "from": "30777",
            "fromString": "30777",
            "to": null,
            "toString": null
          },
          {
            "field": "timeestimate",
            "fieldtype": "jira",
            "from": null,
            "fromString": null,
            "to": "0",
            "toString": "0"
          },
          {
            "field": "timespent",
            "fieldtype": "jira",
            "from": null,
            "fromString": null,
            "to": "7200",
            "toString": "7200"
          }
        ]
      }
    ]
  }
}
```

### 使用JQL时间段精确搜索
示例：`project = CARSERVICE AND issuetype = 缺陷 AND priority in (P0, P1) AND createdDate >= "2020-11-20 01:00" AND createdDate <= "2020-11-20 11:08" ORDER BY created DESC`
用于时间段精确搜索的字段`key`叫`createDate`（创建时间精确搜索），用于更新时间精确搜索的字段`key`叫`updatedDate`。
其中`createDate`或者`updatedDate`，正确的日期格式是：`yyyy/MM/dd HH:mm`，`yyyy-MM-dd HH:mm`，`yyyy/MM/dd`，`yyyy-MM-dd`，或者是一个时间段`-5d`，`4w 2d`。

### 获取Issue的备注详情列表
接口名：`https://jira.shadow.com/rest/api/2/issue/{issueIdOrKey}/comment`

#### 接口介绍
Returns all comments for an issue.
Results can be ordered by the "created" field which means the date a comment was added.

#### Request Options

Parameter|Value|Type|Style|Description
---|---|---|---|---
issueIdOrKey*| |string|template|to get comments for
startAt| |long|query|the page offset, if not specified then defaults to 0
maxResults| |int|query|how many results on the page should be included. Defaults to 50.
orderBy| |string|query|ordering of the results.
expand| |string|query|optional flags: renderedBody (provides body rendered in HTML)


### 获取筛选器详情
接口名：`https://jira.shadow.com/rest/api/2/filter/{id}`

#### 接口介绍
Returns a filter given an id
从`Response`中可以拿到筛选器对应的`JQL`条件

#### Request Options

Parameter|Value|Type|Style|Description
---|---|---|---|---
id*| |long|template|the id of the filter being looked up
expand| |string|query|the parameters to expand


### 获取Issue的列表
接口名：`https://jira.shadow.com/rest/api/2/search`

#### 接口介绍
Searches for issues using JQL.
**Sorting** the jql parameter is a full JQL expression, and includes an ORDER BY clause.

The fields param (which can be specified multiple times) gives a comma-separated list of fields to include in the response. This can be used to retrieve a subset of fields. A particular field can be excluded by prefixing it with a minus.

By default, only navigable (*navigable) fields are returned in this search resource. Note: the default is different in the get-issue resource -- the default there all fields (*all).

  - *all - include all fields
  - *navigable - include just navigable fields
  - summary,comment - include just the summary and comments
  - -description - include navigable fields except the description (the default is *navigable for search)
  - *all,-comment - include everything except comments
**GET vs POST**: If the JQL query is too large to be encoded as a query param you should instead POST to this resource.

**Expanding Issues in the Search Result**: It is possible to expand the issues returned by directly specifying the expansion on the expand parameter passed in to this resources.

For instance, to expand the "changelog" for all the issues on the search result, it is neccesary to specify "changelog" as one of the values to expand.

#### Request Options

Parameter|Value|Type|Style|Description
---|---|---|---|---
jql| |string|query|a JQL query string
startAt| |int|query|the index of the first issue to return (0-based)
maxResults| |int|query|the maximum number of issues to return (defaults to 50). The maximum allowable value is dictated by the JIRA property 'jira.search.views.default.max'. If you specify a value that is higher than this number, your search results will be truncated.
validateQuery| |boolean|query|whether to validate the JQL query
fields| |string|query|the list of fields to return for each issue. By default, all navigable fields are returned.
expand| |string|query|A comma-separated list of the parameters to expand.


### 模糊搜索，获取自定义字段的相关信息
接口名：`https://jira.shadow.com/rest/api/2/customFields`

#### Request Options

Parameter|Value|Type|Style|Description
---|---|---|---|---
startAt| |long|query|
maxResults| |int|query|
search| |string|query|

#### 返回结果示例
```json
{
  "maxResults": 50,
  "startAt": 0,
  "total": 1,
  "isLast": true,
  "values": [
    {
      "id": "customfield_17601",
      "name": "端",
      "description": "<p>标记Issue是在哪个端上被发现的</p>",
      "type": "选择列表 (级联)",
      "searcherKey": "端",
      "self": "https://jira.souche-inc.com/rest/api/2/customFields/customfield_17601",
      "numericId": 17601,
      "isLocked": false,
      "isManaged": false,
      "isAllProjects": false,
      "projectsCount": 8,
      "screensCount": 1
    }
  ]
}
```
