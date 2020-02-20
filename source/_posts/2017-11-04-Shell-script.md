---
title: Shell小脚本
date: 2017-11-04 15:51:48
categories: [Shell]
tags: [shell]
---

#### 删除目录下的除今天外的所有文件夹

1. 目录下的文件夹规律【年月日时分秒】
```bash
# taoyi @ TaoYi-Mac in ~/Desktop/test0001 [15:54:29] 
$ ll
total 0
drwxr-xr-x  2 taoyi  staff    68B 11  3 18:29 20171027121219
drwxr-xr-x  3 taoyi  staff   102B 11  3 18:30 20171101124273
drwxr-xr-x  3 taoyi  staff   102B 11  3 18:29 20171102124212
drwxr-xr-x  2 taoyi  staff    68B 11  3 18:29 20171103121216
drwxr-xr-x  3 taoyi  staff   102B 11  3 18:29 20171103124211
drwxr-xr-x  2 taoyi  staff    68B 11  3 18:29 20171103124216
drwxr-xr-x  2 taoyi  staff    68B 11  3 18:29 20171104124212
```

  <!--more-->

2. shell脚本
```bash
# 目录下的所有文件夹名称写入文件``dir``
ls -l /Users/taoyi/Desktop/test0001/ | awk '/^d/ {print $NF}' > /Users/taoyi/Desktop/test0001/dir

# `date +%Y%m%d`，获取当天的年月日
for i in $(grep -v `date +%Y%m%d` /Users/taoyi/Desktop/test0001/dir)
do
	# 删除目录下的文件夹
    rm -rf /Users/taoyi/Desktop/test0001/$i
done

# 删除零时写入的文件``dir``
rm -rf /Users/taoyi/Desktop/test0001/dir
```

#### kill指定name的pid

```bash
# kill指定name的pid
# 示例："./kill_pidname.sh jhost"

pid_name=$1
ps -ef | grep -v grep | grep $pid_name | while read username pid other
do
    kill -9 $pid
done
```

#### adb截图导出并展示

```bash
# 调用安卓系统内部截图命令screencap截图保存
adb shell /system/bin/screencap -p /sdcard/screenshot.jpg
# 导出图片到本地目录
adb pull /sdcard/screenshot.jpg ~/shell-tools/ScreenShots/
# 打开图片
open ~/shell-tools/ScreenShots/screenshot.jpg
```

#### android打包并安装

```bash
cd /Users/taoyi/git_projects/Gitlab/androidclientnative/
git checkout develop
git pull

rm -rf /Users/taoyi/git_projects/Gitlab/androidclientnative/app/build/
rm -rf /Users/taoyi/shell-tools/APK/*.apk

gradle clean assembleFengcheBeta
# gradle clean assembleFengchePreview
# gradle clean assembleFengcheRelease

cp -rf /Users/taoyi/git_projects/Gitlab/androidclientnative/app/build/outputs/apk/beta/*.apk /Users/taoyi/shell-tools/APK/
adb uninstall com.souche.fengche
adb install /Users/taoyi/shell-tools/APK/*.apk
```

#### Shell脚本解析xml文件字段

示例文件内容``build.xml``
```xml
  <parameters>
    <hudson.model.StringParameterValue>
      <name>SCHEME</name>
      <description>scheme configuration of this project StoreCI</description>
      <value>Coding_iOS</value>
    </hudson.model.StringParameterValue>
    <hudson.model.StringParameterValue>
      <name>CONFIGURATION</name>
      <description>configuration of packing, Release/Debug</description>
      <value>Release</value>
    </hudson.model.StringParameterValue>
    <hudson.model.StringParameterValue>
      <name>OUTPUT_FOLDER</name>
      <description>output folder for build artifacts, it is located in workspace/project root dir.</description>
      <value>build_outputs</value>
    </hudson.model.StringParameterValue>
    <hudson.model.StringParameterValue>
      <name>BRANCH</name>
      <description>git repository branch</description>
      <value>master</value>
    </hudson.model.StringParameterValue>
  </parameters>
  <causeBag class="linked-hash-map">
    <entry>
      <hudson.model.Cause_-UserIdCause>
        <userId>shadow</userId>
      </hudson.model.Cause_-UserIdCause>
      <int>1</int>
    </entry>
  </causeBag>
```

