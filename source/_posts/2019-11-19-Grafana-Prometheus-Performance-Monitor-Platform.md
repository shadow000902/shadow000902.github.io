---
title: 性能压测监控环境搭建
date: 2019-11-19 15:35:45
categories: [环境搭建, 性能测试]
tags: [performance, prometheus, influxDB, grafana, shell]
---

### 几个关键地址
1. 包下载地址：[官网下载地址](https://prometheus.io/download/)
    - 监控服务：[prometheus](https://github.com/prometheus/prometheus/releases/download/v2.14.0/prometheus-2.14.0.linux-amd64.tar.gz)
    - 服务器监控服务：[node_exporter](https://github.com/prometheus/node_exporter/releases/download/v0.18.1/node_exporter-0.18.1.linux-amd64.tar.gz)
    - MySQL监控服务：[mysqld_exporter](https://github.com/prometheus/mysqld_exporter/releases/download/v0.12.1/mysqld_exporter-0.12.1.linux-amd64.tar.gz)
    - JVM监控服务：[jmx_exporter](https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.12.0/jmx_prometheus_javaagent-0.12.0.jar)

  <!--more-->

### `监控服务`部署
下载上述的监控服务包，并解压，可以得到如下文件：
```bash
root@su-007:~/tools/prometheus-2.13.1.linux-amd64# ll
total 136300
drwxr-xr-x  5 3434 3434     4096 Nov 22 09:35 ./
drwxr-xr-x  5 root root     4096 Nov  6 18:29 ../
drwxr-xr-x  2 3434 3434     4096 Oct 17 23:09 console_libraries/
drwxr-xr-x  2 3434 3434     4096 Oct 17 23:09 consoles/
drwxr-xr-x 24 root root     4096 Nov 23 23:00 data/
-rw-r--r--  1 3434 3434    11357 Oct 17 23:09 LICENSE
-rw-r--r--  1 root root   169283 Nov 23 23:00 nohup.log
-rw-r--r--  1 3434 3434     2770 Oct 17 23:09 NOTICE
-rwxr-xr-x  1 3434 3434 78646149 Oct 17 21:17 prometheus*
-rw-r--r--  1 3434 3434     1531 Nov 22 09:35 prometheus.yml
-rwxr-xr-x  1 3434 3434 47209942 Oct 17 21:18 promtool*
-rwxr-xr-x  1 3434 3434 13493572 Oct 17 21:19 tsdb*
```
其中`prometheus*`为服务启动脚本文件，`prometheus.yml`为普罗米修斯监控系统的配置文件

全量配置如下：
```yaml
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'
    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.
    static_configs:
    - targets: ['10.10.10.10:9090']

  - job_name: "mysql"
    static_configs:
    - targets: ["10.10.10.11:9104"]

  - job_name: "node"
    static_configs:
    - targets: ["10.10.10.10:9100","10.10.10.11:9100","10.10.10.12:9100"]

  - job_name: 'java'
    scrape_interval: 30s
    static_configs:
    - targets:
      - '10.10.10.11:2031'
      - '10.10.10.11:2032'
      - '10.10.10.11:2035'
      - '10.10.10.12:52031'
      - '10.10.10.12:52032'
      - '10.10.10.12:52035'
```
其中主要使用了几个模块的监控，没有会用报警，有需要的话，可以自己尝试。
几个模块的定义介绍：
    - `job_name: 'prometheus'`：是监控程序本身，用于监控检测被监控系统是否正确连接，默认端口9090
    - `job_name: "mysql"`：监控mysql服务器的情况，默认端口9104
    - `job_name: "node"`：监控服务器状态，默认端口9100
    - `job_name: 'java'`：JVM监控，这里的端口是自己在启动tomcat应用服务时，在启动脚本中自己定义的端口号
  这里的`job_name`都是可以自己定义，主要用来区分几个监控模块
  
配置好配置文件后，就可以启动监控服务了
```bash
nohup ./prometheus >> ./nohup.log 2>&1 &
```
启动脚本，设置后台运行，并把运行日志写进`nohup.log`文件中
启动后，就可以在浏览器中访问`10.10.10.10:9090/targets`查看各个节点的状态了，确保`State`是`UP`，不然就可能有问题，需要排查了
{% asset_img 监控节点情况.png 监控节点情况 %}

### `服务器`监控部署
下载上述的服务器监控服务包，并解压，可以得到如下文件：
```bash
root@su-007:~/tools/node_exporter-0.18.1.linux-amd64# ll
total 16512
drwxr-xr-x 2 3434 3434     4096 Nov  5 14:53 ./
drwxr-xr-x 5 root root     4096 Nov  6 18:29 ../
-rw-r--r-- 1 3434 3434    11357 Jun  5 00:50 LICENSE
-rwxr-xr-x 1 3434 3434 16878582 Jun  5 00:41 node_exporter*
-rw-r--r-- 1 root root     3439 Nov  5 14:53 nohup.log
-rw-r--r-- 1 3434 3434      463 Jun  5 00:50 NOTICE
```
这里面东西很简单，它不需要配置文件，只有一个关键的`node_exporter*`启动脚本文件，直接启动脚本就OK
```bash
nohup ./node_exporter >> ./nohup.log 2>&1 &
```
在浏览器访问`10.10.10.10:9100/metrics`，可以看到监控数据，就说明服务启动成功了

### `MySQL`监控部署
下载上述的MySQL监控服务包，并解压，可以得到如下文件：
```bash
root@test-01:~/tools/mysqld_exporter-0.12.1.linux-amd64$ ll
total 14500
drwxr-xr-x  2 root root     4096 Nov  6 17:43 ./
drwxrwxr-x 15 root root     4096 Nov  6 18:02 ../
-rw-r--r--  1 root root    11325 Jul 29 20:47 LICENSE
-rw-rw-r--  1 root root       51 Nov  6 17:38 .my.cnf
-rwxr-xr-x  1 root root 14813452 Jul 29 20:36 mysqld_exporter*
-rw-rw-r--  1 root root      529 Nov  6 16:58 nohup.log
-rw-r--r--  1 root root       65 Jul 29 20:47 NOTICE
```
默认只有一个`mysqld_exporter*`启动脚本文件。
`mysqld_exporter`需要连接到Mysql，所以需要Mysql的权限，我们先为它创建用户并赋予所需的权限。
命令行登录mysql，执行如下命令：
```sql
mysql> GRANT REPLICATION CLIENT,PROCESS ON *.* TO 'mysql_monitor'@'localhost' identified by 'mysql_monitor';
mysql> GRANT SELECT ON *.* TO 'mysql_monitor'@'localhost';
```
创建`mysqld_exporter`执行的配置文件`.my.cnf`，写入如下内容：
```bash
[client]
user=mysql_monitor
password=mysql_monitor
```
启动监控服务并调用脚本文件：
```bash
nohup ./mysqld_exporter --config.my-cnf=./.my.cnf >> ./nohup.log 2>&1 &
```
在浏览器访问`10.10.10.11:9104/metrics`，可以看到监控数据，就说明服务启动成功了

### `JVM`监控部署
下载上述的jar文件，创建配置文件`jmx_exporter.yml`
配置文件内容如下：
```yaml
#---    # ---前的#要去掉
lowercaseOutputLabelNames: true
lowercaseOutputName: true
whitelistObjectNames: ["java.lang:type=OperatingSystem"]
rules:
 - pattern: 'java.lang<type=OperatingSystem><>((?!process_cpu_time)\w+):'
   name: os_$1
   type: GAUGE
   attrNameSnakeCase: true
```
在启动tomcat的脚本中，添加参数`-javaagent:/home/shadow/tools/JMX/jmx_prometheus_javaagent-0.12.0.jar=3080:/home/shadow/tools/JMX/jmx_exporter.yml`
在启动脚本中：
```bash
CATALINA_OPTS="-Xms2g -Xmx2g -javaagent:/home/shadow/tools/JMX/jmx_prometheus_javaagent-0.12.0.jar=3080:/home/shadow/tools/JMX/jmx_exporter.yml"
```
这里定义的3080端口，既是`prometheus`监控服务获取JVM参数的端口
还有一点需要注意的是：`jmx_prometheus_javaagent-0.12.0.jar`和`jmx_exporter.yml`存放的位置必须和tomcat的位置在同一用户下，不然可能会出现因为权限问题，无法调用的情况。
在浏览器访问`10.10.10.11:3080/metrics`，可以看到监控数据，就说明服务启动成功了

### `Grafana`各个监控面板配置
每个不同类型的监控，需要有不同类型的面板，这里不自己配置面板，而是从外部导入，[官方Dashboards平台](https://grafana.com/grafana/dashboards)
1. 服务器监控面板：选择`主机基础监控(cpu，内存，磁盘，网络)`，`ID`为`9276`
2. MySQL监控面板：选择`MySQL Overview`，`ID`为`7362`
3. JVM监控面板：选择`JMX Overview`，`ID`为`3457`