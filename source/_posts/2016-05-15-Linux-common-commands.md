---
title: Linux常用命令
date: 2016-05-15 16:31:42
categories: [Linux]
tags: [linux]
---

### 基础命令
#### mv
1. Moving files
    ```bash
    mv test0001.txt /opt/
    ```
2. Moving multiple files
    ```bash
    mv test0001.txt test0002.txt /opt/
    mv *.txt /opt/
    ```
3. Moving directory
    ```bash
    mv /tmp/test0001 /opt/
    ```

  <!--more-->

4. Renaming files or directory
    ```bash
    mv test0001.txt test0002.txt
    ```
5. Renaming directory
    ```bash
    mv test0001 test0002
    ```
6. Print what happen
    ```bash
    mv -v *.txt /opt/
    ```
7. Using interactive mode
    ```bash
    mv -i *.txt /opt/
    ```
8. Using update option
    ```bash
    mv -uv *.txt /opt/
    ```
9. Do not overwrite any existing file
    ```bash
    mv -vn *.txt /opt/
    ```
10. Create backup when copying
    ```bash
    mv -bv *.txt /opt/
    ```
    [10 Practical mv Command Examples](https://linoxide.com/linux-command/mv-command-linux/)

#### cp(copy)
```bash
cp -r /opt/android/tools /opt/      # -r 复制文件夹
```

#### ps(process status)
参数说明：
```
ps 的参数非常多, 在此仅列出几个常用的参数并大略介绍含义
-A 列出所有的行程
-w 显示加宽可以显示较多的资讯
-au 显示较详细的资讯
-aux 显示所有包含其他使用者的行程
au(x) 输出格式 :
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
USER: 行程拥有者
PID: pid
%CPU: 占用的 CPU 使用率
%MEM: 占用的记忆体使用率
VSZ: 占用的虚拟记忆体大小
RSS: 占用的记忆体大小
TTY: 终端的次要装置号码 (minor device number of tty)
STAT: 该行程的状态:
D: 无法中断的休眠状态 (通常 IO 的进程)
R: 正在执行中
S: 静止状态
T: 暂停执行
Z: 不存在但暂时无法消除
W: 没有足够的记忆体分页可分配
<: 高优先序的行程
N: 低优先序的行程
L: 有记忆体分页分配并锁在记忆体内 (实时系统或捱A I/O)
START: 行程开始时间
TIME: 执行的时间
COMMAND:所执行的指令
```
1. 简单应用
	```bash
	ps -ef | grep tomcat
	```
2. 复杂查询展示
	```bash
	:<<BLOCK
	循环20次
	-o 参数用来格式化输出``指定字段``，字段头为%mem, 只展示指定进程的该字段
	tail -1 取每次循环结果的最后一行，且间隔1秒
	awk用于处理结果展示，展示第一列值和每次的平均值
	BLOCK
	for i in $(seq 20); \
	do ps -o %mem -p 20752 \
	| tail -1;sleep 1;done \
	| awk '{t+=$1;print $1,t/NR}'
	```
3. ``-o``参数使用
	```bash
	# shadow @ shadow in ~ [9:14:44] C:130
    $ ps -o pid,ppid,pgrp,session,tpgid,comm 
      PID  PPID  PGRP  SESS TPGID COMMAND
     4415  4414  4415  4223  4618 zsh
     4618  4415  4618  4223  4618 ps
	```

#### kill

#### shutdown

#### swatch(simple watcher)

#### unzip

#### tar(tape archive)

#### diff

#### git

#### cat
```bash
一次显示整个文件:cat filename
从键盘创建一个文件:cat > filename 只能创建新文件,不能编辑已有文件.
将几个文件合并为一个文件:cat file1 file2 > file
```
1. *合并文件*
    ```bash
    cat *.csv > all-in-one.csv														# 合并多个CSV文件，不考虑顺序
    cat file1.csv file2.csv file3.csv ... file[n].csv > all-in-one.csv				# 合并多个CSV文件，考虑顺序
    ```

#### chmod(change mode)    # 更改文件／文件夹权限

#### chown(change owner)   # 更改文件／文件夹所有者

#### cd(change directory)  # 进入某目录

#### df(disk free)

#### dirs

#### 列举当前目录文件``ls``、``ll``(list)
```bash
ll -t                     # 当前目录文件按倒叙排列，最新的排最前面
ll -t | tac               # 当前目录文件按顺序排列，最早的排最前面
```

#### mkdir(make directories)

#### rm
```bash
rm -f 					# 直接删除文件，无需确认
rm -r 					# 删除文件夹，需要确认
rm -rf 					# 直接删除目录及其中的全部文件，无需确认
```

#### fdisk

#### telnet

#### ifconfig

#### tail
```bash
tail -f catalina.out | grep request      # 查看Linux服务器实时日志，catalina.out为服务器实时记录日志的文件
```

#### touch           # 创建文件（夹）命令

1. 使用文件名作为参数，可以同时创建多个文件。当目标文件已经存在时，将更新该文件的时间标记，否则将创建指定名称的空文件。
    ```bash
    touch file1 file2
    ```
2. 创建新的目录
    ```bash
    [root@localhost home]# mkdir dir1
    [root@localhost home]# mkdir dir2/dir
    mkdir: 无法创建目录"dir2/dir": 没有那个文件或目录
    [root@localhost home]# mkdir -p dir2/dir                    # -p 确保目录名称存在，不存在的就建一个
    [root@localhost home]#
    ```
3. 同时创建多级目录
    ```bash
    [root@localhost home]# ls
    justin lost+found t
    [root@localhost home]# mkdir -p {dir1,dir2/{dir3,dir4}}
    [root@localhost home]# ls
    dir1 dir2 justin lost+found t
    [root@localhost home]# ls dir2
    dir3 dir4
    [root@localhost home]#
    ```

#### rmdir            # 删除文件（夹）命令
```bash
[root@localhost home]# mkdir -p {dir1,dir2/dir3}            # -p 当子目录被删除后也成为空目录的话，则顺便一并删除
[root@localhost home]# ls
dir1 dir2 justin lost+found t
[root@localhost home]# rmdir dir1
[root@localhost home]# rmdir dir2
rmdir: 删除 "dir2"失败: 目录非空
[root@localhost home]# rmdir -p dir2/dir3/
[root@localhost home]# ls
justin lost+found t
[root@localhost home]#
```

#### 更改文件（夹）权限
1. 更改所有者权限
    ```bash
    sudo chmod 600 ××× #（只有所有者有读和写的权限）
    sudo chmod 644 ××× #（所有者有读和写的权限，组用户只有读的权限）
    sudo chmod 700 ××× #（只有所有者有读和写以及执行的权限）
    sudo chmod 666 ××× #（每个人都有读和写的权限）
    sudo chmod 777 ××× #（每个人都有读和写以及执行的权限）
    ```
    ```markdown
    sudo chmod -（代表类型）[×××（所有者）×××（组用户）×××（其他用户）]           # xxx为一个二进制组合
    ```
    其中×××指文件名（也可以是文件夹名，不过要在chmod后加-ld）。
    三位数的每一位都表示一个用户类型的权限设置。取值是0～7，即二进制的[000]~[111]。
    这个三位的二进制数的每一位分别表示读、写、执行权限。
    如000表示三项权限均无，而100表示只读。这样，我们就有了下面的对应：
    ```bash
    0 [000] 无任何权限
    4 [100] 只读权限
    6 [110] 读写权限
    7 [111] 读写执行权限
    ```
2. 更改文件（夹）权限
    ```bash
    chmod [-cfvR] [--help] [--version] mode file...
    mode : 权限设定字串, 格式如下 : [ugoa...][[+-=][rwxX]...][,...]
    ```
    ```markdown
    u 表示该档案的拥有者，
    g 表示与该档案的拥有者属于同一个群体(group)者，
    o 表示其他以外的人，
    a 表示这三者皆是。 
    + 表示增加权限、- 表示取消权限、= 表示唯一设定权限。 
    r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该档案是个子目录或者该档案已经被设定过为可执行。 
    -c : 若该档案权限确实已经更改，才显示其更改动作 
    -f : 若该档案权限无法被更改也不要显示错误讯息 
    -v : 显示权限变更的详细资料 
    -R : 对目前目录下的所有档案与子目录进行相同的权限变更(即以递回的方式逐个变更) 
    --help : 显示辅助说明 
    --version : 显示版本 
    ```
3. 文件（夹）的权限
    ```markdown
    -rw------- (600) -- 只有属主有读写权限。 
    -rw-r--r-- (644) -- 只有属主有读写权限；而属组用户和其他用户只有读权限。 
    -rwx------ (700) -- 只有属主有读、写、执行权限。 
    -rwxr-xr-x (755) -- 属主有读、写、执行权限；而属组用户和其他用户只有读、执行权限。 
    -rwx--x--x (711) -- 属主有读、写、执行权限；而属组用户和其他用户只有执行权限。 
    -rw-rw-rw- (666) -- 所有用户都有文件读、写权限。这种做法不可取。 
    -rwxrwxrwx (777) -- 所有用户都有读、写、执行权限。更不可取的做法。 
    ```
    以下是对目录的两个普通设定: 
    ```markdown
    drwx------ (700) - 只有属主可在目录中读、写。 
    drwxr-xr-x (755) - 所有用户可读该目录，但只有属主才能改变目录中的内容。
    ```

#### 查看目录剩余空间大小，*du(disk usage)*
1. df -hl             # 查看磁盘剩余空间
    ```bash
    文件系统       容量    已用   可用                      已用%          挂载点
    Filesystem   Size   Used  Avail Capacity iused      ifree %iused  Mounted on
    /dev/disk1  112Gi   91Gi   21Gi    82% 1900939 4293066340    0%   /
    ```
2. 
    ```bash
    df -h              # 命令查看整个硬盘的大小 ，-h表示人可读的
    du -sh [目录名]     # 返回该目录的大小
    du -sm [文件夹]     # 返回该文件夹总M数
    df --help          # 查看更多功能
    du --help          # 查看更多功能
    ```
    32.3
    ```bash
    du -sh xmldb/
    du -sm * | sort -n      # 统计当前目录大小并按大小排序
    du -sk * | grep taoyi   # 查看一个人的大小
    du -m | cut "/" -f 2    # 查看第二个/字符前的文字
    wc [-lmw]               # -l: 多少行；-m: 多少字符；-w: 多少字
    ```
4. 查看当前目录下各文件夹的大小
    ```bash
    du -h --max-depth=1
    du -d 1 -h              # 命令查看当前目录下所有文件夹的大小 -d 指深度，后面加一个数值
    ```
    ``--max-depth=n``表示深入到第``n``层目录，此处设置为``1``，即表示深入``1``层，即查看当前目录下各个文件夹的大小；如果设置为``0``，表示不深入到子目录，那得出的就是当前目录的总大小。
    
5. du命令参数
    ```bash
    du [-abcDhHklmsSx] [-L <符号连接>][-X <文件>][--block-size][--exclude=<目录或文件>] [--max-depth=<目录层数>][--help][--version][目录或文件]
    ```
    - ``-a或-all``：为每个指定文件显示磁盘使用情况，或者为目录中每个文件显示各自磁盘使用情况。
    - ``-b或-bytes``：显示目录或文件大小时，以byte为单位。
    - ``-c或–total``：除了显示目录或文件的大小外，同时也显示所有目录或文件的总和。
    - ``-D或–dereference-args``：显示指定符号连接的源文件大小。
    - ``-h或–human-readable``：以K，M，G为单位，提高信息的可读性。
    - ``-H或–si``：与-h参数相同，但是K，M，G是以1000为换算单位,而不是以1024为换算单位。
    - ``-k或–kilobytes``：以1024 bytes为单位。
    - ``-l或–count-links``：重复计算硬件连接的文件。
    - ``-L<符号连接>或–dereference<符号连接>``：显示选项中所指定符号连接的源文件大小。
    - ``-m或–megabytes``：以1MB为单位。
    - ``-s或–summarize``：仅显示总计，即当前目录的大小。
    - ``-S或–separate-dirs``：显示每个目录的大小时，并不含其子目录的大小。
    - ``-x或–one-file-xystem``：以一开始处理时的文件系统为准，若遇上其它不同的文件系统目录则略过。
    - ``-X<文件>或–exclude-from=<文件>``：在<文件>指定目录或文件。
    - ``–exclude=<目录或文件>``：略过指定的目录或文件。
    - ``–max-depth=<目录层数>``：超过指定层数的目录后，予以忽略。
    - ``–help``：显示帮助。
    - ``–version``：显示版本信息。
    - ``-0``：（杠零）表示每列出一个目录的信息，不换行，而是直接输出下一个目录的信息。

#### 修改root密码
```bash
[root@shadow000902 /]# passwd								# 修改密码命令
Changing password for user root.
New password: 												# 输入新的密码
Retype new password: 										# 确认新的密码
passwd: all authentication tokens updated successfully.		# 成功修改密码提示
```

#### 永久修改`ubuntu`主机名
```bash
vim /etc/hostname
```

#### 永久修改`redhat/centos`主机名
```bash
vi /etc/sysconfig/network
```
修改`HOSTNAME`字段值即修改了主机名

#### 创建用户及用户组，并修改密码切换用户
```bash
# root @ shadow in ~ [10:30:20] C:1
$ adduser shadow                            # 创建用户
# root @ shadow in ~ [10:34:45]
$ groupadd shadow                           # 创建用户组
groupadd：“shadow”组已存在                    # 在创建用户的时候，已经同时创建了同名的用户组
# root @ shadow in ~ [10:36:52]
$ passwd shadow                             # 修改用户密码
更改用户 shadow 的密码 。
新的 密码：
重新输入新的 密码：
passwd：所有的身份验证令牌已经成功更新。
# root @ shadow in ~ [10:38:41]
$ su - shadow                               # 切换用户
[shadow@shadow ~]$                          # 切换用户成功
```

#### 删除用户及用户文件夹
```bash
# 查看所有用户
cat /etc/passwd|grep -v nologin|grep -v halt|grep -v shutdown|awk -F":" '{ print $1"|"$3"|"$4 }'|more
su - root                                   # 首先需要切换到root用户
userdel -r shadow                           # 删除shadow用户及用户文件夹
```

#### CentOS卸载软件
```bash
yum remove tomcat
```

#### “shadow is not in the sudoers file.  This incident will be reported.”解决方法
在``root``用户下，执行``visudo``
```bash
  91 ## Allow root to run any commands anywhere
  92 root    ALL=(ALL)       ALL
  93 shadow  ALL=(ALL)       ALL        # 添加这段内容，第一个单词是，需要可以使用sudo权限的用户名
  94
  95 ## Allows members of the 'sys' group to run networking, software,
```

#### Ubuntu 命令行安装语言包
中文语言包:
- language-pack-zh-hans 简体中文
- language-pack-zh-hans-base
- language-pack-zh-hant 繁体中文
- language-pack-zh-hant-base
安装命令：

```bash
sudo apt-get install  language-pack-zh-han*
```
最后运行语言支持检查
```bash
sudo apt install $(check-language-support)
```
会更新最新的语言支持包。

#### 查找文件夹
```bash
find / -name mysql
```

#### tree Mac下树形查看当前目录文件
1. 使用`find`命令模拟出`tree`命令的效果
    ```bash
    find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
    ```
    当然也可以写一个别名来快速执行该命令，运行如下命令，将上面这个命令写到`~/.bash_profile`里，以后直接运行`tree`命令就更方便了:
    ```bash
    alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
    ```
2. 使用 `homebrew` 安装 `tree` 命令行
    ```bash
    brew install tree
    ```
    这样就在你的`mac`上安装了 `tree` 命令行了。
3. `tree`命令行参数（只实用与安装了`tree`命令行工具）
    ```
    -a 显示所有文件和目录。
    -A 使用ASNI绘图字符显示树状图而非以ASCII字符组合。
    -C 在文件和目录清单加上色彩，便于区分各种类型。
    -d 显示目录名称而非内容。
    -D 列出文件或目录的更改时间。
    -f 在每个文件或目录之前，显示完整的相对路径名称。
    -F 在执行文件，目录，Socket，符号连接，管道名称名称，各自加上"*","/","=","@","|"号。
    -g 列出文件或目录的所属群组名称，没有对应的名称时，则显示群组识别码。
    -i 不以阶梯状列出文件或目录名称。
    -I 不显示符合范本样式的文件或目录名称。
    -l 如遇到性质为符号连接的目录，直接列出该连接所指向的原始目录。
    -n 不在文件和目录清单加上色彩。
    -N 直接列出文件和目录名称，包括控制字符。
    -p 列出权限标示。
    -P 只显示符合范本样式的文件或目录名称。
    -q 用"?"号取代控制字符，列出文件和目录名称。
    -s 列出文件或目录大小。
    -t 用文件和目录的更改时间排序。
    -u 列出文件或目录的拥有者名称，没有对应的名称时，则显示用户识别码。
    -x 将范围局限在现行的文件系统中，若指定目录下的某些子目录，其存放于另一个文件系统上，则将该子目录予以排除在寻找范围外。
    ```
4. `tree`结果乱码解决
    ```bash
    tree -N
    ```
    - -N  Print non-printable characters as is instead of as escaped octal numbers.

#### ls -R
列出当前目录下所有目录及文件的相对路径
{% asset_img 当前目录下的所有文件及文件夹.png 当前目录下的所有文件及文件夹 %}

#### `last`显示最近的登录用户信息
```bash
# souche @ kickseed in ~ [11:34:38]
$ last -n 5
souche   pts/1        172.17.53.161    Tue Dec 11 11:34   still logged in
souche   pts/1        172.17.49.117    Tue Dec 11 11:16 - 11:17  (00:00)
souche   pts/1        172.17.53.161    Tue Dec 11 10:47 - 10:48  (00:00)
souche   pts/1        172.17.52.197    Mon Dec 10 18:57 - 18:58  (00:01)
souche   pts/4        172.17.53.34     Mon Dec 10 17:05 - 17:34  (00:28)

wtmp begins Mon Dec  3 10:06:15 2018

```

### 进阶命令
#### top
参数：
```
-b：以批处理模式操作,搭配`n`参数一起使用，可以用来将`top`的结果输出到档案内
-c：切换显示模式，共有两种模式，一是只显示执行档的名称，另一种是显示完整的路径与名称S : 累积模式，会将己完成或消失的子行程 ( dead child process ) 的 CPU time 累积起来
-d：屏幕刷新间隔时间；
-I：忽略失效过程；
-s：保密模式；
-S：累积模式；
-i：不显示任何闲置 (idle) 或无用 (zombie) 的行程；
-u<用户名>：指定用户名；
-p<进程号>：指定进程；
-n<次数>：循环显示的次数，完成后将会退出 top
```
1. 监控每个进程的情况
```bash
top -b -d 1 -n 20 -p 3951 | grep --line-buffered ^3951 | awk '{cpu+=$9;mem+=$10}{print $9,$10,cpu/NR,mem/NR}'
```

#### 文本去重
```bash
# !/bin/sh
file='test.txt'
sort -n $file | uniq
sort -n $file | awk '{if($0!=line)print; line=$0}'
sort -n $file | sed '$!N; /^\(.*\)\n\1$/!P; D'
```

#### scp     # 本地文件与服务器文件交互
```bash
# 从服务器下载文件
scp username@servername:/remote_path/filename ~/local_destination
# 上传本地文件到服务器
scp ~/local_path/local_filename username@servername:/remote_path
# 从服务器下载整个目录
scp -r username@servername:/remote_path/remote_dir/ ~/local_destination
# 上传目录到服务器
scp  -r ~/local_dir username@servername:/remote_path/remote_dir
```

#### netstat
参数：
    -a或--all: 显示所有连线中的Socket。
    -A<网络类型>或--<网络类型>: 列出该网络类型连线中的相关地址。
    -c或--continuous: 持续列出网络状态。
    -C或--cache: 显示路由器配置的快取信息。
    -e或--extend: 显示网络其他相关信息。
    -F或--fib: 显示FIB。
    -g或--groups: 显示多重广播功能群组组员名单。
    -h或--help: 在线帮助。
    -i或--interfaces: 显示网络界面信息表单。
    -l或--listening: 显示监控中的服务器的Socket。
    -M或--masquerade: 显示伪装的网络连线。
    -n或--numeric: 直接使用IP地址，而不通过域名服务器。
    -N或--netlink或--symbolic: 显示网络硬件外围设备的符号连接名称。
    -o或--timers: 显示计时器。
    -p或--programs: 显示正在使用Socket的程序识别码和程序名称。
    -r或--route 显示Routing: Table。
    -s或--statistice: 显示网络工作信息统计表。
    -t或--tcp: 显示TCP传输协议的连线状况。
    -u或--udp: 显示UDP传输协议的连线状况。
    -v或--verbose: 显示指令执行过程。
    -V或--version: 显示版本信息。
    -w或--raw: 显示RAW传输协议的连线状况。
    -x或--unix 此参数的效果和指定"-A: unix"参数相同。
    --ip或--inet 此参数的效果和指定"-A: inet"参数相同。

1. 获取端口占用情况【Linux系统】
	```bash
	# shadow @ shadow in ~ [0:33:06] 
	$ netstat -anp | grep 80
	(No info could be read for "-p": geteuid()=1000 but you should be root.)
	tcp        0      0 172.16.194.20:41622     100.100.45.73:80        TIME_WAIT   -                   
	tcp        0      0 172.16.194.20:39718     100.100.30.25:80        ESTABLISHED -                   
	tcp6       0      0 :::8080                 :::*                    LISTEN      -                   
	unix  2      [ ACC ]     STREAM     LISTENING     2056613  -                    @/containerd-shim/moby/ebda2e07d80217a8cd7876f119624690f5cf6fda30a1f2a6d53607b63502680e/shim.sock
	unix  3      [ ]         STREAM     CONNECTED     2057472  -                    @/containerd-shim/moby/ebda2e07d80217a8cd7876f119624690f5cf6fda30a1f2a6d53607b63502680e/shim.sock
	unix  3      [ ]         STREAM     CONNECTED     11580    -                    /run/systemd/journal/stdout
	unix  3      [ ]         STREAM     CONNECTED     11801    -                    
	```
2. 获取不重复的网络连接数量
	```bash
	:<<BLOCK
	获取所有的网络连接
	取第五列
	对第五列数据用``:``分隔，并取第一列
	数据升序排列
	对重复数据进行去重，``-c``统计出现次数
	识别每行开头的数字，对结果降序排列
	计算一共有多少个不重复的数据
	BLOCK
	netstat -tnp \
	| awk '{print $5}' \
	| awk -F: '{print $1}' \
	| sort \
	| uniq -c \
	| sort -nr \
	| wc -l
	```
 3. 显示tcp，udp的端口和进程等相关情况
 ```bash
 [root@shadow ~]# netstat -tunlp
 Active Internet connections (only servers)
 Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
 tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      24569/sshd          
 udp        0      0 0.0.0.0:4038            0.0.0.0:*                           724/dhclient        
 udp        0      0 0.0.0.0:68              0.0.0.0:*                           724/dhclient        
 udp        0      0 172.17.0.1:123          0.0.0.0:*                           32364/ntpd          
 udp        0      0 172.16.194.20:123       0.0.0.0:*                           32364/ntpd          
 udp        0      0 127.0.0.1:123           0.0.0.0:*                           32364/ntpd          
 udp        0      0 0.0.0.0:123             0.0.0.0:*                           32364/ntpd          
 udp6       0      0 :::61028                :::*                                724/dhclient        
 udp6       0      0 :::123                  :::*                                32364/ntpd  
```

#### lsof    # Mac下查看端口占用情况
```bash
# taoyi @ TyMac in ~ [1:54:51] C:130
$ lsof -i tcp:5555
COMMAND   PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
adb     94280 taoyi   14u  IPv4 0x38c46a3265bac391      0t0  TCP 192.168.31.71:49360->192.168.31.233:personal-agent (ESTABLISHED)
```


### Linux 三剑客
#### grep
1. 在文件中查找单词
    ```bash
    grep shadow /etc/hosts
    ```
2. 在多个文件中查找单词
    ```bash
    grep shadow /etc/hosts /etc/hosts1
    ```
3. 列出包含指定单词的文件的文件名
    ```bash
    grep -l shadow /etc/hosts /etc/hosts1 /etc/hosts2 /etc/hosts3
    ```
4. 在文件中查找指定单词并显示匹配行的行号
    ```bash
    grep -n shadow /etc/hosts /etc/hosts1
    ```
5. 输出不包含指定单词的行
    ```bash
    grep -v shadow /etc/hosts
    ```
6. 输出所有以指定单词开头的行
    ```bash
    grep ^ shadow /etc/hosts
    ```
7. 输出所有以指定单词结尾的行
    ```bash
    grep shadow$ /etc/hosts
    ```
8. 参数递归地查找指定单词
    ```bash
    grep -r shadow /etc/hosts
    ```
9. 查找文件中所有的空行
    ```bash
    grep ^$ /etc/hosts
    ```
10. 同时查找多个单词
    ```bash
    grep -e shadow -e shadows /etc/hosts
    ```
11. 计算匹配到的单词的数量
    ```bash
    grep -c -f shadow /etc/hosts
    ```
12. 
    ```bash
    grep -irn "SyncWriteStream" ./node_modules/hexo-deployer-git/
    ```
13. 打印查找结果匹配行的上下n行
    ```bash
    # 前后5行
    grep -5 'parttern' inputfile
    # 后5行
    grep -A 5 'parttern' inputfile
    # 前5行
    grep -B 5 'parttern' inputfile
    ```
14. 不查找有些文件夹
    ```bash
    # 排除单个目录
    grep -E "http" ./ -R --exclude-dir=.git
    # 排除多个目录
    grep -E "http" . -R --exclude-dir={.git,venv}
    # 排除多个文件
    grep -E "http" . -R --exclude={_config.yml,debug.log}
    # 排除多个类型后缀的文件
    grep -E "http" . -R --exclude=*.{py,js} 
    ```

#### awk
参数：
	NR：表示从awk开始执行后，按照记录分隔符读取的数据次数，默认的记录分隔符为换行符，因此默认的就是读取的数据行数，NR可以理解为Number of Record的缩写。
	NF：表示目前的记录被分割的字段的数目，NF可以理解为Number of Field。
	BEGIN：模式指定的操作在读取任何输入之前执行，且只执行一次。
	END：模式指定的操作在读取所有的输入后执行。

```bash
ll | awk '{print $9}'                                   # 输出ll命令拿到的信息，并只打印出第九列
ll | awk '{$1=$2=$3=$4=$5=$6=$7=$8=""; print $0}'       # 排除多列，并打印出后面的所有列，“0”表示所有
ll | awk '{print $1, $2}'                               # 输出ll命令拿到的信息，并只打印出第一、第二列
awk '{print $1 $2}' filename                            # 打印完文件的第一行，再打印文件的第二行
awk 'END{print NR}' filename                            # 打印文本文件的总行数
awk 'NR==1{print}' filename                             # 打印文本第一行
ps -ef | grep tomcat | awk '{printf $2 "\t" }'          # 获取 ps 出来的结果的第二列；printf 打印结果时，取消换行符；"\t"把结果之间用空格分隔
```
1. 获取 Linux 服务器下所有的 tomcat
    原始数据：
    ```bash
    souche   14034     1  0 Dec07 ?        00:26:10 /opt/souche/java/bin/java -Djava.util.logging.config.file=/home/souche/tomcats/12005_ironman-test/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Dignore.endorsed.dirs= -classpath /home/souche/tomcats/12005_ironman-test/bin/bootstrap.jar:/home/souche/tomcats/12005_ironman-test/bin/tomcat-juli.jar -Dcatalina.base=/home/souche/tomcats/12005_ironman-test -Dcatalina.home=/home/souche/tomcats/12005_ironman-test -Djava.io.tmpdir=/home/souche/tomcats/12005_ironman-test/temp org.apache.catalina.startup.Bootstrap start
    ```
    ```bash
    ps -ef | grep tomcat | awk 'END{print "The end!"}BEGIN{FS="/"}{print $10}'
    # 同
    ps -ef | grep tomcat | awk -F "/" '{print $10}'
    ```
    获取结果：
    ```bash
    12005_ironman-test
    The end!
    ```
    其中`END{print "The end!"}`这一段非必要
2. awk 命令的参数
    ```bash
    ARGC               命令行参数个数
    ARGV               命令行参数排列
    ENVIRON            支持队列中系统环境变量的使用
    FILENAME           awk浏览的文件名
    FNR                浏览文件的记录数
    FS                 设置输入域分隔符，等价于命令行 -F选项
    NF                 浏览记录的域的个数
    NR                 已读的记录数
    OFS                输出域分隔符
    ORS                输出记录分隔符
    RS                 控制记录分隔符
    ```
3. awk 命令格式
    ```bash
    awk '条件1 {动作1} 条件2｛动作2｝…' 文件名                  # 命令方式一
    commend | awk '条件1 {动作1} 条件2｛动作2｝…'              # 命令方式二
    ```
4. awk 结果排序
    ```bash
    # souche @ kickseed in ~/tomcats [12:48:05] C:2
    $ ps -ef | grep tomcat | awk 'END{print "The end!"}BEGIN{FS="/"}{print $10 | "sort -r -n"}'
    The end!
    12021_venom-test
    12020_asgard-test
    12019_redline-test
    12018_whiteDragonHorse-test
    12017_topgear-flow-test
    12014_topgear-test3
    12012_audit-test
    12005_ironman-test
    ```
    其中`-r`表示从大到小，不加该参数表示从小到大，`-n`表示按照数字排序


#### sed     #
[sed命令用法](https://www.cnblogs.com/maxincai/p/5146338.html)

```markdown
[root@www ~]# sed [-nefr] [动作]
选项与参数：
-n ：使用安静(silent)模式。在一般 sed 的用法中，所有来自 STDIN 的数据一般都会被列出到终端上。但如果加上 -n 参数后，则只有经过sed 特殊处理的那一行(或者动作)才会被列出来。
-e ：直接在命令列模式上进行 sed 的动作编辑；
-f ：直接将 sed 的动作写在一个文件内， -f filename 则可以运行 filename 内的 sed 动作；
-r ：sed 的动作支持的是延伸型正规表示法的语法。(默认是基础正规表示法语法)
-i ：直接修改读取的文件内容，而不是输出到终端。

动作说明： [n1[,n2]]function
n1, n2 ：不见得会存在，一般代表『选择进行动作的行数』，举例来说，如果我的动作是需要在 10 到 20 行之间进行的，则『 10,20[动作行为] 』

function：
a ：新增， a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)～
c ：取代， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！
d ：删除，因为是删除啊，所以 d 后面通常不接任何咚咚；
i ：插入， i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)；
p ：列印，亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行～
s ：取代，可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g 就是啦！
```
1. 以行为单位删除
    ```bash
    nl ~/test.txt | sed '2,5d'                         # 删除2～5行
    nl ~/test.txt | sed '2d'                           # 删除第2行
    nl ~/test.txt | sed '3,$d'                         # 删除3到最后一行
    ```
2. 以行为单位新增
    ```bash
    nl ~/test.txt | sed '2a drink tea'                 # 在第二行后即第三行加上“drink tea”
    nl ~/test.txt | sed '2i drink tea'                 # 在第二行前即第二行加上“drink tea”
    nl ~/test.txt | sed '2a drink tea or ......\'      # 在第二行后加上两行，每一行之间都必须要以反斜杠『 \ 』来进行新行的添加
    ```
3. 以行为单位替换
    ```bash
    nl ~/test.txt | sed '2,5c No 2-5 number'           # 将第2-5行的内容取代成为『No 2-5 number
    nl ~/test.txt | sed -n '5,7p'                      # 列出 ~/test.txt 文件内的第 5-7 行
    ```
4. 数据的搜索并显示
    ```bash
    nl ~/test.txt | sed '/root/p'                      # 如果root找到，除了输出所有行，还会输出匹配行
    nl ~/test.txt | sed -n '/root/p'                   # 只打印包含root的行
    ```
5. 数据的搜索并删除
    ```bash
    nl ~/test.txt | sed '/root/d'                      # 删除包含root的行，其他行输出
    ```
6. 数据的搜索并执行命令
    ```bash
    nl ~/test.txt | sed -n '/root/{s/bash/blueshell/;p}'       # 找到root对应的行，执行后面花括号中的一组命令，每个命令之间用分号分隔，这里把bash替换为blueshell，再输出这行
    nl ~/test.txt | sed -n '/root/{s/bash/blueshell/;p;q}'     # 最后的q是退出
    ```
7. **数据的搜索并替换**
    ```bash
    sed 's/要被取代的字串/新的字串/g'
    ```
8. 多点编辑
    ```bash
    nl ~/test.txt | sed -e '3,$d' -e 's/bash/blueshell/'       # -e表示多点编辑，一条sed命令，删除/etc/passwd第三行到末尾的数据，并把bash替换为blueshell
    ```
9. **直接修改文件内容**
    ``sed``可以直接修改文件的内容，不必使用管道命令或数据流重导向
    ```bash
    sed -i 's/\.$/\!/g' test.txt                               # 将 test.txt 内每一行结尾若为 . 则换成 ! sed 的『 -i 』选项可以直接修改文件内容
    # 如果 -i 参数不生效的话，需要使用 -ig 参数
    sed -ig's/要被取代的字串/新的字串/g' test.txt
    sed -i '$a # This is a test' test.txt                      # 在 test.txt 最后一行加入『# This is a test』 $代表的是最后一行，而a的动作是新增
    ```
10. **直接修改文件内容进阶**
    对同一个文件中的多个字段同时做修改，并对原文件做备份。
    原文本与替换文本之间用3个`@`分隔成两段
    如果替换后的值，需要参数化取值，则只需要把`'`换成`"`即可。
    ```bash
    sed -i.backup -E \
      -e "s@maCode = \".*\"@maCode = \"${maCode}\"@" \
      -e "s@orderCode = \".*\"@orderCode = \"${orderCode}\"@" \
      ${WORKSPACE}/mainStream/topgear/customMS001/customMS001_${ENV}.py
    ```
11. **删除和插入文件的倒数指定行**
	删除文件的倒数第二行
	```bash
	sed -i.backup $(($(cat ${dest_file} | wc -l)))'d' ${dest_file}
	```
	在倒数第二行开始插入字符「即倒数第一行和第二行之间插入需要插入的字符」
	```bash
	sed -i $(($(cat ${dest_file} | wc -l)+1))"i\\$line" $dest_file
	```
12. **匹配+替换的组合使用**
	使用 \1 , \2代表第一个和第二个正则分组，用来分别取出 161～163 的第2列和第3列。
	由于使用 () 的分组正则属于扩展正则表达式，所以需要增加 -E 选项来开启扩展正则的支持。
	```bash
	# taoyi @ TyMac in ~ [13:32:06] 
    $ seq 161 163 | sed -E 's#.(.)(.)#\1#'
    # 以下为结果
    6
    6
    6
    
    # taoyi @ TyMac in ~ [13:32:46] 
    $ seq 161 163 | sed -E 's#.(.)(.)#\2#'
    # 以下为结果
    1
    2
    3
	```
13. **在文件开头插入指定内容**
    ```bash
    # 在jobList文件的开头插入字符串`123456`
    sed -i "1i\\123456" jobsList
    ```
    
### 其它常用命令
#### jq
