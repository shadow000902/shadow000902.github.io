---
title: Linux环境安装MySQL
date: 2018-07-21 15:48:15
categories: [MySQL]
tags: [python, mysql]
---

##### 以下内容基于CentOS完成

##### MySQL包下载地址
[32位5.7.22版本下载地址](https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-i686.tar.gz)
[64位5.7.22版本下载地址](https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-x86_64.tar.gz)

  <!--more-->

##### 下载、解压并安装
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

##### 安装和初始化数据库
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
最后的``,:eh<pj(p2NZ``为mysql初始化默认密码。

##### 配置``/etc/my.cnf``
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


##### 初始化报错
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

##### 将``mysqld``服务加入开机自启动项
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

##### 启动``mysql``服务





##### 设置远程登录权限
```bash
mysql> grant all privileges on *.* to'root' @'%' identified by 'root';
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> quit
Bye
```

##### 无密码登录mysql
在``/etc/my.cnf``中加入``skip-grant-tables``

##### 修改mysql默认密码
```bash
mysql> set password='123456';
```

##### 问题解决
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