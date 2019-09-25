---
title: InfluxDB&Grafana&Shell性能自动化测试平台搭建
date: 2019-08-18 23:37:13
categories: [性能测试]
tags: [performance, influxDB, grafana, shell]
---

#### 安装`Docker`
[MAC平台](https://download.docker.com/mac/stable/Docker.dmg)
[Windows平台](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe)
[Ubuntu平台](https://www.runoob.com/docker/ubuntu-docker-install.html)
[Centos7平台](https://blog.csdn.net/xinzhifu1/article/details/83579256)

  <!--more-->

#### 安装并启用`influxDB`
##### 安装`influxDB`
```bash
# 安装
docker pull influxdb
# 启动容器
docker run -d -p 8086:8086 -p 8083:8083 --name=jmeterdb influxdb
# 进入容器内部
docker exec -it jmeterdb bash
# 进入influxdb命令行
flux
# 创建jmeter数据库
create database jmeter;
```

##### `Jmeter`设置
添加`Backend Listener`【后端监听器】
{% asset_img Backend-Listener.png Backend-Listener %}
{% asset_img 后端监听器.png 后端监听器 %}
只需修改三个字段：
  - influxdbUrl：修改为实际的`influxdb`地址
  - application：应用名称
  - testTitle：测试标题

##### 检查`jmeter`和数据库是否正常连接
在`jmeter`中添加Http请求，并执行测试
在`influxdb`后台中查询是否有产生数据：
```bash
# 进入容器内部
docker exec -it jmeterdb bash
# 进入influxdb命令行
flux
# 使用jmeter数据库
use jmeter
# 查询数据
select * from jmeter
```
{% asset_img 查询influxdb数据.png 查询influxdb数据 %}

#### 性能监控平台`Grafana`部署及初始化
##### `grafana`部署
[Grafana官网](https://grafana.com/docs/)
```bash
# 安装
docker pull grafana/grafana
# 启动容器
docker run -d -p 3000:3000 --name=jmeterGraf grafana/grafana
```

##### 平台初始化设置
1. 本地登录地址：[http://localhost:3000](http://localhost:3000)
2. 默认用户名/密码：admin/admin
3. 在Web平台中添加influxdb数据库
{% asset_img WEB平台influxDB设置.png WEB平台influxDB设置 %}
4. `JMeter Dashboard`设置
{% asset_img 导入工作台配置.png 导入工作台配置 %}
填入其中的[JSON内容](https://github.com/shadow000902/iJmeter/blob/master/shell/jmeter_dashboard.json)

#### 使用`Grafana`平台进行自动化压测实践
1. 对被测的`jmeter`脚本的`线程数`进行参数化设置
该设置主要用于在后面脚本中进行线程数的修改，从而达到执行不同并发下的测试
{% asset_img 线程参数化设置.png 线程参数化设置 %}
2. 测试脚本
```bash
#!/usr/bin/env bash
export jmx_template="jmeterScript"
export suffix=".jmx"
export jmx_template_filename="${jmx_template}${suffix}"
export os_type=`uname`

# 需要在系统变量中定义jmeter根目录的位置，如下
 export jmeter_path="/opt/apache-jmeter/"

# 清空nohup.out
cat /dev/null > nohup.out

# 强制杀掉JMeter进程
killJMeter()
{
    pid=`ps -ef|grep jmeter|grep java|awk '{print $2}'`
    echo "jmeter Id list :$pid"
    if [[ "$pid" = "" ]]
    then
      echo "no jmeter pid alive"
    else
      kill -9 $pid
    fi
}

# 设置执行5次测试，每次的线程数分别是【10、20、30、40、50】
# 每次测试的持续时间，由jmeter脚本中的调度器【Scheduler】的持续时间（秒）【Duration(seconds)】来定
thread_number_array=(10 20 30 40 50)
for num in "${thread_number_array[@]}"
do
    # 生成对应压测线程的jmx文件
    export jmx_filename="${jmx_template}_${num}${suffix}"
    export jtl_filename="test_${num}.jtl"

    rm -f ${jmx_filename} ${jtl_filename}
    cp ${jmx_template_filename} ${jmx_filename}
    echo "生成jmx压测脚本 ${jmx_filename}"

    if [[ "${os_type}" == "Darwin" ]]; then
        # Mac下执行该语句
        sed -i "" "s/thread_num/${num}/g" ${jmx_filename}
    else
        # Linux下执行该语句
        sed -i "s/thread_num/${num}/g" ${jmx_filename}
    fi

    # JMeter 静默压测
    nohup ${jmeter_path}/bin/jmeter -n -t ${jmx_filename} -l ${jtl_filename} &
    sleep 65
    killJMeter
    rm -f ${jmx_filename}
done
echo "自动化压测全部结束"
```
3. 测试结果的展现
{% asset_img 5次不同并发数的测试结果.png 5次不同并发数的测试结果 %}

