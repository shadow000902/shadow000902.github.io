---
title: Jenkins中slave的设置
date: '2017-06-24T13:02:12.000Z'
categories:
  - Jenkins
tags:
  - jenkins
---

# 2017-06-24-Jenkins-slave-settings

### 在Jenkins中配置从节点

增加节点后，实际并没有直接连上，还需要在节点服务器上进行相应的配置

### 在从节点服务器的host中的加入配置

```bash
sudo vim /etc/hosts
```

```bash
111.111.111.111 jenkins.shadow.com                        # 前部分IP为Jenkins的内网地址，后部分为Jenkins的对外访问域名
```

### 从节点服务器上配置Jenkins节点配置

点击上图中的`slave.jar`的链接，下载该文件，放在上方指定的`Jenkins`工作目录下

```bash
test@test-devtesting-00001:~/jenkins$ ll
total 760
drwxrwxr-x  3 test test   4096 Jun 23 16:04 ./
drwx------ 18 test test   4096 Jun 24 13:47 ../
-rw-rw-r--  1 test test   7623 Jun 23 16:04 maven33-agent.jar
-rw-rw-r--  1 test test  19971 Jun 23 16:04 maven33-interceptor.jar
-rw-rw-r--  1 test test   6764 Jun 23 16:04 maven3-interceptor-commons.jar
-rw-rw-r--  1 test test    738 Jun  8 16:52 slave-agent.jnlp
-rw-rw-r--  1 test test 717563 May  2 17:29 slave.jar                                # 上方下载的slave.jar文件
-rwxrwxr-x  1 test test    114 Jun  6 19:28 start_jenkins.sh*                        # 启动Jenkinsslave的脚本
drwxrwxr-x 14 test test   4096 Jun 24 12:43 workspace/                                # Jenkins项目的工作目录
```

将提示中的启动`Jenkins`的脚本写入文件`start_jenkins.sh`中

```text
java -jar slave.jar -jnlpUrl http://jenkins.shadow.com/computer/test-devtesting-00001/slave-agent.jnlp 2>&1 &
# 或
java -Dfile.encoding=UTF-8 -jar agent.jar -jnlpUrl http://jenkins.shadow.com/computer/slave_51/slave-agent.jnlp -secret 815485b5788e77960f86a1sdf32es6e02d55c9fa104c0e754c1efb046e8a50b44c31cec4 2>&1 &
```

* 如果在 slave 上执行脚本出现乱码问题，可以通过加该参数`-Dfile.encoding=UTF-8`解决
* 如果服务器存在密码，用于免密链接需要加该参数`-secret 815485b5788e77960f86a6e02q3easf1cxad55c9fa104c0e754c1efb046e8a50`，该参数一般在 jenkins 的 slave 设置页会显示出来。

赋予`start_jenkins.sh`执行权限

```bash
chmod a+x start_jenkins.sh
```

启动slave

```bash
./start_jenkins.sh
```

回到Jenkins节点列表，查看添加的节点，状态如图就说明启动成功了。

至此，slave节点就配置并启动完毕了。

### 通过`SSH`的方式连接`slave`

* 启动方式：`Launch agent agents via SSH`
* 主机：Agent's Hostname or IP
* Credentials：登录以上`主机`的账密信息

  该种连接`slave`的方式依赖`Java`环境，所以需要设置一个`JAVA_HOME`的环境变量

  如无问题，点击保存之后，就会正常连接成功了

### 问题处理

