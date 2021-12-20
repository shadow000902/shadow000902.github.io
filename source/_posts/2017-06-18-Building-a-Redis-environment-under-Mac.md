---
title: Mac下Redis环境搭建
date: 2017-06-18 18:08:44
categories: [环境搭建, Redis]
tags: [redis]
---

#### 下载安装包
下载稳定版本的安装包[redis-stable](http://download.redis.io/redis-stable.tar.gz)

#### 安装Redis
   ```bash
   tar -xvf redis-stable.tar.gz
   cp ./redis-stable /opt/
   cd /opt/redis-stable
   sudo make test
   sudo make install
   ```

  <!--more-->


#### 配置Redis
1. 创建需要的目录
   ```bash
   mkdir bin
   mkdir etc
   mkdir db
   ```

2. 拷贝安装好的``redis``文件到创建的``bin``目录下
   ```bash
   cp /usr/bin/redis-* /opt/redis-stable/bin/
   ```
       结果``/opt/redis-stable/bin/``目录下的内容如下
   ```bash
   ╭─taoyi at TaoYi-Mac in /opt/redis-stable/bin using ‹› 17-06-18 - 18:06:48
   ╰─○ ll
   total 6648
   -rwxr-xr-x  1 taoyi  staff    98K  6 18 18:06 redis-benchmark
   -rwxr-xr-x  1 taoyi  staff    14K  6 18 18:06 redis-check-aof
   -rwxr-xr-x  1 taoyi  staff   1.0M  6 18 18:06 redis-check-rdb
   -rwxr-xr-x  1 taoyi  staff   159K  6 18 18:06 redis-cli
   -rwxr-xr-x  1 taoyi  staff   1.0M  6 18 18:06 redis-sentinel
   -rwxr-xr-x  1 taoyi  staff   1.0M  6 18 18:06 redis-server
   ```

3. 拷贝安装目录``src``目录下的``mkreleasehdr.sh``到安装目录下
   ```bash
   cp /opt/redis-stable/src/mkreleasehdr.sh /opt/redis-stable/
   ```

4. 拷贝安装目录下的``redis.conf``到创建的``etc``目录下
   ```bash
   cp /opt/redis-stable/redis.conf /opt/redis-stable/etc/
   ```

5. 修改``redis.conf``
   ```text
   #修改为守护模式
   daemonize yes
   #设置进程锁文件
   pidfile /opt/redis-stable/redis.pid
   #端口
   port 6379
   #客户端超时时间
   timeout 300
   #日志级别
   loglevel debug
   #日志文件位置
   logfile /opt/redis-stable/log-redis.log
   #设置数据库的数量，默认数据库为0，可以使用SELECT <dbid>命令在连接上指定数据库id
   databases 8
   ##指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合
   #save <seconds> <changes>
   #Redis默认配置文件中提供了三个条件：
   save 900 1
   save 300 10
   save 60 10000
   #指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF压缩，如果为了节省CPU时间，
   #可以关闭该#选项，但会导致数据库文件变的巨大
   rdbcompression yes
   #指定本地数据库文件名
   dbfilename dump.rdb
   #指定本地数据库路径
   dir /opt/redis-stable/db/
   #指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能
   #会在断电时导致一段时间内的数据丢失。因为 redis本身同步数据文件是按上面save条件来同步的，所以有
   #的数据会在一段时间内只存在于内存中
   appendonly no
   #指定更新日志条件，共有3个可选值：
   #no：表示等操作系统进行数据缓存同步到磁盘（快）
   #always：表示每次更新操作后手动调用fsync()将数据写到磁盘（慢，安全）
   #everysec：表示每秒同步一次（折衷，默认值）
   appendfsync everysec
   ```

8. 修改``redis``目录的所有者
   ```bash
   chown -R taoyi /opt/redis-stable
   ```

#### 启动Redis服务
   ```bash
   ./opt/redis-stable/bin/redis-server ./opt/redis-stable/etc/redis.conf
   ```

#### 访问Redis服务
   ```bash
   ./opt/redis-stable/bin/redis-cli
   ```

### `Ubuntu`安装`redis`服务
1. 安装
    ```shell
    $ sudo apt-get install redis-server
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following packages were automatically installed and are no longer required:
      dctrl-tools javascript-common libjs-jquery libjs-sphinxdoc libjs-underscore libsodium18 libyaml-0-2 libzmq5 python-cffi-backend python-chardet
      python-concurrent.futures python-crypto python-cryptography python-dateutil python-enum34 python-gnupg python-idna python-ipaddress python-jinja2
      python-mako python-markupsafe python-msgpack python-ndg-httpsclient python-openssl python-psutil python-pyasn1 python-pycurl python-pymysql python-requests
      python-six python-systemd python-tornado python-urllib3 python-yaml python-zmq salt-common
    Use 'sudo apt autoremove' to remove them.
    The following additional packages will be installed:
      libjemalloc1 redis-tools
    Suggested packages:
      ruby-redis
    The following NEW packages will be installed:
      libjemalloc1 redis-server redis-tools
    0 upgraded, 3 newly installed, 0 to remove and 248 not upgraded.
    Need to get 519 kB of archives.
    After this operation, 1,507 kB of additional disk space will be used.
    Do you want to continue? [Y/n] Y
    Get:1 http://mirrors.aliyun.com/ubuntu xenial/universe amd64 libjemalloc1 amd64 3.6.0-9ubuntu1 [78.9 kB]
    Get:2 http://mirrors.aliyun.com/ubuntu xenial-security/universe amd64 redis-tools amd64 2:3.0.6-1ubuntu0.4 [95.5 kB]
    Get:3 http://mirrors.aliyun.com/ubuntu xenial-security/universe amd64 redis-server amd64 2:3.0.6-1ubuntu0.4 [344 kB]
    Fetched 519 kB in 0s (1,716 kB/s) 
    Selecting previously unselected package libjemalloc1.
    (Reading database ... 116705 files and directories currently installed.)
    Preparing to unpack .../libjemalloc1_3.6.0-9ubuntu1_amd64.deb ...
    Unpacking libjemalloc1 (3.6.0-9ubuntu1) ...
    Selecting previously unselected package redis-tools.
    Preparing to unpack .../redis-tools_2%3a3.0.6-1ubuntu0.4_amd64.deb ...
    Unpacking redis-tools (2:3.0.6-1ubuntu0.4) ...
    Selecting previously unselected package redis-server.
    Preparing to unpack .../redis-server_2%3a3.0.6-1ubuntu0.4_amd64.deb ...
    Unpacking redis-server (2:3.0.6-1ubuntu0.4) ...
    Processing triggers for libc-bin (2.23-0ubuntu11) ...
    Processing triggers for man-db (2.7.5-1) ...
    Processing triggers for ureadahead (0.100.0-19.1) ...
    Processing triggers for systemd (229-4ubuntu21.22) ...
    Setting up libjemalloc1 (3.6.0-9ubuntu1) ...
    Setting up redis-tools (2:3.0.6-1ubuntu0.4) ...
    Setting up redis-server (2:3.0.6-1ubuntu0.4) ...
    Processing triggers for libc-bin (2.23-0ubuntu11) ...
    Processing triggers for ureadahead (0.100.0-19.1) ...
    Processing triggers for systemd (229-4ubuntu21.22) ...
    ```
    安装完成后，即会自动启动redis服务

2. 查看进程端口号
    ```shell 
    $ ps -aux | grep redis
    redis    10727  0.0  0.0  40892  6796 ?        Ssl  10:38   0:00 /usr/bin/redis-server 127.0.0.1:6379
    shadow   10800  0.0  0.0  14980  1012 pts/1    S+   10:39   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn redis
    ```

3. 查看redis服务器状态
    ```shell 
    $ netstat -nlt | grep 6379
    tcp        0      0 127.0.0.1:6379          0.0.0.0:*               LISTEN     
    ```
    ```bash
    $ sudo /etc/init.d/redis-server status
    ● redis-server.service - Advanced key-value store
       Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor preset: enabled)
       Active: active (running) since Thu 2021-03-18 10:38:56 CST; 1min 10s ago
         Docs: http://redis.io/documentation,
               man:redis-server(1)
     Main PID: 10727 (redis-server)
       CGroup: /system.slice/redis-server.service
               └─10727 /usr/bin/redis-server 127.0.0.1:6379
    
    Mar 18 10:38:56 kickseed systemd[1]: Starting Advanced key-value store...
    Mar 18 10:38:56 kickseed run-parts[10719]: run-parts: executing /etc/redis/redis-server.pre-up.d/00_example
    Mar 18 10:38:56 kickseed run-parts[10728]: run-parts: executing /etc/redis/redis-server.post-up.d/00_example
    Mar 18 10:38:56 kickseed systemd[1]: Started Advanced key-value store.
    ```

4. 配置文件修改
    ```shell
    /etc/redis/redis.conf
    ```
   开启Redis的远程连接：
   注释掉绑定地址`#bind 127.0.0.1`

5. 重启服务
    ```shell
   sudo /etc/init.d/redis-server restart
   # 或者
   sudo service redis-server restart
   # 或者
   sudo redis-server /etc/redis/redis.conf
    ```