```bash
# 获取<userId>shadow</userId>中的shadow
sed -n 's/.*>\(.*\)<\/userId>/\1/p' $JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/build.xml
# 获取<userId>shadow</userId>中的shadow，赋值给userId
# 使用位置：Jenkins获取构建人
userId=(`sed -n 's/.*>\(.*\)<\/userId>/\1/p' $JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/build.xml`)
```

#### Shell脚本获取文本特定字段

```bash
# 获取log文件第一行中，``[0m``字符后面的所有字符
head -1 $JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/log | awk -F '\\[0m' '{print $NF}'
```

#### Jenkins获取构建人，并赋值到变量并使用

取值``shell``
```bash
head -1 $JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/log | awk -F '\\[0m' '{print $NF}' > userId
read userId < userId
echo "userId=${userId}" > userId.txt
```
``set Build Name``中加入构建人
```bash
${PROPFILE,file="userId.txt",property="userId"}
```

#### Jenkins获取安卓APP版本号并赋值给变量并使用

取值``shell``
```bash
versionName=`cat app/gradle.properties | grep 'VERSION_NAME' | cut -d '=' -f 2 `
echo "versionName=${versionName}" > versionName.txt
```
``set Build Name``中加入安卓APP版本号
```bash
${PROPFILE,file="versionName.txt",property="versionName"}
```

#### 获取目录的所有csv文件并合并为一个csv文件
```bash
interface=$1
# 进入脚本所在的位置
cd /Users/taoyi/git_projects/Gitlab/RF_InterfaceTest/Library/处理接口文档
# 获取./output/api-docs/souche/*/*.csv文件并移动到./CSV目录下
mv -f ./*/*/*/*/*.csv ./CSV/
# 把所有的csv文件合并为一个together.csv文件
cat ./CSV/*.csv > ./$interface.csv
# 删除中间的处理文件
rm -rf ./output
rm -rf ./CSV/*.csv
# 在第一行下加入表头行
#sed -ig "" '1i\属于哪个服务,属于哪个suite,对应RF接口名称\n' ./together.csv
```

#### ``Json``中的字典转化成``Robot-Framework``的参数格式
```bash
# ``Json``中的字典转化成``Robot-Framework``的参数格式
# 先把需要修改的json文本写入文件，再对该文件进行操作
# 示例："./change_Dict.sh pice"

file_name=$1
sed -ig 's/":/=/g' $file_name
sed -ig 's/"//g' $file_name
sed -ig 's/,/    /g' $file_name
```

#### 简单的服务器部署脚本
```bash
#!/bin/bash

set -o errexit
set -o xtrace

dir_project_home="/home/souche/projects/topgear"
dir_tomcat_home="/home/souche/tomcats/12001_topgear-test"
file_war="*.war"
file_catalina_out=${dir_tomcat_home}"/logs/catalina.out"

echo "----update code from git begin"
cd ${dir_project_home}
git reset --hard
git pull
branch=$1
if [ ! -n "$branch" ];
then
    git checkout master
else
    git checkout $branch
fi
echo "----update code from git end"

echo "----build project begin"
cd ${dir_project_home}
# mvn config:load -Denv=DEV-STABLE -Dtoken=O6eq7WSKlC
mvn clean install  -DskipTests=true
echo "----build project end"

echo "----shutdown tomcat"
ps auxwww | grep java | grep ${dir_tomcat_home} | awk '{print $2}' | xargs kill -9 2>/dev/null;
sleep 1s

echo "----reset war file"
rm -rf ${dir_tomcat_home}/webapps/ROOT;
rm -rf ${dir_tomcat_home}/webapps/ROOT.war;
cp -r ${dir_project_home}/topgear-web/target/$file_war ${dir_tomcat_home}/webapps/ROOT.war

echo "----start tomcat"
sh ${dir_tomcat_home}/bin/startup.sh;

cd ${dir_tomcat_home}/logs
tail -f catalina.out
```

