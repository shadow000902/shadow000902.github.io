---
title: JIRA使用小结
date: 2018-11-27 19:36:30
categories: [Jira]
tags: [jira]
---
### 问题类型
#### 问题类型
列表包含系统中所有的问题`类型`，也可以新增问题`类型`

#### 问题类型方案
`问题类型方案`用于确定哪些`问题类型`将提供给`一组项目`。它还允许指定的顺序介绍用户界面的问题类型。

  <!--more-->

#### 子任务

### 工作流
#### 工作流
作用于单个流程，比如缺陷流程、需求流程


#### 工作流方案
作用于整个项目，一个`工作流方案`，是包含项目中所有的包括缺陷工作流、需求工作流等多个工作流的一个集合。


### 界面配置
#### 创建一个`界面`
`界面`是对字段的排列布局，是`创建问题`、`编辑问题`或`执行工作流`过程时显示的页面。
  - 要选择 `创建` or `编辑`问题时显示的界面，请利用`界面方案`将其挂接到问题操作功能中 。
  - 为特定工作流过渡选择显示屏幕，请选择所属`工作流`过渡并编辑它。
注意: 只能删除没有应用到`界面方案`以及没有关联到`工作流`的`界面`。

#### `界面`添加字段值
`界面`添加完成后，点击`配置`，进入字段值`添加/编辑`页面
通用配置字段如下：

|Field|Type|
|---|---|
|问题类型|系统域|
|主题|系统域|
|模块|系统域|
|描述|系统域|
|优先级|系统域|
|处理优先级|选择列表（单选）|
|报告人|系统域|
|经办人|系统域|
|解决版本|系统域|
|标签|系统域|
|关注人|选择用户（多选）|
|附件|系统域|

#### 创建一个`界面方案`
创建`界面方案`时，需要选择一个`默认界面`，选择前面创建的`界面`。
`页面方案`允许您为每个问题操作选择相应的页面。 `界面方案`被`问题类型界面方案`映射到问题类型上 , 再关联到项目上。
注意: 只能删除在`问题类型界面方案`中没有使用的`界面方案`。

#### 创建一个`问题类型界面方案`
创建`问题类型界面方案`时，需要选择一个`界面方案`，选择前面创建的`界面方案`。
`问题类型页面方案`允许您选择哪个 `页面方案` 应用于指定的问题类型。然后, 问题类型的屏幕计划可以关联到某个或多个项目, 可以指定屏幕上的是什么计划, 因此什么为的屏幕应用于某一具体问题的操作的项目” 的问题。
注意: 你无法删除已经关联项目的`问题类型界面方案`。

### 字段
#### 自定义字段生效步骤
1. 添加字段，字段类型可以根据需要自己选择
2. 如果是枚举类型字段，进入字段配置页面，设置对应的枚举值
3. 如果字段只希望在个别项目中使用的，进入字段配置界面，配置字段适用的问题类型和项目
4. 在创建BUG、查看BUG的界面中，增加该字段


#### 字段配置
这里的`字段配置`指的是一套字段的所有配置的合集
`字段配置`用于规划字段的状态，告诉`JIRA`如何控制字段。例如，可以在`字段配置`中设置所有输入或查看页面隐藏一个字段, 或决定一个字段在编辑时是`必选项`。`字段配置`只有应用于 `字段配置方案`, 并且将方案关联到项目中时才会生效。

#### 设置`字段配置`配置项的值
`字段配置`列表中的某一个配置，点击`配置`，进入具体字段列表，每个字段的配置项都一致，主要包括`隐藏/显示`、`必选项/可选择的`

#### 字段配置方案
`字段配置方案`将 `字段配置`映射到`问题类型`上。 `字段配置方案`可以关联到多个项目，项目中的问题通过`字段配置`与`问题类型`的映射关系，而显示不同的字段。
编辑`字段配置方案`，选择前面创建的`字段配置`。

### 修改项目各项配置
如果需要修改项目的配置，需要进入到`该项目`的`项目设置`中

#### 修改项目的`问题类型`
`行为`-`使用不同的方案`，选择在`问题类型方案`中创建的类型

