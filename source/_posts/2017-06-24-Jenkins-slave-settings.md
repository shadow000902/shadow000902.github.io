---
title: Jenkins中slave的设置
date: 2017-06-24 13:02:12
categories: [Jenkins]
tags: [jenkins]
---

### 在Jenkins中配置从节点
{% asset_img 配置从节点.png 配置从节点 %}
增加节点后，实际并没有直接连上，还需要在节点服务器上进行相应的配置

  <!--more-->

### 在从节点服务器的host中的加入配置

```bash
sudo vim /etc/hosts
```
```bash
111.111.111.111 jenkins.shadow.com						# 前部分IP为Jenkins的内网地址，后部分为Jenkins的对外访问域名
```

### 从节点服务器上配置Jenkins节点配置
{% asset_img 从节点配置要点.png 从节点配置要点 %}
点击上图中的``slave.jar``的链接，下载该文件，放在上方指定的``Jenkins``工作目录下
```bash
test@test-devtesting-00001:~/jenkins$ ll
total 760
drwxrwxr-x  3 test test   4096 Jun 23 16:04 ./
drwx------ 18 test test   4096 Jun 24 13:47 ../
-rw-rw-r--  1 test test   7623 Jun 23 16:04 maven33-agent.jar
-rw-rw-r--  1 test test  19971 Jun 23 16:04 maven33-interceptor.jar
-rw-rw-r--  1 test test   6764 Jun 23 16:04 maven3-interceptor-commons.jar
-rw-rw-r--  1 test test    738 Jun  8 16:52 slave-agent.jnlp
-rw-rw-r--  1 test test 717563 May  2 17:29 slave.jar								# 上方下载的slave.jar文件
-rwxrwxr-x  1 test test    114 Jun  6 19:28 start_jenkins.sh*						# 启动Jenkinsslave的脚本
drwxrwxr-x 14 test test   4096 Jun 24 12:43 workspace/								# Jenkins项目的工作目录
```
将提示中的启动``Jenkins``的脚本写入文件``start_jenkins.sh``中
```shell
java -jar slave.jar -jnlpUrl http://jenkins.shadow.com/computer/test-devtesting-00001/slave-agent.jnlp 2>&1 &
# 或
java -Dfile.encoding=UTF-8 -jar agent.jar -jnlpUrl http://jenkins-14.dasouche-inc.net:17080/computer/slave_51/slave-agent.jnlp -secret 815485b5788e77960f86a6e02d55c9fa104c0e754c1efb046e8a50b44c31cec4 2>&1 &
```
- 如果在 slave 上执行脚本出现乱码问题，可以通过加该参数`-Dfile.encoding=UTF-8`解决
- 如果服务器存在密码，用于免密链接需要加该参数`-secret 815485b5788e77960f86a6e02d55c9fa104c0e754c1efb046e8a50`，该参数一般在 jenkins 的 slave 设置页会显示出来。

赋予``start_jenkins.sh``执行权限
```bash
chmod a+x start_jenkins.sh
```
启动slave
```bash
./start_jenkins.sh
```
回到Jenkins节点列表，查看添加的节点，状态如图就说明启动成功了。
{% asset_img 节点列表.png 节点列表 %}

至此，slave节点就配置并启动完毕了。

### 通过`SSH`的方式连接`slave`
{% asset_img SSH方式设置slave连接.png SSH方式设置slave连接 %}
- 启动方式：`Launch agent agents via SSH`
- 主机：Agent's Hostname or IP
- Credentials：登录以上`主机`的账密信息
该种连接`slave`的方式依赖`Java`环境，所以需要设置一个`JAVA_HOME`的环境变量
如无问题，点击保存之后，就会正常连接成功了

### 问题处理
1. 出现`java.net.ConnectException: Connection refused (Connection refused)`解决方式
    在 jenkins 的`系统设置`中的`Jenkins Location`模块下的`Jenkins URL`中，不要使用域名，而是直接写`http://IP:port`
