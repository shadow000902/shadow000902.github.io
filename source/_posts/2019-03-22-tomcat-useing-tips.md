---
title: Tomcat使用小技巧
date: 2019-03-22 09:54:35
categories: [Tomcat]
tags: [tomcat]
---

1. 设置 tomcat 启动后的占用内存大小
    ```bash
    # vim /tomcats/bin/catalina.sh
    # 添加配置参数
    JAVA_OPTS='-Xms256m -Xmx400m'
    ```
    
2. 脚本新建新的 tomcat 目录
```bash
# 执行脚本：
# ./new_server.sh server_tomcat git_repo nu

server_tomcat=$1    # server_tomcat 比如：12001_topgear-test
git_repo=$2         # git_repo 比如：topgear
nu=$3               # nu 比如：01

tar -xvf apache-tomcat-9.0.4.tar.gz
mv apache-tomcat-9.0.4 ${server_tomcat}
cp 12001_topgear-test/deploy.sh ${server_tomcat}
cp 12001_topgear-test/conf/server.xml ${server_tomcat}/conf/server.xml

# 使用sed命令时，如果
sed -ig "s/11001/110${nu}/g" ./${server_tomcat}/conf/server.xml
sed -ig "s/12001/120${nu}/g" ./${server_tomcat}/conf/server.xml
sed -ig "s/13001/130${nu}/g" ./${server_tomcat}/conf/server.xml
sed -ig "s/14001/140${nu}/g" ./${server_tomcat}/conf/server.xml
sed -ig "s/15001/150${nu}/g" ./${server_tomcat}/conf/server.xml

sed -ig "s/topgear\"/${git_repo}\"/g" ./${server_tomcat}/deploy.sh
sed -ig "s/12001_topgear-test/${server_tomcat}/g" ./${server_tomcat}/deploy.sh
sed -ig "s/topgear-web/${git_repo}-web/g" ./${server_tomcat}/deploy.sh
sed -ig 's/mvn config:load/# mvn config:load/g' ./${server_tomcat}/deploy.sh
```
Sed后面的表达式一般用单引号引起来``'``，当需要使用**变量**时就换用双引号``"``。

3. 