#### 修改项目的`工作流`

### 基础插件使用
#### 修改`状态`的时候，同步修改`解决结果`
在从状态A转换到状态B的操作上，添加`后处理功能`，选择`更新问题字段`，然后选择需要更新的问题字段
{% asset_img 更新问题字段.png 更新问题字段 %}

### 插件及其应用
#### `scriptrunner`
该插件可用作jira工作流的一个验证器，用于在工作流转换时，增加额外的操作，比如如下功能：
1. 在状态转换时，设置必填`备注`
    1.1 编辑工作流，选中需要修改的转换标线，点击`验证器`，进入验证器的添加页面
    1.2 点击`添加验证器`，进入验证器添加页面
    {% asset_img 状态转换加ScriptValidator【ScriptRunner】.png 状态转换加ScriptValidator【ScriptRunner】 %}
    1.3 为Validator添加状态转换参数
    {% asset_img 为Validator添加参数.png 为Validator添加参数 %}
    1.4 最后在添加一个转换说明
    {% asset_img 对转换操作添加说明.png 对转换操作添加说明 %}
    1.5 添加成功后如图所示
    {% asset_img 验证器添加成功后.png 验证器添加成功后 %}

    到这里算是完成了80%，在对`BUG`进行`FIXED`操作是，还是可能会出现`没有弹窗`的情况，这种情况主要是对转换操作没有设置界面，导致没有界面可以弹出来
    所以需要最后一步操作，就是对转换动作添加`界面`：
    {% asset_img 对转换操作添加界面.png 对转换操作添加界面 %}

2. 在转换状态时，可以添加脚本方式去设置执行自己想要做的事情
    添加方式如图：
    {% asset_img 添加自定义脚本参数.png 添加自定义脚本参数 %}
    {% asset_img 编写脚本项.png 编写脚本项 %}

