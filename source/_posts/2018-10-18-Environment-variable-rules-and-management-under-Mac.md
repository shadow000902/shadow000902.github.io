---
title: Mac 下环境变量规则及管理
date: 2018-10-18 14:15:03
categories: [Tips]
tags: [mac]
---

#### Mac系统的环境变量，加载顺序
- a. /etc/profile
- b. /etc/paths
- c. ~/.bash_profile
- d. ~/.bash_login
- e. ~/.profile
- f. ~/.bashrc
- g. ~/.zshrc

  <!--more-->

其中`a`和`b`是系统级别的，系统启动就会加载，其余是用户级别的。`c`,`d`,`e`按照从前往后的顺序读取，如果`c`文件存在，则后面的几个文件就会被忽略不读了，以此类推。
`~/.bashrc`没有上述规则，它是`bash shell`打开的时候载入的。
`~/.zshrc`没有上述规则，它是`zsh shell`打开的时候载入的。
这里建议在`c`中添加环境变量，以下也是以在`c`中添加环境变量来演示的。

#### 添加环境变量
比如添加 `maven` 环境变量
编辑 `~/.bash_profile`文件
```bash
vim ~/.bash_profile
```
添加环境变量
```bash
export M2_HOME=/opt/apache-jmeter-5.0
export PATH=$PATH:$M2_HOME/bin
```
生效环境变量
```bash
source ~/.bash_profile
```

#### 使用zsh shell
在`~/.zshrc`中加入如下内容
```bash
...
source ~/.bash_profile
...
```
这样的话，在每次打开 `zsh shell` 的时候，都会对 `~/.bash_profile` 中的环境变量进行初始化生效

#### `Mac`下`JAVA_HOME`设置，适用于通过`pkg`包直接安装的`java`
1. 检查Java是否已经安装成功
    ```bash
    # taoyi @ taoyiDSC000331 in ~ [15:30:28] 
    $ java -version
    java version "1.8.0_251"
    Java(TM) SE Runtime Environment (build 1.8.0_251-b08)
    Java HotSpot(TM) 64-Bit Server VM (build 25.251-b08, mixed mode)
    ```
    以上输出即说明Java已经安装成功了

2. 查看java指令文件的位置
    ```bash
    # taoyi @ taoyiDSC000331 in ~ [15:35:22] 
    $ which java     
    /usr/bin/java
    # taoyi @ taoyiDSC000331 in ~ [15:36:13] 
    $ ll /usr/bin/java             
    lrwxr-xr-x  1 root  wheel    74B  7  7 01:46 /usr/bin/java -> /System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands/java
    ```
    从以上输出可以知道，`/usr/bin/java`是一个链接文件，实际指向`/System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands/java`这个文件。

3. 获取java实际安装位置
    ```bash
    # taoyi @ taoyiDSC000331 in ~ [15:36:21] 
    $ cd /System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands                                  
    # taoyi @ taoyiDSC000331 in /System/Library/Frameworks/JavaVM.framework/Versions/Current/Commands [15:44:24] 
    $ ./java_home
    /Library/Java/JavaVirtualMachines/jdk1.8.0_251.jdk/Contents/Home
    ```
    从以上可以看到，java的实际安装位置为`/Library/Java/JavaVirtualMachines/jdk1.8.0_251.jdk`，实际的HOME位置为`/Library/Java/JavaVirtualMachines/jdk1.8.0_251.jdk/Contents/Home`

4. 设置`JAVA_HOME`环境变量
    ```bash
    export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_251.jdk/Contents/Home"
    export PATH="$JAVA_HOME/bin:$PATH"
    ```
    根据使用的终端命令的不一样，把以上内容添加到对应的环境变量文件中，如果使用的是原生的`bash`终端，就把内容添加到`~/.bash_profile`中，如果使用的是`zsh`终端，就把内容添加到`~/.zshrc`中
    最后执行`source ~/.zshrc`命令，使刚才的设置生效。