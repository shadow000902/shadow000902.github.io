---
title: Mac 下环境变量规则及管理
date: 2018-10-18 14:15:03
categories: [Tips]
tags: [mac]
---

##### Mac系统的环境变量，加载顺序
- a. /etc/profile
- b. /etc/paths
- c. ~/.bash_profile
- d. ~/.bash_login
- e. ~/.profile
- f. ~/.bashrc
- g. ~/.zshrc
其中`a`和`b`是系统级别的，系统启动就会加载，其余是用户接别的。`c`,`d`,`e`按照从前往后的顺序读取，如果`c`文件存在，则后面的几个文件就会被忽略不读了，以此类推。
`~/.bashrc`没有上述规则，它是`bash shell`打开的时候载入的。
`~/.zshrc`没有上述规则，它是`zsh shell`打开的时候载入的。
这里建议在`c`中添加环境变量，以下也是以在`c`中添加环境变量来演示的。

##### 添加环境变量
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

##### 使用zsh shell
在`~/.zshrc`中加入如下内容
```bash
...
source ~/.bash_profile
...
```
这样的话，在每次打开 `zsh shell` 的时候，都会对 `~/.bash_profile` 中的环境变量进行初始化生效