3. `Script-Fields`使用
    依次进入：`设置`-`管理应用`-`Script Fields`，点击`Create Script Field`按钮，再点击`Custom Script Field`
    {% asset_img Create-Script-Field.png Create-Script-Field %}
    {% asset_img Custom-Script-Field.png Custom-Script-Field %}

    示例1：获取最后变更到某个状态的时间

    代码如下：
    ```groovy
    package com.onresolve.jira.groovy.test.scriptfields.scripts
    
    import com.atlassian.jira.component.ComponentAccessor
    
    def changeHistoryManager = ComponentAccessor.getChangeHistoryManager()
    def created = changeHistoryManager.getChangeItemsForField(issue, "status").sort { a, b -> a.created == b.created ? 0 : a.created > b.created ? -1 : 1 }.find {
        it.to == "12300" 
    }?.getCreated()
    
    def createdTime = created?.getTime()
    
    createdTime ? new Date(createdTime) : null
    ```
    
    其中设置的`12300`即为目标状态的`statusId`，执行结果会返回一个最后变更到这个状态的时间，返回的格式由上面设置的`Template`字段格式来确定
    {% asset_img Template使用默认的Text-Field返回的结果.png Template使用默认的Text-Field返回的结果 %}

    或者在`Template`字段依旧选择`Text Field(multi-line)`，然后再脚本中格式化日期为一下格式
    ```groovy
    package com.onresolve.jira.groovy.test.scriptfields.scripts
    
    import com.atlassian.jira.component.ComponentAccessor
    import com.atlassian.jira.datetime.DateTimeFormatter
    def changeHistoryManager = ComponentAccessor.getChangeHistoryManager()
    def created = changeHistoryManager.getChangeItemsForField(issue, "status").sort { a, b -> a.created == b.created ? 0 : a.created > b.created ? -1 : 1 }.find {
        it.to == "12300" 
    }?.getCreated()
    
    def createdTime = created?.getTime()
    DateTimeFormatter dateTimeFormatter = ComponentAccessor.getComponent(DateTimeFormatter.class);
    createdTime?dateTimeFormatter.withStyle(com.atlassian.jira.datetime.DateTimeStyle.DATE_TIME_PICKER).format(new Date(createdTime)):null
    ```
    {% asset_img Template使用默认的Date-Time返回的结果.png Template使用默认的Date-Time返回的结果 %}

    示例2：获取在某个状态停留的时长
    ```groovy
    import com.atlassian.jira.component.ComponentAccessor
    import com.atlassian.jira.issue.history.ChangeItemBean
    
    def changeHistoryManager = ComponentAccessor.getChangeHistoryManager()
    
    def inProgressName = "实施中"
    
    List<Long> rt = [0L]
    def changeItems = changeHistoryManager.getChangeItemsForField(issue, "status")
    changeItems.reverse().each { ChangeItemBean item ->
        def timeDiff = System.currentTimeMillis() - item.created.getTime()
        if (item.fromString == inProgressName) {
            rt << -timeDiff
        }
        if (item.toString == inProgressName) {
            rt << timeDiff
        }
    }
    
    def total = rt.sum() as Long
    return (total/1000/60/60/24) as long ?: 0L
    ```
    其中设置的`实施中`即为停留状态的名称，最后返回的`total`是一个单位为`毫秒`的时间，`return`结果可以根据需要进行调整
    
    示例2扩展：获取多个状态下停留时长的总和
    ```groovy
    import com.atlassian.jira.component.ComponentAccessor
    import com.atlassian.jira.issue.history.ChangeItemBean
    
    def changeHistoryManager = ComponentAccessor.getChangeHistoryManager()
    
    def inProgressName1 = "开发开始"
    def inProgressName2 = "开发结束"
    
    List<Long> rt1 = [0L]
    List<Long> rt2 = [0L]
    def changeItems = changeHistoryManager.getChangeItemsForField(issue, "status")
    changeItems.reverse().each { ChangeItemBean item ->
        def timeDiff = System.currentTimeMillis() - item.created.getTime()
        if (item.fromString == inProgressName1) {
            rt1 << -timeDiff
        }
        if (item.toString == inProgressName1) {
            rt1 << timeDiff
        }
        if (item.fromString == inProgressName2) {
            rt2 << -timeDiff
        }
        if (item.toString == inProgressName2) {
            rt2 << timeDiff
        }
    }
    
    def total1 = rt1.sum() as Long
    def total2 = rt2.sum() as Long
    
    return ((total1+total2)/1000/60/60/24) as long ?: 0L
    ```
   
   结果取绝对值，并保留两位小数
   ```groovy
    def total1 = rt1.sum() as float
    def total2 = rt2.sum() as float
        
    def total = Math.round(Math.abs((total1+total2)/1000/60/60/24)*100)/100
    
    return total ?: 0L
    ```
   
    以上获取时间段的方式，如果是取单个状态的时间段，可能会存在不准确的情况，建议使用时间点相减的方式来进行获取，代码如下：
    ```groovy
    package com.onresolve.jira.groovy.test.scriptfields.scripts
    
    import com.atlassian.jira.component.ComponentAccessor
    import com.atlassian.jira.datetime.DateTimeFormatter
    
    def changeHistoryManager = ComponentAccessor.getChangeHistoryManager()
    def start = changeHistoryManager.getChangeItemsForField(issue, "status").sort { a, b ->
        a.created == b.created ? 0
                : a.created > b.created ? -1 : 1
    }.find {
        it.to == "13302"
    }?.getCreated()
    
    def finish = changeHistoryManager.getChangeItemsForField(issue, "status").sort { a, b ->
        a.created == b.created ? 0
                : a.created > b.created ? -1 : 1
    }.find {
        it.to == "13027"
    }?.getCreated()
    
    def closed = changeHistoryManager.getChangeItemsForField(issue, "status").sort { a, b ->
        a.created == b.created ? 0
                : a.created > b.created ? -1 : 1
    }.find {
        it.to == "11202"
    }?.getCreated()
    
    
    def startTime
    def finishTime
    def diffTime
    
    if(start){
        startTime = start?.getTime()
        if(finish){
            finishTime = finish?.getTime()
        }else if (finish == null && closed != null){
            finishTime = closed?.getTime()
        }else{
            finishTime = System.currentTimeMillis()
        }
        diffTime = finishTime - startTime as float
    }else{
        diffTime = 0
    }
    
    DateTimeFormatter dateTimeFormatter = ComponentAccessor.getComponent(DateTimeFormatter.class);
    //startTime ? dateTimeFormatter.withStyle(com.atlassian.jira.datetime.DateTimeStyle.DATE_TIME_PICKER).format(new Date(startTime)) : null
    //finishTime ? dateTimeFormatter.withStyle(com.atlassian.jira.datetime.DateTimeStyle.DATE_TIME_PICKER).format(new Date(finishTime)) : null
    
    //return (diffTime / 1000 / 60 / 60 / 24) as float ?: 0L
    
    def total = Math.round((diffTime/1000/60/60/24)*100)/100
    
    return total ?: 0L
    ```

