---
title: Linux环境安装MySQL
date: 2018-07-21 15:48:15
categories: [MySQL]
tags: [python, mysql]
---

### 以下内容基于CentOS完成

#### MySQL包下载地址
[32位5.7.22版本下载地址](https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-i686.tar.gz)
[64位5.7.22版本下载地址](https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-x86_64.tar.gz)

  <!--more-->

#### 下载、解压并安装
```bash
# 下载
wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-i686.tar.gz
# 解压
tar -zxvf mysql-5.7.22-linux-glibc2.12-i686.tar.gz
# 移动并重命名文件夹mysql-5.7.22-linux-glibc2.12-i686为mysql，并移动文件夹到/usr/local/
mv ~/Documents/mysql-5.7.22-linux-glibc2.12-i686 /usr/local/mysql
# 检查库文件是否有删除，若有便删除（linux系统自带的）
rpm -qa | grep mysql
# 检查mysql组和用户是否存在，如无创建
cat /etc/group | grep mysql
cat /etc/passwd |grep mysql
# 创建用户组和用户
groupadd mysql
# //useradd -r参数表示mysql用户是系统用户，不可用于登录系统
useradd -r -g mysql mysql
# 在mysql下添加data目录
cd /usr/local/mysql
mkdir data
# 更改mysql目录下所有的目录及文件夹所属组合用户
cd /usr/local/
chown -R mysql mysql/
chgrp -R mysql mysql/
```

#### 安装和初始化数据库
```bash
./mysqld --initialize --user=mysql --basedir=/usr/local/mysql/ --datadir=/usr/local/mysql/data/
```
成功结果：
```bash
2018-07-21T06:59:31.854623Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
2018-07-21T06:59:32.366767Z 0 [Warning] InnoDB: New log files created, LSN=45790
2018-07-21T06:59:32.468040Z 0 [Warning] InnoDB: Creating foreign key constraint system tables.
2018-07-21T06:59:32.526369Z 0 [Warning] No existing UUID has been found, so we assume that this is the first time that this server has been started. Generating a new UUID: 9ec0b2b8-8cb3-11e8-b9c4-f022d6ce8326.
2018-07-21T06:59:32.526606Z 0 [Warning] Gtid table is not ready to be used. Table 'mysql.gtid_executed' cannot be opened.
2018-07-21T06:59:32.529148Z 1 [Note] A temporary password is generated for root@localhost: ,:eh<pj(p2NZ
```
```bash
2018-10-20T18:10:58.363348Z 0 [System] [MY-013169] [Server] /opt/mysql-8.0.12-linux-glibc2.12-x86_64/bin/mysqld (mysqld 8.0.12) initializing of server in progress as process 12636
2018-10-20T18:10:58.366576Z 0 [Warning] [MY-010122] [Server] One can only use the --user switch if running as root
2018-10-20T18:11:01.748127Z 5 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: &h3Th88Lwx5f
2018-10-20T18:11:03.525973Z 0 [System] [MY-013170] [Server] /opt/mysql-8.0.12-linux-glibc2.12-x86_64/bin/mysqld (mysqld 8.0.12) initializing of server has completed
```

