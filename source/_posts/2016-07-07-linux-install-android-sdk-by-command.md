---
title: Linux下命令行安装配置android-sdk
date: '2016-07-07T00:05:16.000Z'
categories:
  - Linux
tags:
  - sdk
  - linux
---

# 2016-07-07-Linux-install-android-sdk-by-command

1. 首先需要下载android sdk tools only

   ```text
   wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
   tar -zxvf android-sdk_r24.4.1-linux.tgz
   ```

2. 查看可用的SDK组件

   ```text
   android list sdk --all
   ```

3. 下载需要的组件, 注意--all 这个参数一定要加上, 否则后面filter里的序号不起作用

   ```text
   android update sdk -u --all --filter 1,2,3,5
   ```

4. 更新已安装的`SDK`

   ```text
   android update sdk --no-ui
   ```

