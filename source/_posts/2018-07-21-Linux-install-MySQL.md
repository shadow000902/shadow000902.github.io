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
#### 使用apt-get安装mysql
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

#### 使用brew安装mysql
```shell
# ubuntu @ VM-4-14-ubuntu in ~ [16:39:03] C:1
$ brew install mysql
Running `brew update --auto-update`...
Error: Failed to download https://formulae.brew.sh/api/cask.jws.json!
==> Downloading https://formulae.brew.sh/api/cask.jws.json
########################################################################################################################################################################################## 100.0%
==> Downloading https://formulae.brew.sh/api/formula_tap_migrations.jws.json
########################################################################################################################################################################################## 100.0%
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
blink                           botan@2                         espflash                        pylyzer                         ruff-lsp                        woof-doom
==> New Casks
apple-hewlett-packard-printer-drivers  drata-agent                            graalvm-jdk                            rio                                    whisky
audiocupcake                           elektron-overbridge                    grs-bluewallet                         rode-connect
chatall                                eset-cyber-security                    mumu-x                                 score
command-x                              flexoptix                              mycard                                 screen-studio
devpod                                 frappe-books                           picoscope                              ths

You have 4 outdated formulae installed.
==> Downloading https://formulae.brew.sh/api/cask_tap_migrations.jws.json
########################################################################################################################################################################################## 100.0%

==> Fetching dependencies for mysql: icu4c, openssl@3, libevent, libcbor, pcre2, dbus, libxcrypt, util-linux, mpdecimal, sqlite, berkeley-db@5, libedit, krb5, libtirpc, libnsl, unzip, python@3.11, glib, libcap, lz4, zstd, systemd, libfido2, protobuf@21, brotli, libunistring, libidn2, libnghttp2, libssh2, openldap, rtmpdump, curl and cyrus-sasl
==> Fetching icu4c
==> Downloading https://ghcr.io/v2/homebrew/core/icu4c/manifests/73.2
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/2e5082de52a2c85ae665e51f8d0de0651611397cb02f4b4e2bb37898ba52a629--icu4c-73.2.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/icu4c/blobs/sha256:714dc987ca9c9b594e6e17c02640f93b49074f81264be16051a93a8f5f674d77
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/d467742181d935c7e6128244f70d5fced229aaf7d1f2b7af9ae1009f663c0f49--icu4c--73.2.x86_64_linux.bottle.tar.gz
==> Fetching openssl@3
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/manifests/3.1.1_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/30a4cb7b3cf5e6879dbfb142a6ecbf65a0fc2e36dec4627348665c0bcc348dcb--openssl@3-3.1.1_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/blobs/sha256:1231b6b95a6c55e775258b4c19b3babbc504a065b984ec6df9d960cf7ffc947b
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/33833a468db1399c62bc53bd3bcd306d3def3cc28f752328b92ede28eb0cb77b--openssl@3--3.1.1_1.x86_64_linux.bottle.tar.gz
==> Fetching libevent
==> Downloading https://ghcr.io/v2/homebrew/core/libevent/manifests/2.1.12_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/68b113f9ab63db45f4e1860de522ce2ca4fa081eb3c0d5c7d6005a35c3cf8d06--libevent-2.1.12_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libevent/blobs/sha256:83ef4ce689a91f6fca013d6b4b0b2fcda3706080f8e0cccd056a3d94d6bc0f17
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/694835ad258e8dc6e9758f34fd0f18013d7a61f2a6ac1ca0e481f652d80b086a--libevent--2.1.12_1.x86_64_linux.bottle.tar.gz
==> Fetching libcbor
==> Downloading https://ghcr.io/v2/homebrew/core/libcbor/manifests/0.10.2
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/b3b69aa10b9eff19299a02bde62661644cfd29b742e5e5bb197e70c03b8f4d96--libcbor-0.10.2.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libcbor/blobs/sha256:0c532bdfe6b9efb37ff7cd43d1fcf2def27aefbffbea09093cecf16f95adc198
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/f6d81f223b81ac56d58b624409ac9b60e17b6ea18ce51d61e5a0e1f56b751e6c--libcbor--0.10.2.x86_64_linux.bottle.tar.gz
==> Fetching pcre2
==> Downloading https://ghcr.io/v2/homebrew/core/pcre2/manifests/10.42
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/6a53794fcaabc5cc5e05b19c02ca9c4c5f2cb9a4d65a5790a6841146465b040f--pcre2-10.42.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/pcre2/blobs/sha256:6fb73ccbfd7f7d48b9400512ded73383a19dc54ec015ab1aab2b849480c3b3f8
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/9195332009f1485200ff410fafd513e4d339be267d4b8bbeb15d20556558c33f--pcre2--10.42.x86_64_linux.bottle.tar.gz
==> Fetching dbus
==> Downloading https://ghcr.io/v2/homebrew/core/dbus/manifests/1.14.8
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/3c5f9d9d68c9be7706a0e09b6bf728f60e829d09e300ad19d64058133c4fde61--dbus-1.14.8.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/dbus/blobs/sha256:e317deee5c58aea9757d6a84537a5b54532e593a366901005786b9f4d00fb00f
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/2b9f4c39f7bb2fc88a83183d7e136ed713c026c5284f780061344f81e591d2e3--dbus--1.14.8.x86_64_linux.bottle.tar.gz
==> Fetching libxcrypt
==> Downloading https://ghcr.io/v2/homebrew/core/libxcrypt/manifests/4.4.36
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/950e230307625f9e57d74f0076caab42b6c67a325c70b83efa2c9cc84be1f839--libxcrypt-4.4.36.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libxcrypt/blobs/sha256:ad1c4b570d7a66046038c13345b54337d858a2db78dcfb7e90a2b21adc1d6802
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/8a89cd46e87dade4849639585d2fd436fa581e9d21471f24e76e590d177c095f--libxcrypt--4.4.36.x86_64_linux.bottle.tar.gz
==> Fetching util-linux
==> Downloading https://ghcr.io/v2/homebrew/core/util-linux/manifests/2.39.1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/ab19c77ba7ed43a7bf3be64312099e176d64e319f12d8cf9e4925dc2f3f80548--util-linux-2.39.1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/util-linux/blobs/sha256:3e38d81b856507fb126b26eaba4d20459dbe06993e26e798786954de730052ab
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/735dc2b32f5c3930622c0c132830c39bfd9c57acd688e558ea471c67f7034a9b--util-linux--2.39.1.x86_64_linux.bottle.tar.gz
==> Fetching mpdecimal
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/2.5.1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/f367c2ee08c56b88be0662703a8e4275f8657608a268c8c44e845154b0cea543--mpdecimal-2.5.1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/blobs/sha256:c5d64a4dd47dc1b66887c0cecd884f0848a801cb2f684cde0f4664e709574067
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/e02dc86f10704b9aeb72336cbffeb0d490260c2d5d976556c00f8d9fce6bef03--mpdecimal--2.5.1.x86_64_linux.bottle.tar.gz
==> Fetching sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.42.0
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/9054dbd2014cfa67115dbd42da881a047783b58c96344ba1d65317539985b631--sqlite-3.42.0.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/blobs/sha256:8226fd550248842674a281032e758b0f2fd1f0d7dd543f6eb78512b1edf00ad5
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/aae9b14e25dc720feab29f6ba2b1e54edbb4502703c3ed5cb2d86dfd25e9c4f9--sqlite--3.42.0.x86_64_linux.bottle.tar.gz
==> Fetching berkeley-db@5
==> Downloading https://ghcr.io/v2/homebrew/core/berkeley-db/5/manifests/5.3.28_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/17e4e0def00184b561c8a490b5c0813a7c4f5e1365eb2e927570786eb4e05e09--berkeley-db@5-5.3.28_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/berkeley-db/5/blobs/sha256:c0e2906cc6657dc497fec75629560b0a404b81cebadf5e10c1f70616a14fa886
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/8b5fb485cdbb78c808921aeee52f32eadf4dc239fa5c03df690e316a1f9f4021--berkeley-db@5--5.3.28_1.x86_64_linux.bottle.tar.gz
==> Fetching libedit
==> Downloading https://ghcr.io/v2/homebrew/core/libedit/manifests/20221030-3.1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/fb5226448ca27f1779ac14bd7419ae08a24df67c516a919bd176b81ad0896390--libedit-20221030-3.1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libedit/blobs/sha256:bee1f6bfb90dd3c9b26ce4732e04025a468fe2fa29d63049cb0aa2a888e610d2
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/cb584d6de2880054c41aceb962c287de5101444edfd2611e6afdb4aee428cca9--libedit--20221030-3.1.x86_64_linux.bottle.tar.gz
==> Fetching krb5
==> Downloading https://ghcr.io/v2/homebrew/core/krb5/manifests/1.21_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/32c98b39241cf26de27624b054208954d379c44c1ea6895a726ee27bdea76260--krb5-1.21_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/krb5/blobs/sha256:cb324a8c5a6c8f60143a4e24f235c0955183a7262c5a2fc6c08a3a9408645f99
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/8af61a009a5d99e012ed5e2c5ebb522bfe060d9e9d02daf8aa04f7a5891e1bc6--krb5--1.21_1.x86_64_linux.bottle.tar.gz
==> Fetching libtirpc
==> Downloading https://ghcr.io/v2/homebrew/core/libtirpc/manifests/1.3.3
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/8855f5ef631c25ab1532940cd26ad4e298df26b4414ccd1426becf1b4ed7a3f9--libtirpc-1.3.3.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libtirpc/blobs/sha256:26371c5e683f16a4b2ebf4475150672f76d45e3d43583c942fcb0e916be77dc3
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/5fff9750e00be58fcd7274922fd551422a2b885f50e849d9af74a44e659317f1--libtirpc--1.3.3.x86_64_linux.bottle.tar.gz
==> Fetching libnsl
==> Downloading https://ghcr.io/v2/homebrew/core/libnsl/manifests/2.0.0_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/86e8a2a3ce4c0d286a9ff3a6776bfbbf67e8e9aefa48596a6149f09457bde4ef--libnsl-2.0.0_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libnsl/blobs/sha256:ed70b285939e2ab21ba53d122ce2d4beab4cd0f9c86925c3d3a2cfb1b0eeecb3
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/c9eaf36a8d19f53ae16de75047a0662fb77c2865d66e83a3b90391ace3a79617--libnsl--2.0.0_1.x86_64_linux.bottle.tar.gz
==> Fetching unzip
==> Downloading https://ghcr.io/v2/homebrew/core/unzip/manifests/6.0_8
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/b9a98c1a65dea38eb0bb5d9106a5758ed0ff17635811bd7f7cd6be5908c2961b--unzip-6.0_8.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/unzip/blobs/sha256:baf15e19852a0f9756e3302fa6f3866eaeccc06730c9907bffc19f32861d64bf
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/b21864e34ef4cb82ce78fcf50f8d91e7b3525e695b095c7d006c15cd802eefbb--unzip--6.0_8.x86_64_linux.bottle.tar.gz
==> Fetching python@3.11
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/manifests/3.11.4_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/c009c3cb6566d4e36121a40c85204870afab2b9c86263b1d38d3c672361c6cb1--python@3.11-3.11.4_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/blobs/sha256:7e8892393a9df0437e1ada50c011df549867348fe12e998d8d659da77379aa07
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/56dabc6f51c30c659a7b638dc2e0db03ee0abfb654824bfbc7f56eacbeb68a75--python@3.11--3.11.4_1.x86_64_linux.bottle.tar.gz
==> Fetching glib
==> Downloading https://ghcr.io/v2/homebrew/core/glib/manifests/2.76.4
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/948354b81d1afa62d6c2c2bb260e244d78249c041da621692ead9cdee06fc7f8--glib-2.76.4.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/glib/blobs/sha256:a66ad2580fe4a040cb0c0d51b37772d6d8df4b5505e2d6f6d87c82471d7adcaa
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/7cce68ea37f6935ce98a383b9400218c3424c4896c03068d01a28b295899c272--glib--2.76.4.x86_64_linux.bottle.tar.gz
==> Fetching libcap
==> Downloading https://ghcr.io/v2/homebrew/core/libcap/manifests/2.69
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/686c24487732ef743b26325cb6d31abae653b97d379a56729a3dd5a6ffe85fd6--libcap-2.69.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libcap/blobs/sha256:c76a15fd8bef73c4c24174992f4507ae01260b7e2a6864e7e528acd93f1f488f
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/e3a42780561a92d24c64a550297443785c41440945d5bc9edd7e907ed3100d22--libcap--2.69.x86_64_linux.bottle.tar.gz
==> Fetching lz4
==> Downloading https://ghcr.io/v2/homebrew/core/lz4/manifests/1.9.4
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/379e59b981667f9585b33a2ff318769d8edca3ce6fd2e9a67ed291ae3e0cc872--lz4-1.9.4.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/lz4/blobs/sha256:1757fefc3840e11c4822e4c2a95aa62aca44a4eaccce6f5c414ea51d1e58bf8e
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/0e1822b21340968e08a38ebad2df2a2007600450c01d984e82071a679ae9b419--lz4--1.9.4.x86_64_linux.bottle.tar.gz
==> Fetching zstd
==> Downloading https://ghcr.io/v2/homebrew/core/zstd/manifests/1.5.5
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/0afc423c03e4ef9c6e5a0a9bd0833be3f24fe4d17390e10342137f0d1b53dbf7--zstd-1.5.5.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/zstd/blobs/sha256:68c8655224f058316c16462507b6cdd061bd546e161bf8419c68ca526d3a9a48
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/bc77edd851b4d46b2f563b6dc3edff96e6230c9fac665fd0cb8ffe20a4280cfd--zstd--1.5.5.x86_64_linux.bottle.tar.gz
==> Fetching systemd
==> Downloading https://ghcr.io/v2/homebrew/core/systemd/manifests/253.6
########################################################################################################################################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/systemd/blobs/sha256:002ce9cec2c8050ab3273e9c8fea98ed90b3d59260fc792440b9f1845c01e7ad
########################################################################################################################################################################################## 100.0%
==> Fetching libfido2
==> Downloading https://ghcr.io/v2/homebrew/core/libfido2/manifests/1.13.0_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/45bf50ee4ed0a5bef8bd7337de5554ff6b69e7b3dc2848d8e971a12d28b6ec0f--libfido2-1.13.0_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libfido2/blobs/sha256:54a0268ea3f24f5d9f0c4bfbe997d425d7f2f133c4df6f8ebe8c87bf7e76372f
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/5d1fee224f250026e4cd1bd966657e41ae1651b68537080f340d1046ada77e4b--libfido2--1.13.0_1.x86_64_linux.bottle.tar.gz
==> Fetching protobuf@21
==> Downloading https://ghcr.io/v2/homebrew/core/protobuf/21/manifests/21.12
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/9f24cec38d165f7984e74442740f777284ab3ead474a5ebc3838c58635419111--protobuf@21-21.12.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/protobuf/21/blobs/sha256:57404e662da5768d45c06790cd227171205fcc0e1f775d4e1f2a91cad8ec45cc
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/ee7198a3a8e7ea8a5081e161de87ceac018071feca856132cd7677457ba71ef7--protobuf@21--21.12.x86_64_linux.bottle.tar.gz
==> Fetching brotli
==> Downloading https://ghcr.io/v2/homebrew/core/brotli/manifests/1.0.9
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/922ce7b351cec833f9bd2641f27d8ac011005f8b1f7e1119b8271cfb4c0d3cd7--brotli-1.0.9.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/brotli/blobs/sha256:97756cdd4ee7ca03251307eafdb3dff7be3f070a8c0fdf385e87e7ad4a1068de
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/be14053abf40a4424e57a05dbcf0a241f0fd10f0fc3c19426dbd25f37720e533--brotli--1.0.9.x86_64_linux.bottle.tar.gz
==> Fetching libunistring
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/manifests/1.1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/a34801f1ad5800ba51b2b3951d82a913ccf0641982f86b02df2f0aa182535055--libunistring-1.1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/blobs/sha256:252f3716191a8c08f8d10e2c20b84cf9645e2c264f409f58d3255d9a4edce77f
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/acc8b5bda4be9c1f9fb5016ebed59e76f37c87c5ead566f58f79aa3064cfbbe1--libunistring--1.1.x86_64_linux.bottle.tar.gz
==> Fetching libidn2
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/manifests/2.3.4_1-1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/03ad193177f4e7d05ee2ed19a455028cb5fbf7ea1a812d88f18f5e9e8b4a4d43--libidn2-2.3.4_1-1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/blobs/sha256:af78945967847cdf33779abbd1142cabb31d6b5d428f367e23bc068f1d240e49
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/bc61c7d91e776e8967178a1ff72134e7d5a797c3db23c0c90e45612f99815fe0--libidn2--2.3.4_1.x86_64_linux.bottle.1.tar.gz
==> Fetching libnghttp2
==> Downloading https://ghcr.io/v2/homebrew/core/libnghttp2/manifests/1.54.0
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/44bf2473b9a633f7b958b0e0d691180f8618f4bec47778672bd9758948fdde1f--libnghttp2-1.54.0.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libnghttp2/blobs/sha256:c5ea523e4a8618aae652c01e9695ab274571e13f2db926910202dea089d7336d
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/193b0388c2733e1c9ac4ff0f253035095c5f8b8485bba7168d0b907e404ca7cc--libnghttp2--1.54.0.x86_64_linux.bottle.tar.gz
==> Fetching libssh2
==> Downloading https://ghcr.io/v2/homebrew/core/libssh2/manifests/1.11.0_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/48ca0c7785b21630a4817c59b72205609ccb0575e7abc64d64af2e61a60b5b0a--libssh2-1.11.0_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/libssh2/blobs/sha256:57746d26d6d96b0ba3a7b7021b8f13a466685e8a2172fa49bf4cb44d91d24429
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/dd2e47d97bc9571f46d4876b2ae13568f5ceff7cfb9b99d955fa8d4d262afd3a--libssh2--1.11.0_1.x86_64_linux.bottle.tar.gz
==> Fetching openldap
==> Downloading https://ghcr.io/v2/homebrew/core/openldap/manifests/2.6.5
########################################################################################################################################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openldap/blobs/sha256:acc12b445557a8b4c5872e7fae4653e36ccc74b618c9bd82eb40f28c7618e0b6
########################################################################################################################################################################################## 100.0%
==> Fetching rtmpdump
==> Downloading https://ghcr.io/v2/homebrew/core/rtmpdump/manifests/2.4.20151223_2
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/9cc68d151bcde6dce7c43dbbb240d184da5bffbb50ee3f345ca291ce52d3a4d5--rtmpdump-2.4+20151223_2.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/rtmpdump/blobs/sha256:d051297b563e80fbcff1a9006ae9fa0ce66280716322fa58a669298d73407e6f
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/fdaa004be81732c1b57b752b441481a3672510077bf7f7869a01687d213b654f--rtmpdump--2.4+20151223_2.x86_64_linux.bottle.tar.gz
==> Fetching curl
==> Downloading https://ghcr.io/v2/homebrew/core/curl/manifests/8.1.2_1
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/4a6e1184385038c60152e94e38e334f9468b728d7a029833b9d4bb64a93fbebd--curl-8.1.2_1.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/curl/blobs/sha256:02b3b8dde04541f3fe2e0cd4c996909597cf9dd3473a1e298d21e25853529082
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/92f0b26272b01dfcad285b2995ef379c47d86f62313b06a12218302a8507e727--curl--8.1.2_1.x86_64_linux.bottle.tar.gz
==> Fetching cyrus-sasl
==> Downloading https://ghcr.io/v2/homebrew/core/cyrus-sasl/manifests/2.1.28_2
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/1b83b1c4579a3298a1011c9418ccdf6449e5bb9797de00bca7d20dfbff820257--cyrus-sasl-2.1.28_2.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/cyrus-sasl/blobs/sha256:f1bc6d528c1c0e53c2eecb599e5127070654a7bdfb9acb0232cfd08bfaf38efd
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/a8f7183cca0be88bce3698861d233ac60f48d72b1c84fab941bde64a0c128119--cyrus-sasl--2.1.28_2.x86_64_linux.bottle.tar.gz
==> Fetching mysql
==> Downloading https://ghcr.io/v2/homebrew/core/mysql/manifests/8.0.33_3
Already downloaded: /home/ubuntu/.cache/Homebrew/downloads/a1894ed626d297a083fba6b13f7cdb7725c2df94967d7ccbcae44b27f3fdb5ea--mysql-8.0.33_3.bottle_manifest.json
==> Downloading https://ghcr.io/v2/homebrew/core/mysql/blobs/sha256:e81e56785691e7ea4d0af44e4ce5d73035bc09959b9b80ea2300d1df66ef2958
########################################################################################################################################################################################## 100.0%
==> Installing dependencies for mysql: icu4c, openssl@3, libevent, libcbor, pcre2, dbus, libxcrypt, util-linux, mpdecimal, sqlite, berkeley-db@5, libedit, krb5, libtirpc, libnsl, unzip, python@3.11, glib, libcap, lz4, zstd, systemd, libfido2, protobuf@21, brotli, libunistring, libidn2, libnghttp2, libssh2, openldap, rtmpdump, curl and cyrus-sasl
==> Installing mysql dependency: icu4c
==> Pouring icu4c--73.2.x86_64_linux.bottle.tar.gz
==> Downloading https://formulae.brew.sh/api/cask.jws.json
########################################################################################################################################################################################## 100.0%
🍺  /home/linuxbrew/.linuxbrew/Cellar/icu4c/73.2: 268 files, 87.1MB
==> Installing mysql dependency: openssl@3
==> Pouring openssl@3--3.1.1_1.x86_64_linux.bottle.tar.gz
Unlinking /home/linuxbrew/.linuxbrew/Cellar/openssl@1.1/1.1.1u... 3999 symlinks removed.
==> Downloading https://formulae.brew.sh/api/formula.jws.json
########################################################################################################################################################################################## 100.0%
🍺  /home/linuxbrew/.linuxbrew/Cellar/openssl@3/3.1.1_1: 6,820 files, 38.2MB
==> Installing mysql dependency: libevent
==> Pouring libevent--2.1.12_1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libevent/2.1.12_1: 62 files, 2.6MB
==> Installing mysql dependency: libcbor
==> Pouring libcbor--0.10.2.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libcbor/0.10.2: 31 files, 218.7KB
==> Installing mysql dependency: pcre2
==> Pouring pcre2--10.42.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/pcre2/10.42: 234 files, 7MB
==> Installing mysql dependency: dbus
==> Pouring dbus--1.14.8.x86_64_linux.bottle.tar.gz
==> /home/linuxbrew/.linuxbrew/Cellar/dbus/1.14.8/bin/dbus-uuidgen --ensure=/home/linuxbrew/.linuxbrew/var/lib/dbus/machine-id
🍺  /home/linuxbrew/.linuxbrew/Cellar/dbus/1.14.8: 77 files, 2.9MB
==> Installing mysql dependency: libxcrypt
==> Pouring libxcrypt--4.4.36.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libxcrypt/4.4.36: 24 files, 369.2KB
==> Installing mysql dependency: util-linux
==> Pouring util-linux--2.39.1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/util-linux/2.39.1: 410 files, 23.9MB
==> Installing mysql dependency: mpdecimal
==> Pouring mpdecimal--2.5.1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/mpdecimal/2.5.1: 71 files, 2.4MB
==> Installing mysql dependency: sqlite
==> Pouring sqlite--3.42.0.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/sqlite/3.42.0: 12 files, 5.8MB
==> Installing mysql dependency: berkeley-db@5
==> Pouring berkeley-db@5--5.3.28_1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/berkeley-db@5/5.3.28_1: 5,271 files, 87.7MB
==> Installing mysql dependency: libedit
==> Pouring libedit--20221030-3.1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libedit/20221030-3.1: 54 files, 791.9KB
==> Installing mysql dependency: krb5
==> Pouring krb5--1.21_1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/krb5/1.21_1: 163 files, 5.3MB
==> Installing mysql dependency: libtirpc
==> Pouring libtirpc--1.3.3.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libtirpc/1.3.3: 85 files, 1MB
==> Installing mysql dependency: libnsl
==> Pouring libnsl--2.0.0_1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libnsl/2.0.0_1: 18 files, 182.2KB
==> Installing mysql dependency: unzip
==> Pouring unzip--6.0_8.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/unzip/6.0_8: 16 files, 597.1KB
==> Installing mysql dependency: python@3.11
==> Pouring python@3.11--3.11.4_1.x86_64_linux.bottle.tar.gz
==> /home/linuxbrew/.linuxbrew/Cellar/python@3.11/3.11.4_1/bin/python3.11 -m ensurepip
==> /home/linuxbrew/.linuxbrew/Cellar/python@3.11/3.11.4_1/bin/python3.11 -m pip install -v --no-deps --no-index --upgrade --isolated --target=/home/linuxbrew/.linuxbrew/lib/python3.11/site-pac
🍺  /home/linuxbrew/.linuxbrew/Cellar/python@3.11/3.11.4_1: 2,845 files, 67.3MB
==> Installing mysql dependency: glib
==> Pouring glib--2.76.4.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/glib/2.76.4: 462 files, 26.1MB
==> Installing mysql dependency: libcap
==> Pouring libcap--2.69.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libcap/2.69: 99 files, 464KB
==> Installing mysql dependency: lz4
==> Pouring lz4--1.9.4.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/lz4/1.9.4: 22 files, 695.3KB
==> Installing mysql dependency: zstd
==> Pouring zstd--1.5.5.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/zstd/1.5.5: 31 files, 3.2MB
==> Installing mysql dependency: systemd
==> Pouring systemd--253.6.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/systemd/253.6: 663 files, 23.0MB
==> Installing mysql dependency: libfido2
==> Pouring libfido2--1.13.0_1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libfido2/1.13.0_1: 548 files, 1.6MB
==> Installing mysql dependency: protobuf@21
==> Pouring protobuf@21--21.12.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/protobuf@21/21.12: 288 files, 38.4MB
==> Installing mysql dependency: brotli
==> Pouring brotli--1.0.9.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/brotli/1.0.9: 25 files, 2.5MB
==> Installing mysql dependency: libunistring
==> Pouring libunistring--1.1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libunistring/1.1: 57 files, 5.5MB
==> Installing mysql dependency: libidn2
==> Pouring libidn2--2.3.4_1.x86_64_linux.bottle.1.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libidn2/2.3.4_1: 80 files, 1.2MB
==> Installing mysql dependency: libnghttp2
==> Pouring libnghttp2--1.54.0.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libnghttp2/1.54.0: 14 files, 832.8KB
==> Installing mysql dependency: libssh2
==> Pouring libssh2--1.11.0_1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/libssh2/1.11.0_1: 198 files, 1.4MB
==> Installing mysql dependency: openldap
==> Pouring openldap--2.6.5.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/openldap/2.6.5: 85 files, 7.9MB
==> Installing mysql dependency: rtmpdump
==> Pouring rtmpdump--2.4+20151223_2.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/rtmpdump/2.4+20151223_2: 20 files, 624.1KB
==> Installing mysql dependency: curl
==> Pouring curl--8.1.2_1.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/curl/8.1.2_1: 511 files, 5.0MB
==> Installing mysql dependency: cyrus-sasl
==> Pouring cyrus-sasl--2.1.28_2.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/cyrus-sasl/2.1.28_2: 89 files, 1.1MB
==> Installing mysql
==> Pouring mysql--8.0.33_3.x86_64_linux.bottle.tar.gz
==> /home/linuxbrew/.linuxbrew/Cellar/mysql/8.0.33_3/bin/mysqld --initialize-insecure --user=ubuntu --basedir=/home/linuxbrew/.linuxbrew/Cellar/mysql/8.0.33_3 --datadir=/home/linuxbrew/.linuxbr
==> Caveats
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -u root

To start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  /home/linuxbrew/.linuxbrew/opt/mysql/bin/mysqld_safe --datadir=/home/linuxbrew/.linuxbrew/var/mysql
==> Summary
🍺  /home/linuxbrew/.linuxbrew/Cellar/mysql/8.0.33_3: 320 files, 360.8MB
==> Running `brew cleanup mysql`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Upgrading 1 dependent of upgraded formulae:
Disable this behaviour by setting HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
pyenv 2.3.18 -> 2.3.22
==> Fetching dependencies for pyenv: berkeley-db
==> Fetching berkeley-db
==> Downloading https://ghcr.io/v2/homebrew/core/berkeley-db/manifests/18.1.40_2
########################################################################################################################################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/berkeley-db/blobs/sha256:3ba948d2977fbfcc865086fab6d6567b4f3972fcc46e327817fb7600f64d4312
########################################################################################################################################################################################## 100.0%
==> Fetching pyenv
==> Downloading https://ghcr.io/v2/homebrew/core/pyenv/manifests/2.3.22
########################################################################################################################################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/pyenv/blobs/sha256:350eeb5f925813f78110c2e2492bfae3da6d71ba0e931124ed90a78b39fa9137
########################################################################################################################################################################################## 100.0%
==> Upgrading pyenv
  2.3.18 -> 2.3.22

==> Installing dependencies for pyenv: berkeley-db
==> Installing pyenv dependency: berkeley-db
==> Pouring berkeley-db--18.1.40_2.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/berkeley-db/18.1.40_2: 44 files, 8.2MB
==> Installing pyenv
==> Pouring pyenv--2.3.22.x86_64_linux.bottle.tar.gz
🍺  /home/linuxbrew/.linuxbrew/Cellar/pyenv/2.3.22: 1,086 files, 4.2MB
==> Running `brew cleanup pyenv`...
Removing: /home/linuxbrew/.linuxbrew/Cellar/pyenv/2.3.18... (1,067 files, 4.1MB)
==> Checking for dependents of upgraded formulae...
==> No broken dependents found!
==> Caveats
==> mysql
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -u root

To start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  /home/linuxbrew/.linuxbrew/opt/mysql/bin/mysqld_safe --datadir=/home/linuxbrew/.linuxbrew/var/mysql

# ubuntu @ VM-4-14-ubuntu in ~ [14:23:34] C:1
$ brew services start mysql
==> Tapping homebrew/services
Cloning into '/home/linuxbrew/.linuxbrew/Homebrew/Library/Taps/homebrew/homebrew-services'...
remote: Enumerating objects: 2461, done.
remote: Counting objects: 100% (2461/2461), done.
remote: Compressing objects: 100% (1173/1173), done.
remote: Total 2461 (delta 1152), reused 2344 (delta 1100), pack-reused 0
Receiving objects: 100% (2461/2461), 672.89 KiB | 1.93 MiB/s, done.
Resolving deltas: 100% (1152/1152), done.
Tapped 1 command (45 files, 950.0KB).
Created symlink /home/ubuntu/.config/systemd/user/default.target.wants/homebrew.mysql.service → /home/ubuntu/.config/systemd/user/homebrew.mysql.service.
==> Successfully started `mysql` (label: homebrew.mysql)

# ubuntu @ VM-4-14-ubuntu in ~ [14:26:08]
$ mysql_secure_installation

Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: Y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
Please set the password for root here.

New password:

Re-enter new password:

Estimated strength of the password: 50
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : Y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : Y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : q

 ... skipping.
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : Y
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : Y
Success.

All done!
```

