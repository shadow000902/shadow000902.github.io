---
title: Telegram代理设置
date: 2019-09-07 23:26:31
categories: [Tips]
tags: [telegram, tips]
---

1. 自身电脑的代理打开全局代理
{% asset_img 全局代理设置.png 全局代理设置 %}

  <!--more-->

2. 设置好全局代理后，查看全局代理情况下，电脑默认设置的socks代理IP和端口
{% asset_img 默认SOCKS代理设置.png 默认SOCKS代理设置 %}

3. 然后设置Telegram的代理
`Settings`-`Advanced`-`Network and proxy`-`Connection type`
{% asset_img 代理设置选择页.png 代理设置选择页 %}
`Use custom proxy`，然后选择`ADD PROXY`，选择`SOCKS5`，填写其中的`Hostname`和`Port`
{% asset_img SOCKS代理设置.png SOCKS代理设置 %}




