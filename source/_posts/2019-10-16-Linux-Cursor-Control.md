---
title: 2019-10-16-Linux-Cursor-Control
date: 2019-10-16 16:14:16
categories: [Linux]
tags: [linux]
---

1. VIM编辑下，控制光标
```bash
# 命令模式下，移动光标到段位
shift+a
# 命令模式下，移动光标到文尾
shift+g
```

2. MAC下，命令行控制
```bash
ctrl + a            移动到命令行首
ctrl + e            移动到行尾
ctrl + b            光标后退
ctrl + f            光标前进
alt + f             光标前进一个单词
alt + b             光标后退一格单词
ctrl + ]            从当前光标往后搜索字符串，用于快速移动到该字符串
ctrl + alt + ]      从当前光标往前搜索字符串，用于快速移动到该字符串
ctrl + H            删除光标的前一个字符
ctrl + D            删除当前光标所在字符
ctrl + K            删除光标之后所有单词
ctrl + U            删除当前输入的命令
ctrl + w            删除光标钱的单词
ctrl + y            黏贴删除的内容
alt + .             粘贴上一条命令的最后一个参数
```