### Mac环境安装MySQL

```bash
# taoyi @ tysYZMac in ~ [11:01:18]
$ brew install mysql
Running `brew update --auto-update`...
Installing from the API is now the default behaviour!
You can save space and time by running:
  brew untap homebrew/core
==> Downloading https://formulae.brew.sh/api/formula_tap_migrations.jws.json
############################################################################################################################################### 100.0%
==> Auto-updated Homebrew!
Updated 3 taps (homebrew/services, homebrew/core and homebrew/cask).
==> New Formulae
access                        cycode                        joshuto                       mods                          shush
adb-enhanced                  ddns-go                       jsign                         nerdfix                       sickchill
aftman                        debugbreak                    jsmn                          nexttrace                     slsa-verifier
alass                         driftwood                     judy                          ntbtls                        spotify_player
ansible@7                     dtools                        libabigail                    openfga                       ssocr
apko                          dzr                           libclc                        ord                           staq
argparse                      erlang@25                     libdivsufsort                 pocketbase                    svlint
ast-grep                      fastgron                      libecpint                     procps@3                      svls
aws-amplify                   forgit                        libfastjson                   protobuf@21                   swift-outdated
bashate                       fuc                           libgedit-gtksourceview        proxygen                      tailwindcss-language-server
bbot                          fw                            libint                        pypy3.10                      tern
bilix                         gcc@12                        liblxi                        pypy3.9                       trufflehog
blades                        getmail6                      libmediainfo                  python-toml                   trzsz-ssh
boolector                     gffread                       libomemo-c                    quantum++                     typical
cargo-binstall                git-credential-oauth          libpaho-mqtt                  rio                           virtualfish
cargo-generate                git-tools                     libversion                    roblox-ts                     votca
cbonsai                       gitoxide                      libzen                        rojo                          wally
charls                        go-feature-flag               lowdown                       runme                         wzprof
clive                         gotestsum                     lpeg                          rye                           xbyak
conda-lock                    grpc@1.54                     lr                            safeint                       xe
convco                        grype                         ls-lint                       scrapy                        yamlfmt
core-lightning                hex                           mariadb@10.11                 sh4d0wup                      zchunk
cppinsights                   hivex                         melange                       shodan                        zrok
crabz                         jet                           minigraph                     shub
==> New Casks
1kc-razer                                                                   lg-onscreen-control
apple-hewlett-packard-printer-drivers                                       linn-konfig
asix-ax88179                                                                llamachat
audiocupcake                                                                lo-rain
bloop                                                                       logitune
bookletcreator                                                              loupedeck
bose-updater                                                                motu-m-series
caldigit-docking-utility                                                    mumu-x
caldigit-thunderbolt-charging                                               music-miniplayer
chatall                                                                     music-remote
chatbox                                                                     music-widget
command-x                                                                   mycard
concept2-utility                                                            nordic-nrf-command-line-tools
copilot                                                                     obsbot-webcam
craft                                                                       opal
creative                                                                    pallotron-yubiswitch
dadroit-json-viewer                                                         philips-hue-sync
ddpm                                                                        picoscope
devpod                                                                      pololu-avr-programmer-v2
dintch                                                                      processmonitor
drata-agent                                                                 qflipper
elektron-overbridge                                                         red-canary-mac-monitor
engine-dj                                                                   rio
entry                                                                       rode-connect
eobcanka                                                                    saleae-logic
eset-cyber-security                                                         samsung-portable-ssd-t7
eu                                                                          score
eusamanager                                                                 screen-studio
filemonitor                                                                 shureplus-motiv
firefly-shimmer                                                             skiff
flexoptix                                                                   smooze-pro
focusrite-control                                                           submariner
fractal-bot                                                                 synology-cloud-station-backup
frappe-books                                                                synology-photo-station-uploader
genesys-cloud                                                               synology-surveillance-station-client
graalvm-jdk                                                                 synologyassistant
grs-bluewallet                                                              tea
hdhomerun                                                                   ths
hp-easy-start                                                               tiptoi-manager
huiontablet                                                                 uhk-agent
insta360-studio                                                             volta
jabra-direct                                                                wacom-tablet
kiibohd-configurator                                                        whisky
konica-minolta-bizhub-c759-c658-c368-c287-c3851-driver                      yealink-meeting
lasso                                                                       zsa-wally

You have 12 outdated formulae installed.
==> Downloading https://formulae.brew.sh/api/cask_tap_migrations.jws.json
############################################################################################################################################### 100.0%

==> Fetching dependencies for mysql: icu4c, ca-certificates, openssl@3, libevent, libcbor, libfido2, lz4, protobuf@21, zlib, xz and zstd
==> Fetching icu4c
==> Downloading https://ghcr.io/v2/homebrew/core/icu4c/manifests/73.2
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/icu4c/blobs/sha256:953797d46546c570c4fab4e8b2395624ae90acd492f75b68ff99fbd115ccd748
############################################################################################################################################### 100.0%
==> Fetching ca-certificates
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2023-05-30
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:f664c0f185677a82689ada2a4e35c555e48885e6c2fb5e2dfcc82d9fb79cf870
############################################################################################################################################### 100.0%
==> Fetching openssl@3
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/manifests/3.1.1_1
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/blobs/sha256:c4366444ddd5f55ff7dc1cb24a81c01f6ba946e255556af9c641da17142d472e
############################################################################################################################################### 100.0%
==> Fetching libevent
==> Downloading https://ghcr.io/v2/homebrew/core/libevent/manifests/2.1.12_1
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libevent/blobs/sha256:a75d453a7fe2aba1eaba334621b7bd9f0ff6f9e1f04aa400565f68711a9f6db4
############################################################################################################################################### 100.0%
==> Fetching libcbor
==> Downloading https://ghcr.io/v2/homebrew/core/libcbor/manifests/0.10.2
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libcbor/blobs/sha256:ee1e77e1e6cef7ba754d1757f7aa038e34b139466f789231b672e389a194a5fc
############################################################################################################################################### 100.0%
==> Fetching libfido2
==> Downloading https://ghcr.io/v2/homebrew/core/libfido2/manifests/1.13.0_1
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libfido2/blobs/sha256:92ec60d842d0f283bf1d5f3e063aee439cbe1bfdb3b458556caa0dabeed3d0e1
############################################################################################################################################### 100.0%
==> Fetching lz4
==> Downloading https://ghcr.io/v2/homebrew/core/lz4/manifests/1.9.4
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/lz4/blobs/sha256:cd29e40287b0a2d665a647acbea5512e8db4c371687147aab5c60bf9059b2cca
############################################################################################################################################### 100.0%
==> Fetching protobuf@21
==> Downloading https://ghcr.io/v2/homebrew/core/protobuf/21/manifests/21.12
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/protobuf/21/blobs/sha256:d0909077ab9abd27d47a7990c7bcea6622805421de263ff5a5366beef171bf74
############################################################################################################################################### 100.0%
==> Fetching zlib
==> Downloading https://ghcr.io/v2/homebrew/core/zlib/manifests/1.2.13-1
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/zlib/blobs/sha256:565286ede6cc691fb781b96a76235d714159bf47c7af2cadbca01bffa92bd785
############################################################################################################################################### 100.0%
==> Fetching xz
==> Downloading https://ghcr.io/v2/homebrew/core/xz/manifests/5.4.3
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/xz/blobs/sha256:179cc5316bed5c452aa1658a2a100bc8cd1b210d79c0f2fffec4934fd1f4cd8a
############################################################################################################################################### 100.0%
==> Fetching zstd
==> Downloading https://ghcr.io/v2/homebrew/core/zstd/manifests/1.5.5
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/zstd/blobs/sha256:b709835f4cd5d339b97103f0dfa343489a02d2073f8e80ba7b04d682f1d29bd4
############################################################################################################################################### 100.0%
==> Fetching mysql
==> Downloading https://ghcr.io/v2/homebrew/core/mysql/manifests/8.0.33_3
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/mysql/blobs/sha256:11af549049440ae84f55b8458528d0221e82f48f684e3fc05986072ee0c3c64f
############################################################################################################################################### 100.0%
==> Installing dependencies for mysql: icu4c, ca-certificates, openssl@3, libevent, libcbor, libfido2, lz4, protobuf@21, zlib, xz and zstd
==> Installing mysql dependency: icu4c
==> Pouring icu4c--73.2.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/icu4c/73.2: 268 files, 80.1MB
==> Installing mysql dependency: ca-certificates
==> Pouring ca-certificates--2023-05-30.arm64_ventura.bottle.tar.gz
==> Regenerating CA certificate bundle from keychain, this may take a while...
🍺  /opt/homebrew/Cellar/ca-certificates/2023-05-30: 3 files, 216.2KB
==> Installing mysql dependency: openssl@3
==> Pouring openssl@3--3.1.1_1.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openssl@3/3.1.1_1: 6,495 files, 28.4MB
==> Installing mysql dependency: libevent
==> Pouring libevent--2.1.12_1.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libevent/2.1.12_1: 57 files, 2.2MB
==> Installing mysql dependency: libcbor
==> Pouring libcbor--0.10.2.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libcbor/0.10.2: 31 files, 193.7KB
==> Installing mysql dependency: libfido2
==> Pouring libfido2--1.13.0_1.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libfido2/1.13.0_1: 547 files, 1.3MB
==> Installing mysql dependency: lz4
==> Pouring lz4--1.9.4.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/lz4/1.9.4: 22 files, 680.1KB
==> Installing mysql dependency: protobuf@21
==> Pouring protobuf@21--21.12.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/protobuf@21/21.12: 288 files, 19.6MB
==> Installing mysql dependency: zlib
==> Pouring zlib--1.2.13.arm64_ventura.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/zlib/1.2.13: 13 files, 399KB
==> Installing mysql dependency: xz
==> Pouring xz--5.4.3.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/xz/5.4.3: 162 files, 2.6MB
==> Installing mysql dependency: zstd
==> Pouring zstd--1.5.5.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/zstd/1.5.5: 31 files, 2.3MB
==> Installing mysql
==> Pouring mysql--8.0.33_3.arm64_ventura.bottle.tar.gz
==> /opt/homebrew/Cellar/mysql/8.0.33_3/bin/mysqld --initialize-insecure --user=taoyi --basedir=/opt/homebrew/Cellar/mysql/8.0.33_3 --datadir=/opt/hom
==> Caveats
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -u root

To start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mysql/bin/mysqld_safe --datadir=/opt/homebrew/var/mysql
==> Summary
🍺  /opt/homebrew/Cellar/mysql/8.0.33_3: 318 files, 300.4MB
==> Running `brew cleanup mysql`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Upgrading 4 dependents of upgraded formulae:
Disable this behaviour by setting HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
openssl@1.1 1.1.1t -> 1.1.1u, nghttp2 1.52.0 -> 1.54.0_1, node 20.0.0 -> 20.4.0, pyenv 2.3.13 -> 2.3.22
==> Fetching openssl@1.1
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/manifests/1.1.1u
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/blobs/sha256:0a4b0a3deefd8c470db72605e7a05cfaafe9fcdf4ee834de2b3ec031080b4dde
############################################################################################################################################### 100.0%
==> Fetching dependencies for nghttp2: c-ares and libnghttp2
==> Fetching c-ares
==> Downloading https://ghcr.io/v2/homebrew/core/c-ares/manifests/1.19.1
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/c-ares/blobs/sha256:ba35cc0962beaea7ae345ee1818297c40d5653649e563dc9493b93924b87ae41
############################################################################################################################################### 100.0%
==> Fetching libnghttp2
==> Downloading https://ghcr.io/v2/homebrew/core/libnghttp2/manifests/1.54.0
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libnghttp2/blobs/sha256:6cf8b32982c49da3773729b84d205660591fdad185e2b1a5f267ebd498b60622
############################################################################################################################################### 100.0%
==> Fetching nghttp2
==> Downloading https://ghcr.io/v2/homebrew/core/nghttp2/manifests/1.54.0_1
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/nghttp2/blobs/sha256:890634f1d69a36e62202197a07eddf858e9f391403a6ba993a245f73b321f714
############################################################################################################################################### 100.0%
==> Fetching dependencies for node: libuv
==> Fetching libuv
==> Downloading https://ghcr.io/v2/homebrew/core/libuv/manifests/1.46.0
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libuv/blobs/sha256:8c3beb4d11ed0d45cf0b7e07d280ff815eab9f9c138eec90a2f824168aed039e
############################################################################################################################################### 100.0%
==> Fetching node
==> Downloading https://ghcr.io/v2/homebrew/core/node/manifests/20.4.0
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/node/blobs/sha256:7d20cdeeaab118ba6df4505d9bc7fb65735c71f2696c0d001b44a8917f23f3d2
############################################################################################################################################### 100.0%
==> Fetching pyenv
==> Downloading https://ghcr.io/v2/homebrew/core/pyenv/manifests/2.3.22
############################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/pyenv/blobs/sha256:77b3b2bb54c95d1feb48bd5b4b83b00fd6fa91907239331dd2f058f98b294e62
############################################################################################################################################### 100.0%
==> Upgrading openssl@1.1
  1.1.1t -> 1.1.1u

==> Pouring openssl@1.1--1.1.1u.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openssl@1.1/1.1.1u: 8,101 files, 18MB
==> Running `brew cleanup openssl@1.1`...
Removing: /opt/homebrew/Cellar/openssl@1.1/1.1.1t... (8,101 files, 18MB)
Removing: /Users/taoyi/Library/Caches/Homebrew/openssl@1.1--1.1.1t... (5.3MB)
==> Upgrading nghttp2
  1.52.0 -> 1.54.0_1

==> Installing dependencies for nghttp2: c-ares and libnghttp2
==> Installing nghttp2 dependency: c-ares
==> Pouring c-ares--1.19.1.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/c-ares/1.19.1: 87 files, 681.2KB
==> Installing nghttp2 dependency: libnghttp2
==> Pouring libnghttp2--1.54.0.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libnghttp2/1.54.0: 13 files, 731.4KB
==> Installing nghttp2
==> Pouring nghttp2--1.54.0_1.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/nghttp2/1.54.0_1: 17 files, 2.3MB
==> Running `brew cleanup nghttp2`...
Removing: /opt/homebrew/Cellar/nghttp2/1.52.0... (17 files, 2.2MB)
Removing: /Users/taoyi/Library/Caches/Homebrew/nghttp2--1.52.0... (777KB)
==> Upgrading node
  20.0.0 -> 20.4.0

==> Installing dependencies for node: libuv
==> Installing node dependency: libuv
==> Pouring libuv--1.46.0.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libuv/1.46.0: 47 files, 3MB
==> Installing node
==> Pouring node--20.4.0.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/node/20.4.0: 2,359 files, 57.2MB
==> Running `brew cleanup node`...
Removing: /opt/homebrew/Cellar/node/20.0.0... (2,260 files, 57.2MB)
Removing: /Users/taoyi/Library/Caches/Homebrew/node--20.0.0... (14.5MB)
==> Upgrading pyenv
  2.3.13 -> 2.3.22

==> Pouring pyenv--2.3.22.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pyenv/2.3.22: 1,086 files, 3.3MB
==> Running `brew cleanup pyenv`...
Removing: /opt/homebrew/Cellar/pyenv/2.3.13... (1,048 files, 3.2MB)
==> Checking for dependents of upgraded formulae...
==> No broken dependents found!
==> `brew cleanup` has not been run in the last 30 days, running now...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
Removing: /opt/homebrew/Cellar/c-ares/1.19.0... (87 files, 675.9KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/c-ares--1.19.0... (160.3KB)
Removing: /opt/homebrew/Cellar/ca-certificates/2023-01-10... (3 files, 216.9KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/ca-certificates--2023-01-10... (122.6KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/gettext--0.21.1... (8.8MB)
Removing: /opt/homebrew/Cellar/icu4c/72.1... (263 files, 78.4MB)
Removing: /Users/taoyi/Library/Caches/Homebrew/icu4c--72.1... (28.9MB)
Removing: /opt/homebrew/Cellar/libnghttp2/1.52.0... (13 files, 731.5KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/libnghttp2--1.52.0... (211.3KB)
Removing: /opt/homebrew/Cellar/libuv/1.44.2... (50 files, 3.5MB)
Removing: /opt/homebrew/Cellar/openssl@3/3.0.8... (6,480 files, 28.1MB)
Removing: /Users/taoyi/Library/Caches/Homebrew/pcre2--10.42... (2.0MB)
Removing: /Users/taoyi/Library/Caches/Homebrew/readline--8.2.1... (573.8KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/ca-certificates_bottle_manifest--2023-01-10... (1.8KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/nghttp2_bottle_manifest--1.52.0... (10.7KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/gettext_bottle_manifest--0.21.1... (10.8KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/readline_bottle_manifest--8.2.1... (8.6KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/node_bottle_manifest--19.7.0... (14.9KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/newrelic-infra-agent_bottle_manifest--1.37.2... (7.6KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/c-ares_bottle_manifest--1.19.0... (7.2KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/git_bottle_manifest--2.39.2-1... (12.7KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/pcre2_bottle_manifest--10.42... (8.5KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/icu4c_bottle_manifest--72.1... (8.1KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/pyenv_bottle_manifest--2.3.13... (23.8KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/libnghttp2_bottle_manifest--1.52.0... (7.2KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/openssl@1.1_bottle_manifest--1.1.1t... (8.7KB)
Removing: /Users/taoyi/Library/Caches/Homebrew/openssl@3_bottle_manifest--3.0.8... (8.7KB)
Removing: /Users/taoyi/Library/Logs/Homebrew/terminal-notifier... (64B)
Removing: /Users/taoyi/Library/Logs/Homebrew/vue-cli... (64B)
Pruned 0 symbolic links and 4 directories from /opt/homebrew
==> Caveats
==> mysql
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -u root

To start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mysql/bin/mysqld_safe --datadir=/opt/homebrew/var/mysql

# taoyi @ tysYZMac in ~ [11:05:53]
$ brew services start mysql
==> Successfully started `mysql` (label: homebrew.mxcl.mysql)

# taoyi @ tysYZMac in ~ [11:06:02]
$ mysql_secure_installation

Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: Y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
Please set the password for root here.

New password:

Re-enter new password:

Estimated strength of the password: 50
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : Y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : Y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : q

 ... skipping.
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : Y
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : Y
Success.

All done!

```
