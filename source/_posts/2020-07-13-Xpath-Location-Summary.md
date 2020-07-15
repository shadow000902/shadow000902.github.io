---
title: Xpath定位方法总结
date: 2020-07-13 10:21:47
categories: [Tools]
tags: [web, xpath]
---

### 浏览器控制台下，用`Xpath`命令调试
1. 查看元素是否找到，如果有返回一个列表：`$x('xpath路径")][text()="项目总数"]')`
    示例：
    ```xpath
    $x("//*[text()='确认']")
    (4) [span.confirm, span.confirm, span.confirm, span.confirm]
    ```
2. 实现元素点击：`$x('xpath路径")][text()="项目总数"]')[0].click()`
    示例：
    ```xpath
    $x("//*[text()='确认']")[0].click()
    ```
3. 调试模式下的其它元素定位方法
    {% asset_img web控制台命令调试.png web控制台命令调试 %}
    
### 定位路径表达式

表达式|实例|描述
---|---|---
`/`|`xpath('//div')`|路径以`/`开始，表示找到满足绝对路径的元素
`//`||路径以`//`开始，表示找到文档中所有满足`//`后规则的元素，如`//TEXT`表示找到所有`TEXT`元素
`*`||表示所有，如`//*`，表示选择所有元素
[表达式]||进一步限定元素：<br>①[数字]：表示选择第几个，其中[last()]表示最后一个<br>②[@属性]限定满足该属性，如`//TEXT[@name]`表示含有`name`属性的`TEXT`元素；`//TEXT[not(@*)]`表示所有没有属性的`TEXT`元素；<br>③`/TEXT[@name="text"]`表示所有含有name属性且其值为`text`的`TEXT`元素
&#124;||逻辑或，将多个路径合并到一起，如`//BBB` &#124; `/AAA` 选择所有BBB元素和根元素AAA；可合并的路径数目没有限制|

### `Xpath`定位方法

1. 绝对路径定位
就是从根部开始找，一级一级往下走，如果有同级别的需要用[]标明序号，从1开始
```xpath
// CSDN博客的博主头像
//*[@id="csdn_container_tool"]/div/ul/li[6]/div[1]/a/img
// CSDN博客的CSDNlogo
//*[@id="nav-left-menu"]/li[1]/a/img

// CSDN博客的搜索框的两种xpath定位方法
//*[@id="toolber-keyword"]
/html/body/div[4]/div/ul/div/input
```
   
2. 相对路径定位
```xpath
/html/body/div[1]/div[2]/div[1]/div[1]/form/span[1]/input
```
以下都以定位到`input`做说明。

2.1 元素本身查找（@表示属性）
```xpath
//input[@id="kw"]
//*[@id="kw"]
//*[@type="text"]
```
`//input`表示匹配`input`标签的所有元素
`//*`表示匹配所有元素的标签

2.2 布尔值写法
如果`input`标签中，`id`不是唯一的，`type`也不是唯一的，但在该页面中包含该`id`和`type`的只有这个元素时，就可以用组合的方式定位
```xpath
//*[@id="kw" and @type="text"]
//*[@id="kw" or @type="text"]
```

2.3 找父级
如果自己没有唯一的标志，那么就找自己的上级（父级），或者上级的上级，以此类推。
```xpath
//找父级
//span[@class="s_ipt_w"]/input
//找父级的父级
//form[@id="form"]/span[1]/input
```

2.4 跳级
如果需要定位的元素在该页面不是唯一，但在某个容器内是唯一的，当然那个容器必须要有唯一的标志；
该方法要保证在某容器内该元素是唯一的。
```xpath
//div[@id="wrapper"]//input[@id="kw"]
```

3. `Xpath`函数过滤
3.1 `contains()`
```xpath
//div[contains(@id,'in')]
```
表示选择`id`中包含有`in`的`div`节点

3.2 `text()`
```xpath
//a[text()='baidu']
```
由于一个节点的文本值不属于属性，比如`<a class="baidu" herf="http://www.baidu.com">baidu</a>`，所以用`text()`函数来匹配节点

3.3 `last()`
表示取列表的最后一个

3.4 `start-with()`
```xpath
//div[starts-with(@id,'in')]
```
表示选择以`in`开头的`id`属性的`div`节点

3.5 `not()`函数
```xpath
//input[@name='identity' and not(contains(@class, 'a'))]
```
表示匹配出`name`为`identity`，并且`class`的值中不包含a的`input`节点；
not()函数通常与返回值为`true or false`的函数组合使用，比如`contains()`，`starts-with()`等；
有一种特殊情况需要注意：要匹配出`input`节点下所有的`id`属性`//input[@id]`，要匹配出`input`节点下不含有`id`属性`//input[not(@id)]`

4. 轴&步
轴可定义相对于当前节点的节点集。

轴名称|结果
---|---
ancestor|选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self|选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute|选取当前节点的所有属性。
child|选取当前节点的所有子元素。
descendant|选取当前节点的所有后代元素（子、孙等）。
descendant-or-self|选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following|选取文档中当前节点的结束标签之后的所有节点。
namespace|选取当前节点的所有命名空间节点。
parent|选取当前节点的父节点。
preceding|选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling|选取当前节点之前的所有同级节点。
self|选取当前节点。

语法：`轴名称::节点测试[谓语]`

实例

例子|结果
---|---
child::book|选取所有属于当前节点的子元素的 book 节点。
attribute::lang|选取当前节点的 lang 属性。
child::*|选取当前节点的所有子元素。
attribute::*|选取当前节点的所有属性。
child::text()|选取当前节点的所有文本子节点。
child::node()|选取当前节点的所有子节点。
descendant::book|选取当前节点的所有 book 后代。
ancestor::book|选择当前节点的所有 book 先辈。
ancestor-or-self::book|选取当前节点的所有 book 先辈以及当前节点（如果此节点是 book 节点）
child::*/child::price|选取当前节点的所有 price 孙节点。