最后的``,:eh<pj(p2NZ``为mysql初始化默认密码。

#### 配置``/etc/my.cnf``
```cnf
[mysqld]
#skip-grant-tables
basedir = /usr/local/mysql/
datadir = /usr/local/mysql/data/

[mysql]
#skip-grant-tables
basedir = /usr/local/mysql/
datadir = /usr/local/mysql/data/
```


#### 初始化报错
```bash
$ ./bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql/ --datadir=/usr/local/mysql/data/
2018-07-21T06:58:34.705850Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
2018-07-21T06:58:34.707384Z 0 [ERROR] Could not open file '/var/log/mysqld.log' for error logging: Permission denied
2018-07-21T06:58:34.707398Z 0 [ERROR] Aborting
```
原因：文件没有权限
解决方法：
```bash
touch /var/log/mysqld.log
# 设置文件所有者为mysql
chown -R mysql:mysql /var/log/mysqld.log
```

#### 将``mysqld``服务加入开机自启动项
```bash
cd /usr/local/mysql
cp ./support-files/mysql.server /etc/init.d/mysql
# 把mysql注册为开机启动的服务
chmod +x /etc/init.d/mysql
# 查看是否添加成功
chkconfig --add mysql
chkconfig --list mysql
# mysql          	0:关闭	1:关闭	2:启用	3:启用	4:启用	5:启用	6:关闭
```
``Ubuntu``下，已经没有了``chkconfig``，替换之后的是``sysv-rc-conf``

#### 启动``mysql``服务





#### 设置远程登录权限
```bash
mysql> grant all privileges on *.* to'root' @'%' identified by 'root';
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> quit
Bye
```

#### 无密码登录mysql
在``/etc/my.cnf``中加入``skip-grant-tables``

#### 修改mysql默认密码
```bash
mysql> set password='123456';
```

#### 问题解决
1. ``libaio.so.1``未安装
```bash
./mysqld: error while loading shared libraries: libaio.so.1: cannot open shared object file: No such file or directory
```
解决方法：
```bash
yum install libaio.so.1
```
2. ``libnuma.so.1``未安装
```bash
./bin/mysqld: error while loading shared libraries: libnuma.so.1: cannot open shared object file: No such file or directory
```
解决方法：
```bash
yum install libnuma.so.1
apt-get install libaio-dev     # ubuntu下解决该问题，可能还需要执行 apt-get -f install
```
3. 服务启动报错
```bash
Starting MySQL.Logging to '/var/log/mysql/mysql.log'.
 ERROR! The server quit without updating PID file (/var/lib/mysql/dbserver.pid).
```
解决方法：
```bash
# /etc/init.d/mysql start 
Starting MySQL.Logging to '/usr/local/mysql/data/dbserver.err'.
 SUCCESS! 
# service mysql start
Starting MySQL SUCCESS! 
```

### UBUNTU系统安装mysql
1. 系统纯净的情况下安装：
```bash
sudo apt-get install mysql-server-5.7
```

2. 如果安装中出现各种莫名其妙的问题，说明环境有问题，处理方法是卸载掉所有mysql相关的库，然后重新安装
需要用到的主要是`dpkg`命令
```bash
$ dpkg --list | grep mysql
ii  mysql-client-5.7                              5.7.27-0ubuntu0.16.04.1                  amd64        MySQL database client binaries
ii  mysql-client-core-5.7                         5.7.27-0ubuntu0.16.04.1                  amd64        MySQL database core client binaries
ii  mysql-common                                  5.7.27-0ubuntu0.16.04.1                  all          MySQL database common files, e.g. /etc/mysql/my.cnf
ii  mysql-server-5.7                              5.7.27-0ubuntu0.16.04.1                  amd64        MySQL database server binaries and system database setup
ii  mysql-server-core-5.7                         5.7.27-0ubuntu0.16.04.1                  amd64        MySQL database server binaries
ii  python-pymysql                                0.7.2-1ubuntu1                           all          Pure-Python MySQL driver - Python 2.x
```
可以看到所有系统已经安装的，或者是之前有人安装的mysql
我们需要做的是先卸载这些所有的库，只要是名称上有mysql的全部卸载掉，命令为：
```bash
sudo dpkg --remove mysql-client-5.7 mysql-client-core-5.7 mysql-common mysql-server mysql-server-5.7 mysql-server-core-5.7
```
或者使用：
```bash
sudo dpkg --purge --remove mysql-server-5.7
```
即纯净模式，删除所有相关的依赖
如果出现还是无法删除的情况，那多数是还是被依赖，把报错出来的相关的包进行删除，比如：
```bash
sudo dpkg --remove libqt4-sql-mysql:amd64
sudo dpkg --remove libmysqlclient20
sudo dpkg --remove libmysqlclient-dev
```
清除干净环境后，就可以重新用上面的命令安装了，正常情况下，会正常安装成功，安装成功的日志如下：
```bash
# shadow @ kickseed in ~/ITPlatform/interfaceManage on git:master x [21:00:39] C:100
$ sudo apt-get install mysql-server-5.7 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libcgi-fast-perl libcgi-pm-perl libevent-core-2.0-5 libfcgi-perl libhtml-template-perl libnuma1 mysql-client-5.7 mysql-client-core-5.7 mysql-common
  mysql-server-core-5.7
Suggested packages:
  libipc-sharedcache-perl mailx tinyca
The following NEW packages will be installed:
  libcgi-fast-perl libcgi-pm-perl libevent-core-2.0-5 libfcgi-perl libhtml-template-perl libnuma1 mysql-client-5.7 mysql-client-core-5.7 mysql-common
  mysql-server-5.7 mysql-server-core-5.7
0 upgraded, 11 newly installed, 0 to remove and 251 not upgraded.
Need to get 14.7 kB/19.0 MB of archives.
After this operation, 162 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrors.aliyun.com/ubuntu xenial-security/main amd64 mysql-common all 5.7.27-0ubuntu0.16.04.1 [14.7 kB]
Fetched 14.7 kB in 0s (191 kB/s)   
Preconfiguring packages ...
Selecting previously unselected package mysql-common.
(Reading database ... 114991 files and directories currently installed.)
Preparing to unpack .../mysql-common_5.7.27-0ubuntu0.16.04.1_all.deb ...
Unpacking mysql-common (5.7.27-0ubuntu0.16.04.1) ...
Selecting previously unselected package libnuma1:amd64.
Preparing to unpack .../libnuma1_2.0.11-1ubuntu1.1_amd64.deb ...
Unpacking libnuma1:amd64 (2.0.11-1ubuntu1.1) ...
Selecting previously unselected package mysql-client-core-5.7.
Preparing to unpack .../mysql-client-core-5.7_5.7.27-0ubuntu0.16.04.1_amd64.deb ...
Unpacking mysql-client-core-5.7 (5.7.27-0ubuntu0.16.04.1) ...
Selecting previously unselected package mysql-client-5.7.
Preparing to unpack .../mysql-client-5.7_5.7.27-0ubuntu0.16.04.1_amd64.deb ...
Unpacking mysql-client-5.7 (5.7.27-0ubuntu0.16.04.1) ...
Selecting previously unselected package mysql-server-core-5.7.
Preparing to unpack .../mysql-server-core-5.7_5.7.27-0ubuntu0.16.04.1_amd64.deb ...
Unpacking mysql-server-core-5.7 (5.7.27-0ubuntu0.16.04.1) ...
Selecting previously unselected package libevent-core-2.0-5:amd64.
Preparing to unpack .../libevent-core-2.0-5_2.0.21-stable-2ubuntu0.16.04.1_amd64.deb ...
Unpacking libevent-core-2.0-5:amd64 (2.0.21-stable-2ubuntu0.16.04.1) ...
Processing triggers for libc-bin (2.23-0ubuntu5) ...
Processing triggers for man-db (2.7.5-1) ...
Setting up mysql-common (5.7.27-0ubuntu0.16.04.1) ...
update-alternatives: using /etc/mysql/my.cnf.fallback to provide /etc/mysql/my.cnf (my.cnf) in auto mode
Selecting previously unselected package mysql-server-5.7.
(Reading database ... 115159 files and directories currently installed.)
Preparing to unpack .../mysql-server-5.7_5.7.27-0ubuntu0.16.04.1_amd64.deb ...
Unpacking mysql-server-5.7 (5.7.27-0ubuntu0.16.04.1) ...
Selecting previously unselected package libcgi-pm-perl.
Preparing to unpack .../libcgi-pm-perl_4.26-1_all.deb ...
Unpacking libcgi-pm-perl (4.26-1) ...
Selecting previously unselected package libfcgi-perl.
Preparing to unpack .../libfcgi-perl_0.77-1build1_amd64.deb ...
Unpacking libfcgi-perl (0.77-1build1) ...
Selecting previously unselected package libcgi-fast-perl.
Preparing to unpack .../libcgi-fast-perl_1%3a2.10-1_all.deb ...
Unpacking libcgi-fast-perl (1:2.10-1) ...
Selecting previously unselected package libhtml-template-perl.
Preparing to unpack .../libhtml-template-perl_2.95-2_all.deb ...
Unpacking libhtml-template-perl (2.95-2) ...
Processing triggers for systemd (229-4ubuntu21.4) ...
Processing triggers for ureadahead (0.100.0-19) ...
Processing triggers for man-db (2.7.5-1) ...
Setting up libnuma1:amd64 (2.0.11-1ubuntu1.1) ...
Setting up mysql-client-core-5.7 (5.7.27-0ubuntu0.16.04.1) ...
Setting up mysql-client-5.7 (5.7.27-0ubuntu0.16.04.1) ...
Setting up mysql-server-core-5.7 (5.7.27-0ubuntu0.16.04.1) ...
Setting up libevent-core-2.0-5:amd64 (2.0.21-stable-2ubuntu0.16.04.1) ...
Setting up mysql-server-5.7 (5.7.27-0ubuntu0.16.04.1) ...
update-alternatives: using /etc/mysql/mysql.cnf to provide /etc/mysql/my.cnf (my.cnf) in auto mode
Renaming removed key_buffer and myisam-recover options (if present)
Setting up libcgi-pm-perl (4.26-1) ...
Setting up libfcgi-perl (0.77-1build1) ...
Setting up libcgi-fast-perl (1:2.10-1) ...
Setting up libhtml-template-perl (2.95-2) ...
Processing triggers for libc-bin (2.23-0ubuntu5) ...
Processing triggers for systemd (229-4ubuntu21.4) ...
Processing triggers for ureadahead (0.100.0-19) ...
(venv) 
# shadow @ kickseed in ~/ITPlatform/interfaceManage on git:master x [21:01:53] 
$ which mysql
/usr/bin/mysql
(venv) 
# shadow @ kickseed in ~/ITPlatform/interfaceManage on git:master x [21:02:00] 
$ mysql -uroot
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
(venv) 
# shadow @ kickseed in ~/ITPlatform/interfaceManage on git:master x [21:02:06] C:1
$ mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.27-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> exit
Bye
```

安装过程中会跳出弹窗，让输入root密码，输入两边后，即会安装成功，记住自己设置的密码就可以登录了。