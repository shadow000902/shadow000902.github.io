---
title: Python版本管理工具pyenv使用小结
date: 2018-04-10 20:31:28
categories: [Python]
tags: [pyenv]
---

##### 安装``brew``
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

  <!--more-->

##### 安装``pyenv``
```bash
brew install pyenv
```

##### 把``pyenv``加入环境变量
如果使用的终端是``bash``，则编辑``~/.bashrc``，如果使用的终端是``zsh``，则编辑``~/.zshrc``，在该文件的最开头加入语句：
```bash
eval "$(pyenv init -)"
```

##### ``pyenv``常用基本命令
```bash
pyenv install --list                            # List all available versions
pyenv install <version>                         # install python
pyenv global <version>                          # 全局设置python版本为指定版本
pyenv global 2.7.14 3.6.4                       # 指定多个python版本为全局版本，有顺序
pyenv local <version>                           # 设置当前路径下python版本为指定版本
pyenv shell <version>                           # 设置当前shell窗口使用的python版本为指定版本
pyenv versions                                  # 列举所有版本的python，打``*``的为当前指定的全局版本
pyenv version                                   # 列举已经安装的版本
```

##### 使用``virtualenv``创建``Python``虚拟环境
这个命令只需要一个参数，即虚拟环境的名字。创建完虚拟环境后，当前文件夹会出现一个子文件夹，名字就是上述命令中指定的参数，与虚拟环境相关的文件都保存在这个子文件夹中。按照惯例，一般虚拟环境会被命名为``venv``：
```bash
$ virtualenv venv
New python executable in /Users/taoyi/git_projects/Python_Training/flasky/venv/bin/python2.7
Also creating executable in /Users/taoyi/git_projects/Python_Training/flasky/venv/bin/python
Installing setuptools, pip, wheel...done.
```
（Linux或Mac OS X用户）激活当前虚拟环境：
```bash
source venv/bin/activate
```
虚拟环境被激活后，其中``Python``解释器的路径就被添加进``PATH``中，但这种改变不是永久性的，它只会影响当前的命令行会话。为了提醒你已经激活了虚拟环境，激活虚拟环境的命令会修改命令行提示符，加入环境名：
```bash
$ python -V
Python 2.7.14
(venv)
```
如果想回到全局``Python``解析器中，可以再命令行提示符下输入``deactivate``。

##### 使用``virtualenv``创建指定版本的``Python``的虚拟环境
```bash
virtualenv -p /Users/taoyi/.pyenv/versions/3.6.5/bin/python  py3env
```
 - ``-p``：指定指定版本的``python``的绝对路径
 - ``py3env``：创建的虚拟环境的名称

##### Linux环境下，安装``brew``【需要切换git源码地址中的`Linuxbrew`为`Homebrew`，后续，`Linuxbrew`不在更新】
```bash
# clone源码到用户目录下
git clone https://github.com/Linuxbrew/brew.git ~/.linuxbrew
# 把homebrew-core克隆下来
git clone https://github.com/Linuxbrew/homebrew-core ~/.linuxbrew/Library/Taps/homebrew

# 设置环境变量
export PATH="$HOME/.linuxbrew/bin:$PATH"
export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH"
export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"
```

##### Ubuntu环境下，pyenv安装python失败，解决方法
问题基本就是出现在缺少一些基础库上，解决方法也就是尽量的把一些基础库都安装上
```bash
# 在ubuntu软件源里zlib和zlib-devel叫做zlib1g zlib1g.dev
sudo apt-get install zlib1g zlib1g.dev
```

```bash
yum install readline readline-devel readline-static openssl openssl-devel openssl-static sqlite-devel bzip2-devel bzip2-libs build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
```

##### Linux环境下，pyenv安装python3，``ModuleNotFoundError: No module named '_ctypes'``报错解决
python`3.7`版本需要一个新的包`libffi`
```bash
# Ubuntu 下处理
sudo apt-get install libffi-dev
# Centos 下处理
yum install -y libffi-devel
```