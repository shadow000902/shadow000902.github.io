---
title: Tomcat使用小技巧
date: '2019-03-22T09:54:35.000Z'
categories:
  - Tomcat
tags:
  - tomcat
---

# 2019-03-22-tomcat-useing-tips

1. 设置 tomcat 启动后的占用内存大小

   ```bash
    # vim /tomcats/bin/catalina.sh
    # 修改配置参数，大约是第251行：原始：JAVA_OPTS="$JAVA_OPTS $JSSE_OPTS"
    # 修改为：
    # 其中的数值可以根据需要修改
    JAVA_OPTS="$JAVA_OPTS $JSSE_OPTS -Xms200m -Xmx200m"
   ```

2. 脚本新建新的 tomcat 目录

   \`\`\`bash

   **执行脚本：**

   **./new\_server.sh server\_tomcat git\_repo nu**

server\_tomcat=$1 \# server\_tomcat 比如：12001\_topgear-test git\_repo=$2 \# git\_repo 比如：topgear nu=$3 \# nu 比如：01

tar -xvf apache-tomcat-9.0.4.tar.gz mv apache-tomcat-9.0.4 ${server\_tomcat} cp 12001\_topgear-test/deploy.sh ${server\_tomcat} cp 12001\_topgear-test/conf/server.xml ${server\_tomcat}/conf/server.xml

## 使用sed命令时，如果

sed -ig "s/11001/110${nu}/g" ./${server\_tomcat}/conf/server.xml sed -ig "s/12001/120${nu}/g" ./${server\_tomcat}/conf/server.xml sed -ig "s/13001/130${nu}/g" ./${server\_tomcat}/conf/server.xml sed -ig "s/14001/140${nu}/g" ./${server\_tomcat}/conf/server.xml sed -ig "s/15001/150${nu}/g" ./${server\_tomcat}/conf/server.xml

sed -ig "s/topgear\"/${git\_repo}\"/g" ./${server\_tomcat}/deploy.sh sed -ig "s/12001\_topgear-test/${server\_tomcat}/g" ./${server\_tomcat}/deploy.sh sed -ig "s/topgear-web/${git\_repo}-web/g" ./${server\_tomcat}/deploy.sh sed -ig 's/mvn config:load/\# mvn config:load/g' ./${server\_tomcat}/deploy.sh

``` Sed后面的表达式一般用单引号引起来``'`，当需要使用**变量**时就换用双引号`"\`\`。

3.

