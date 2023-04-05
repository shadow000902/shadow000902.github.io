---
title: Mac电脑使用总结
date: 2021-01-05 11:38:33
categories: [Tips]
tags: [mac]
---

## 浏览器使用总结

### &emsp;标签页快捷键

1. Chrome浏览器，超链接点击后，在新的标签页打开，且切换到新的标签页
    **快捷键**：`COMMAND + SHIFT + 鼠标左键点击超链接`
    **适用场景**：不想页面跳转，又想立马看到超链接页面的内容

  <!--more-->

2. Chrome浏览器，超链接点击后，在新的窗口打开，且切换到新的窗口
    **快捷键**：`SHIFT + 鼠标左键点击超链接`
    **适用场景**：已经打开多个标签了，再在同一窗口打开标签会造成切换标签不便时

3. Chrome浏览器，超链接点击后，在新的标签页打开，且停留在当前标签页
    **快捷键**：`COMMAND + 鼠标左键点击超链接`
    **适用场景**：需要快速查看单页面内的多个内部跳转的页面，又不想要每次查看再返回

### &emsp;好用的浏览器插件

1. 请求头管理插件`ModHeader`
    插件下载地址：[https://bewisse.com/modheader/](https://bewisse.com/modheader/)

2. 浏览器代理切换工具`SwitchyOmega`
    插件下载地址：[https://github.com/FelisCatus/SwitchyOmega/releases](https://github.com/FelisCatus/SwitchyOmega/releases)

3. Web开发者助手`FeHelper`
    插件下载地址：[https://www.baidufe.com/fehelper/index/index.html](https://www.baidufe.com/fehelper/index/index.html)
    插件常用功能列表：
      - JSON美化工具
      - 时间(戳)转换
      - 随机密码生成
      - 颜色转换工具
      - 二维码/解码
      - JSON对比工具
      - 等等

4. 浏览器黑暗模式`DACK READER`
    插件下载地址：[https://darkreader.org/](https://darkreader.org/)

5. 网页翻译工具`彩云小译`
    插件下载地址：[https://fanyi.caiyunapp.com/#/web](https://fanyi.caiyunapp.com/#/web)
    **整篇文章，根据段落进行翻译，中文在英文下展示，即直观有方便**

6. 网页json格式化工具`JSON Formatter`
    插件下载地址：[https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa)
    浏览器请求返回的JSON结果，会自动格式化后进行可视化展示

## Mac系统使用总结

### &emsp;升级系统后，截图软件无法使用

问题可能原因：因为系统升级原因，`/Library/Application\ Support/com.apple.TCC`目录中的文件，损坏或权限异常
导致在`系统偏好设置-安全性与隐私-隐私-屏幕录制`中，无法添加软件，从而无法进行截图和录屏。
解决方案：删除`/Library/Application\ Support/com.apple.TCC`目录中的`TCC.db`文件，然后重启系统
然后重新在`系统偏好设置-安全性与隐私-隐私-屏幕录制`中添加软件，就可以看到对应软件被添加到了列表中
