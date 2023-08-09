---
title: Python版本管理工具pyenv使用小结
date: 2018-04-10 20:31:28
categories: [Python]
tags: [pyenv, brew]
---

#### 安装``brew``
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

  <!--more-->

#### 安装``pyenv``
```bash
brew install pyenv
```

#### 把``pyenv``加入环境变量
如果使用的终端是``bash``，则编辑``~/.bashrc``，如果使用的终端是``zsh``，则编辑``~/.zshrc``，在该文件的最开头加入语句：
```bash
# pyenv init -  pyenv初始化，把pyenv加入环境变量，使其生效，否则pyenv命令无法使用，pyenv命令是pyenv的核心命令，用于安装、卸载、查看、切换不同版本的python，pyenv的其他命令都是围绕这个命令展开的
eval "$(pyenv init -)"
```

#### ``pyenv``常用基本命令
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

#### 使用``virtualenv``创建``Python``虚拟环境
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

#### 使用``virtualenv``创建指定版本的``Python``的虚拟环境
```bash
virtualenv -p /Users/taoyi/.pyenv/versions/3.6.5/bin/python  py3env
```
 - ``-p``：指定指定版本的``python``的绝对路径
 - ``py3env``：创建的虚拟环境的名称

#### Ubuntu环境下，pyenv安装python失败，解决方法
  报错信息：
  ```bash
  # ubuntu @ VM-4-14-ubuntu in /usr/bin [16:24:51]
  $ pyenv install 3.11.3
  WARNING: Please make sure you remove any previous custom paths from your /home/ubuntu/.pydistutils.cfg file.
  Downloading Python-3.11.3.tar.xz...
  -> https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tar.xz
  Installing Python-3.11.3...
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/home/ubuntu/.pyenv/versions/3.11.3/lib/python3.11/curses/__init__.py", line 13, in <module>
      from _curses import *
  ModuleNotFoundError: No module named '_curses'
  WARNING: The Python curses extension was not compiled. Missing the ncurses lib?
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/home/ubuntu/.pyenv/versions/3.11.3/lib/python3.11/ctypes/__init__.py", line 8, in <module>
      from _ctypes import Union, Structure, Array
  ModuleNotFoundError: No module named '_ctypes'
  WARNING: The Python ctypes extension was not compiled. Missing the libffi lib?
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
  ModuleNotFoundError: No module named 'readline'
  WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
  Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/home/ubuntu/.pyenv/versions/3.11.3/lib/python3.11/ssl.py", line 100, in <module>
      import _ssl             # if we can't import it, let the error propagate
      ^^^^^^^^^^^
  ModuleNotFoundError: No module named '_ssl'
  ERROR: The Python ssl extension was not compiled. Missing the OpenSSL lib?
  
  Please consult to the Wiki page to fix the problem.
  https://github.com/pyenv/pyenv/wiki/Common-build-problems
  
  
  BUILD FAILED (Ubuntu 22.04 using python-build 20180424)
  ...
  ```

##### ``ModuleNotFoundError: No module named '_curses'``报错
  ```shell
  ModuleNotFoundError: No module named '_curses'
  WARNING: The Python curses extension was not compiled. Missing the ncurses lib?
  ```
  解决
  ```shell
  sudo apt-get install libncurses-dev
  ```

##### ``ModuleNotFoundError: No module named '_ctypes'``报错
  ```shell
  ModuleNotFoundError: No module named '_ctypes'
  WARNING: The Python ctypes extension was not compiled. Missing the libffi lib?
  ```
  解决
  ```shell
  sudo apt-get install libffi-dev
  ```


##### ``ModuleNotFoundError: No module named 'readline'``报错
  ```shell
  ModuleNotFoundError: No module named 'readline'
  WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
  ```
  解决
  ```shell
  sudo apt-get install libreadline-dev
  ```

##### ``ModuleNotFoundError: No module named '_ssl'``报错
  ```shell
  ModuleNotFoundError: No module named '_ssl'
  ERROR: The Python ssl extension was not compiled. Missing the OpenSSL lib?
  ```
  解决
  ```shell
  sudo apt-get install libssl-dev
  ```