4. 获取项目中的`BUG`被`Reopened`的次数
    依旧是使用`scriptrunner`这个插件中的功能。
    4.1 在`Fields`中选择`Create Script Field`
    {% asset_img 选择「CreateScriptField」.png 选择「CreateScriptField」 %}
    4.2 在列表中选择`No. of Times In Status`
    {% asset_img 选择「No.ofTimesInStatus」.png 选择「No.ofTimesInStatus」 %}
    4.3 选择需要进行统计的状态，如`Reopen`
    {% asset_img 选择「issureStatuses」中的状态.png 选择「issureStatuses」中的状态 %}
    可以在`Preview Issue Key`中填入一个进行过`Reopen`操作的关键字，进行调试
    这里需要注意一点，状态列表里，可能会有比较名称比较接近的状态，你需要确认，在你的项目的工作流里，这个`Reopen`对应的是哪个确切的名称，如果选择里，结果不对，可以自己调试，找到对的
    4.4 到这里获取状态次数的字段创建好了，后面需要应用到项目中
    {% asset_img 在列表选择字段编辑的「ConfigureContext」.png 在列表选择字段编辑的「ConfigureContext」 %}
    从上面这张图可以看到，因为有两个作为`Reopen`的状态，比较粗暴的方法就是都统计上
    4.5 在该字段的`Configure Context`，就可以设置需要应用到的项目了，建议按照需要选择自己的项目，以免影响他人使用
    {% asset_img 选择需要应用的项目.png 选择需要应用的项目.png %}

#### `JSU`
1. `Copy Value From Other Field (JSU)`从其它字段复制值到另一个字段
    实例1：在需求排期时，定义好测试人员字段值为A，然后在流程流转到测试阶段时，自动把经办人修改为测试人员，即自动把经办人修改为A
    {% asset_img 添加后处理功能.png 添加后处理功能 %}
    {% asset_img 配置后处理器.png 配置后处理器 %}
    该后处理器的`Copy Field`有3中方式：

    |function|含义|解释|
    |---|---|---|
    |overwrite|清空并写入|把A字段overwrite到B字段，如果A字段未设置，会把B字段值也置空|
    |append|追加在尾部|把A字段append到B字段：<br>如果A字段未设置，B字段保持不变；<br>如果A字段有值，且和B字段值不一样，设置B字段属性为多用户，则会把A字段的用户添加到B字段值后，即可完成`统计所有经办人`的目的；<br>如果A字段有值，且和B字段值不一样，设置B字段属性为单用户，则会用A字段的用户替换B字段的用户，即完成`修改经办人`；|
    |prepend|追加在开头|和append用法一致，只是往多用户追加的时候，是追加到头部|
    
2. `Fields Required (JSU)`在进行某个操作时，确保某些字段是有值的
    从验证器添加，选择`Fields Required (JSU)`
    {% asset_img FieldsRequired.png FieldsRequired %}
    从`Available fields`中选择字段，添加到右侧的`Required fields`中，作为该次操作的必填参数
    比如希望产品在PRD完成、在和开发测试确认好排期后，在jira流程中填入预计上线时间，这个时候，就可以在产品进行把流转转给开发的这个操作下，新增该验证器，让产品同学必须填入`预计上线时间`，才能让流程往下流转
    