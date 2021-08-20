---
title: Linux下压缩&解压缩命令详解
date: 2016-07-07 00:52:04
categories: [Linux]
tags: [linux]
---

1. zip&unzip
```
zip -r filename.zip dirname               # 压缩mydata文件夹到mydata.zip
unzip filename.zip -d dirname             # 把mydata.zip解压到mydatabak文件夹中
```

  <!--more-->

2. tar
```
tar -zxvf filename.tar                    # 解压到当前目录
tar -zxvf filename.tgz                    # 解压到当前目录
tar -czvf filename.tar dirname            # 目录文件夹dirname的内容打包到filename.tar
tar -zcvf filename.tar.gz dirname         # 目录文件夹dirname的内容打包到filename.tar.gz
tar -zcvf filename.tar.gz dirname1 dirname2 dirname3 .....      # 打包多个文件及文件夹到filename.tar.gz
```

3. XXX.tar.xz
```
xz -d XXX.tar.xz
tar xvf XXX.tar
```

4. XXX.tgz & XXX.tar.gz
```
gunzip XXX.tgz
tar xvf XXX.tar
or
tar xvf XXX.tar.gz
```