#### Jenkins上部署Tomcat的通用脚本
```bash
#!/bin/bash
set -o errexit
set -o xtrace

export BUILD_ID=pleaseDontKillMe
export JAVA_HOME=/opt/souche/java

dir_tomcat_home="/home/souche/tomcats/12001_topgear-test"
file_war="*.war"
file_catalina_out=${dir_tomcat_home}"/logs/catalina.out"

echo "----build project begin"
mvn config:load -Denv=DEV-STABLE -Dtoken=O6eq7WSKlC
mvn clean install  -DskipTests=true
echo "----build project end"

echo "----shutdown tomcat"
ps auxwww | grep java | grep ${dir_tomcat_home} | awk '{print $2}' | xargs kill -9 2>/dev/null;
sleep 1s

echo "----reset war file"
rm -rf ${dir_tomcat_home}/webapps/ROOT;
rm -rf ${dir_tomcat_home}/webapps/ROOT.war;
cp -r ${WORKSPACE}/topgear-web/target/$file_war ${dir_tomcat_home}/webapps/ROOT.war

echo "----start tomcat"
sh ${dir_tomcat_home}/bin/startup.sh;
```

#### **自动部署服务器应用**
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

#### 指定次数执行``pybot``脚本
```bash
# 执行示例：./repeat_test.sh testCases testSuite num

# 测试用例名称
tcName=$1
# 测试套件绝对路径
directPath=$2
# 测试用例执行次数
total=$3

count=1
while [ "$count" -le "$total" ]; do
    echo "$count"
    pybot -d results --test "$tcName" "$directPath"
    count=$((count + 1))
done
echo "Finished."
```

#### 顺序列出当前服务器上运营的 tomcat 应用
```bash
# ps 获取的结果，用"/"分隔，取第十段，并用数字正序排列
ps -ef | grep tomcat | awk -F "/" '{print $10 | sort -n}'
```

#### 指定文件中的换行符替换为空格
1. 使用正则
```bash
cat listTomcat | sed ':label;N;s/\n/ /;b label'
```
2. 使用 shell
```bash
cat listTomcat | tr "\n" " "
```

#### 根据 tag 和 env 执行用例
```bash
#!/usr/bin/env bash

# 选择环境
env=$1
# 选择需要执行的 tag
tag=$2

~/.pyenv/shims/pybot \
    -d results \
    -V ./envVars.py:$env \
    --listener ./RobotListener.py \
    --include=$tag \
    .
```

#### 把文件A的内容插入到文件B中的指定行后
```bash
#!/usr/bin/env bash
#for test add content from src_file to dest_file at specified place.

# fileName: addLines.sh
# 执行方式：./addLines.sh tomcatDir

tomcatDir=$1

echo "hello, begin..."
echo ""
echo "dealing ${tomcatDir}"

src_file="/home/souche/scripts/resource"
dest_file="/home/souche/jenkins/Home/jobs/"${tomcatDir}"/config.xml"


function addLines ()
{
    # delimit_line="==========================================="

:<<BLOCK
    sed -i "2i\\insert line" file 该sed命令使用的是-i参数指定i\选项，在第2行后插入内容
    2i\\ 拆解3部分：2为行号，i\为sed行下追加命令，\为转义字符(必须转义读取变量)
    "" 双引号，保持引号内的字面值，可读\$转义后的变量内容，单引号不行。
    echo $delimit_line | sed -i "2i\\$delimit_line" $dest_file
BLOCK

    # 删除倒数第二行
    sed -i.backup $(($(cat ${dest_file} | wc -l)))'d' ${dest_file}
    
    # 读取源文件
    cat $src_file | while read line
    # 使用循环，在倒数第二行开始，插入源文件的所有内容
    do
        echo $line | sed -i $(($(cat ${dest_file} | wc -l)+1))"i\\$line" $dest_file
        echo $line
    done

    #cat $dest_file
}

# 调用函数执行
addLines

echo ""
echo "hey, end..."
exit 0
```
_shell脚本中调用shell脚本_
```bash
#!/usr/bin/env bash

# 定义jenkins项目目录文件
jobsList="/home/souche/scripts/jobsList"

function repeatAddLines ()
{
	# 获取所有的jenkins项目名称，并写入文件jobsList中
	# ll ~/jenkins/Home/jobs/ | awk '{print $9}' > /home/souche/scripts/jobsList

	# 由于写入的文件中的第一行为空行，需要删除
	# sed -i '1d' /home/souche/scripts/jobsList

	# 读取jobsList中的每行
	cat $jobsList | while read line

	# 对每行名称的项目，调用以上代码进行删除和插入的操作
	do
		/home/souche/scripts/addLines.sh ${line}
	done
}

# 调用函数执行
repeatAddLines
```