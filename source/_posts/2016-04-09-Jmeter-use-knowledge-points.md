---
title: Jmeter使用知识点
date: 2016-04-09 17:08:50
categories: [Tools]
tags: [jmeter]
---

### 常用插件

#### `HTTP Request`HTTP请求
一个线程组或者集合中，所用的请求都使用相同的“Web服务器”，就可以添加一个“HTTP 请求默认值”组件，在其中设置好“服务器地址”、“端口号”、“延时”，这样所有的请求就都会使用该组件中的设置。

  <!--more-->

#### HTTP Cookie 管理器
需要在登录状态下才能发起的请求，在线程组中有一个登录的请求，这样再在该线程组中添加一个“HTTP Cookie 管理器”组件，登录请求完成时，该组件就会自动保存登录的Cookie，这样其他需要登录态才能进行的请求就也能成功进行。

#### `HTTP Header Manager`HTTP信息头管理器
有些服务器限制了需要正常的浏览器才能访问，但是Jmeter在发送请求时，默认使用的“User-Agent”是“Apache-HttpClient/4.2.6 (java 1.5)”，所以需要添加一个“HTTP 信息头管理器”组件，用于模拟正常的浏览器，模拟的内容需要自己手动添加到该组件中，如：User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0

#### `Backend Listener`后端监听器
收集`Jmeter`运行中的数据并传输给`Influxdb`，从而可以在`Grafana`平台上展示
{% asset_img 后端监听器.png 后端监听器 %}
对默认值进行修改，增加数据的抓取值：
```bash
samplersList：market.*
userRegexpForSamplersList：True
```

#### `jp@gc - Stepping Thread Group`阶梯加压插件
  - 线程组一共启动1000个线程数量，
  - 启动第一个线程前，需要等待0s，
  - 最开始启动100个线程，
  - 每隔1s，在1s内，启动100个线程，
  - 全部线程加载完毕后，持续运行600s，
  - 最后，在1s内停止100个线程。
{% asset_img 阶梯加压插件.png 阶梯加压插件 %}

#### `CSV Data Set Config`参数化插件
在压测过程中需要提前准备一些数据，使用该插件，在测试前提前准备好B端手机号，用于批量生成可用于压测的token和ShareId数据
{% asset_img 参数化插件.png 参数化插件 %}

#### `Regular Expression Extractor`正则表达式提取器
数据准备阶段，用于获取response中的值
{% asset_img 正则表达式提取器.png 正则表达式提取器 %}

#### `BeanShell PostProcessor`BeanShell 后置处理程序
测试中用到了token和shareId，使用后置处理程序获取多个字段，并把多个字段用逗号分隔，并写入文件
{% asset_img BeanShell后置处理程序.png BeanShell后置处理程序 %}
脚本如下：
```
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
String shareId=bsh.args[0];
	try {
		FileWriter fstream = new FileWriter("/Users/taoyi/Desktop/JMETER/tokenandShareId.csv",true);
		BufferedWriter out = new BufferedWriter(fstream);
		out.write("${token}"+","+vars.get("shareId")+"\n");
		out.close();
		fstream.close();
	} catch (IOException e) {
		e.printStackTrace();
	}
```

#### `jp@gc - Hits per Second`HPS打点值获取
测试执行过程中，用于获取HPS值
{% asset_img HPS打点值.png HPS打点值 %}

### 三方脚本
#### 不同并发数自动执行jmeter脚本shell命令
```bash
#!/usr/bin/env bash
export jmx_template="market"
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