1. 出现`java.net.ConnectException: Connection refused (Connection refused)`解决方式 在 jenkins 的`系统设置`中的`Jenkins Location`模块下的`Jenkins URL`中，不要使用域名，而是直接写`http://IP:port`
2. `slave`经常会掉线处理 首先需要获取到slave的状态

   ```bash
    http://hostName/computer/slaveName/api/json?pretty=true
   ```

   请求该url会得到一个slave状态的结果

   ```javascript
    {
      "_class" : "hudson.slaves.SlaveComputer",
      "actions" : [
        {
          "_class" : "hudson.plugins.jobConfigHistory.ComputerConfigHistoryAction"
        },
        {

        }
      ],
      "assignedLabels" : [
        {
          "name" : "Mac_slave"
        }
      ],
      "description" : "",
      "displayName" : "Mac_slave",
      "executors" : [
        {

        },
        {

        }
      ],
      "icon" : "computer.png",
      "iconClassName" : "icon-computer",
      "idle" : true,
      "jnlpAgent" : true,
      "launchSupported" : false,
      "loadStatistics" : {
        "_class" : "hudson.model.Label$1"
      },
      "manualLaunchAllowed" : true,
      "monitorData" : {
        "hudson.node_monitors.SwapSpaceMonitor" : {
          "_class" : "hudson.node_monitors.SwapSpaceMonitor$MemoryUsage2",
          "availablePhysicalMemory" : -1,
          "availableSwapSpace" : 830472192,
          "totalPhysicalMemory" : -1,
          "totalSwapSpace" : 1073741824
        },
        "hudson.node_monitors.TemporarySpaceMonitor" : {
          "_class" : "hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace",
          "timestamp" : 1596678461230,
          "path" : "/private/var/folders/3z/t812m3_x2218m6wchwd0ttdm0000gn/T",
          "size" : 63684665344
        },
        "hudson.node_monitors.DiskSpaceMonitor" : {
          "_class" : "hudson.node_monitors.DiskSpaceMonitorDescriptor$DiskSpace",
          "timestamp" : 1596678460739,
          "path" : "/Users/shadow/jenkins_slave/workspace",
          "size" : 63684665344
        },
        "hudson.node_monitors.ArchitectureMonitor" : "Mac OS X (x86_64)",
        "hudson.node_monitors.ResponseTimeMonitor" : {
          "_class" : "hudson.node_monitors.ResponseTimeMonitor$Data",
          "timestamp" : 1596678460739,
          "average" : 106
        },
        "hudson.node_monitors.ClockMonitor" : {
          "_class" : "hudson.util.ClockDifference",
          "diff" : -45
        }
      },
      "numExecutors" : 2,
      "offline" : false,
      "offlineCause" : null,
      "offlineCauseReason" : "",
      "oneOffExecutors" : [

      ],
      "temporarilyOffline" : false,
      "absoluteRemotePath" : "/Users/shadow/jenkins_slave/workspace"
    }
   ```

   其中有一个`offline`字段，`false`表示在线，`true`表示掉线，并且会在`offlineCauseReason`字段中显示掉线原因 然后我们可以通过定时获取`offline`字段的值来判断`slave`是否掉线，如果掉线了，就采取相应的重启`slave`的措施

   处理代码如下：

   \`\`\`python

   **-**_**- coding: utf-8 -**_**-**

   from time import sleep

   import paramiko import requests

```text
def getSlaveStatus():
    baseapi = 'http://jenkins.shadow.com/computer/Mac_slave/api/json?pretty=true'
    resp = requests.get(baseapi)
    result = resp.json()
    return result


def judgeStatus():
    while True:
        sleep(3)
        result = getSlaveStatus()
        print(result)
        status = result["offline"]
        while status:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname='192.168.8.8', port=22, username='shadow', password='V4Hubd1WBePJ')
            stdin, stdout, stderr = ssh.exec_command(
                "nohup java -Xmx1024m -jar /Users/shadow/jenkins_slave/agent.jar -jnlpUrl "
                "http://jenkins.shadow.com/computer/Mac_slave/slave-agent.jnlp -secret "
                "d6c66e20341aa6e628b5f057355384a1q21q1q1a462349a852eec1294ad40cbd016964cb &")
            print(stdout.read())
            break


if __name__ == '__main__':
    judgeStatus()

```
```

