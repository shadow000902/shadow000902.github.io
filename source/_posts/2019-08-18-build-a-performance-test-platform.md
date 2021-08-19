---
title: InfluxDB&Grafana&Shell性能自动化测试平台搭建
date: '2019-08-18T23:37:13.000Z'
categories:
  - 环境搭建
  - 性能测试
tags:
  - performance
  - influxDB
  - grafana
  - shell
---

# 2019-08-18-build-a-performance-test-platform

#### 安装`Docker`

[MAC平台](https://download.docker.com/mac/stable/Docker.dmg) [Windows平台](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) [Ubuntu平台](https://www.runoob.com/docker/ubuntu-docker-install.html) [Centos7平台](https://blog.csdn.net/xinzhifu1/article/details/83579256)

#### 安装并启用`influxDB`

**安装influxDB**

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

**Jmeter设置**

添加`Backend Listener`【后端监听器】

只需修改三个字段：

* influxdbUrl：修改为实际的`influxdb`地址
* application：应用名称
* testTitle：测试标题

**检查jmeter和数据库是否正常连接**

在`jmeter`中添加Http请求，并执行测试 在`influxdb`后台中查询是否有产生数据：

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

#### 性能监控平台`Grafana`部署及初始化

**grafana部署**

[Grafana官网](https://grafana.com/docs/)

```bash
# 安装
docker pull grafana/grafana
# 启动容器
docker run -d -p 3000:3000 --name=jmeterGraf grafana/grafana
```

**平台初始化设置**

1. 本地登录地址：[http://localhost:3000](http://localhost:3000)
2. 默认用户名/密码：admin/admin
3. 在Web平台中添加influxdb数据库
4. `JMeter Dashboard`设置

填入其中的[JSON内容](https://github.com/shadow000902/iJmeter/blob/master/shell/jmeter_dashboard.json)

#### 使用`Grafana`平台进行自动化压测实践

1. 对被测的`jmeter`脚本的`线程数`进行参数化设置

   该设置主要用于在后面脚本中进行线程数的修改，从而达到执行不同并发下的测试

2. 测试脚本

   \`\`\`bash

   **!/usr/bin/env bash**

   export jmx\_template="jmeterScript"

   export suffix=".jmx"

   export jmx\_template\_filename="${jmx\_template}${suffix}"

   export os\_type=`uname`

## 需要在系统变量中定义jmeter根目录的位置，如下

export jmeter\_path="/opt/apache-jmeter/"

## 清空nohup.out

cat /dev/null &gt; nohup.out

## 强制杀掉JMeter进程

killJMeter\(\) { pid=`ps -ef|grep jmeter|grep java|awk '{print $2}'` echo "jmeter Id list :$pid" if \[\[ "$pid" = "" \]\] then echo "no jmeter pid alive" else kill -9 $pid fi }

## 设置执行5次测试，每次的线程数分别是【10、20、30、40、50】

## 每次测试的持续时间，由jmeter脚本中的调度器【Scheduler】的持续时间（秒）【Duration\(seconds\)】来定

thread\_number\_array=\(10 20 30 40 50\) for num in "${thread\_number\_array\[@\]}" do

```text
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
```

done echo "自动化压测全部结束"

```text
3. 测试结果的展现
{% asset_img 5次不同并发数的测试结果.png 5次不同并发数的测试结果 %}

### 服务器的使用情况监控
1. 获取服务器监控数据
```bash
# 每秒采集一次，采集300次，生成文件名："主机名_年月日_时分.nmon",如："su-stable-007_191031_1814.nmon"
nmon -ft -s 1 -c 300
```

1. 安装`nmon2influxdb`
2. 导入采集的数据到`influxdb`中

   ```bash
   root@su-stable-007:~# ./nmon2influxdb  import su-stable-007_191031_1814.nmon 
   2019/10/31 18:20:26 Using configuration file /root/.nmon2influxdb.cfg
   2019/10/31 18:20:26 Creating InfluxDB database nmon_reports
   2019/10/31 18:20:26 NMON file separator: ,
   ####
   File su-stable-007_191031_1814.nmon imported : 28800 points !
   ```

3. 在`influxdb`查询已导入的`nmon`数据

   \`\`\`bash

   root@su-stable-007:~\# influx

   Connected to [http://localhost:8086](http://localhost:8086) version 1.7.8

   InfluxDB shell version: 1.7.8

   > show databases name: databases name

telegraf \_internal jmeter nmon\_reports nmon2influxdb\_log

> use nmon\_reports Using database nmon\_reports show measurements name: measurements
>
> ### name
>
> CPU\_ALL DISKBSIZE DISKBUSY DISKREAD DISKWRITE DISKXFER JFSFILE MEM NET NETPACKET PROC VM select \* from MEM name: MEM time host name value
>
> 1572538454000000000 su-stable-007 active 2740.8 1572538454000000000 su-stable-007 bigfree -1 1572538454000000000 su-stable-007 buffers 226.3 1572538454000000000 su-stable-007 cached 3511.5 1572538454000000000 su-stable-007 highfree -0 1572538454000000000 su-stable-007 hightotal -0 1572538454000000000 su-stable-007 inactive 1470.1 1572538454000000000 su-stable-007 lowfree -0 1572538454000000000 su-stable-007 lowtotal -0 1572538454000000000 su-stable-007 memfree 3509.7 1572538454000000000 su-stable-007 memshared -0 1572538454000000000 su-stable-007 memtotal 7983.1
>
> ```text
> 5. 导入面板
> ```bash
> root@su-stable-007:~# ./nmon2influxdb dashboard su-stable-007_191031_1814.nmon 
> 2019/10/31 19:35:02 Using configuration file /root/.nmon2influxdb.cfg
> 2019/10/31 19:35:02 json: cannot unmarshal number into Go value of type grafanaclient.DataSourcePlugin
> root@su-stable-007:~# ./nmon2influxdb dashboard su-stable-007_191031_1814.nmon 
> 2019/10/31 19:41:46 Using configuration file /root/.nmon2influxdb.cfg
> 2019/10/31 19:41:47 Dashboard uploaded to grafana
> ```
>
> 导入时，可能会出现上面第一次失败的情况，可以多试几次；也可能需要自己手动创建`DataSource`，因为从上面看出来并没有自动创建`DataSource`。 理论上的情况如下：
>
> ```bash
> root@su-stable-007:~# ./nmon2influxdb dashboard su-stable-007_191031_1814.nmon 
> 2019/10/31 19:41:46 Using configuration file /root/.nmon2influxdb.cfg
> 2019/10/31 19:41:47 Grafana nmon2influxdb DataSource created.
> 2019/10/31 19:41:48 Dashboard uploaded to grafana
> ```
>
> 此步操作会创建一个`grafana`的面板，并新建一个`DataSource`，需要自己手动修改一下`DataSource`的`HTTP-URL`

