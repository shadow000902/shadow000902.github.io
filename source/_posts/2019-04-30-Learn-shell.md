---
title: shell学习笔记
date: 2019-04-30 17:07:00
categories: [Shell]
tags: [shell]
---

##### 命令嵌套【嵌套语句通过 \`\` 来标记】
```bash
for list in \
`find /root/.jenkins/jobs/DEBUG-UZAO-*/ -maxdepth 1 -type f -name config.xml`\
;do sed -i s/$now_branch/$new_branch/g $list\
;done
```

  <!--more-->

##### shell的多行注释
```bash
:<<BLOCK
....注释内容
....注释内容1
BLOCK
```
实际意义：
    `:`：前的内容为空，表示执行空命令
    `<<`：重定向，表示把结果重定向到空命令下
    `BLOAK\nBLOCK`：`BLOCK`只需要成对出现，两个`BLOCK`之间的内容就相当于是被注释掉了
    但是如果需要注释的内容中包含 \` 的话的话就需要在前后字符对的中间加入`''`，把需要注释的内容放在`''`之间
以下方式都能表示多行注释：
```bash
:<<'
....注释内容
....注释内容1
'
```
```bash
:<<'BLOCK
....注释内容
....注释内容1
BLOCK'
```