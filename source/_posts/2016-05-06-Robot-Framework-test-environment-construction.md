---
title: Robot-Framework测试环境搭建
date: 2016-05-06 14:16:53
categories: [RobotFramework]
tags: [robot-framework]
---

### 安装python环境。
由于Robot Framework是基于python2开发的，所以必须选择安装python2版本，不然会造成很多异常，之后需要的一些依赖python2的库也无法安装。这里我选择安装的是[Anaconda2](https://www.continuum.io/downloads)，它自身就包含较多的python库，比较好用。

  <!--more-->

### 安装Appium。如果安装过程中遇到问题，还请看[Appium安装](http://shadow000902.space/2016/03/31/Appium安装/)
```bash
npm install appium -g
```

### 安装Robot Framework
#### 源码安装。[下载地址](https://pypi.python.org/pypi/robotframework)
```bash
cd .../robotframework/
python setup.py install
```
#### 通过pip安装
```bash
pip install robotframework
```

### 安装wxPython。[下载地址](http://www.wxpython.org/download.php)
#### windows环境：exe文件，正常安装
#### **mac环境**：``brew``安装，修改源码
```bash
brew install wxpython                   # 使用Homebrew安装wxpython
```
对于``wxPython``的版本控制语句存在于``/Library/Python/2.7/site-packages/robotide/__init__.py``文件中
```python
import sys
import os
from string import Template

errorMessageTemplate = Template("""$reason
You need to install wxPython 2.8.12.1 with unicode support to run RIDE.
 36 wxPython 2.8.12.1 can be downloaded from http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/""")
supported_versions = ["2.8"]

try:
    import wxversion
    from wxversion import VersionError
    if sys.platform == 'darwin':
        supported_versions.append("2.9")
        supported_versions.append("3.0")            # 新增该代码，让ride支持wxpython3.0
    wxversion.select(supported_versions)
    import wx
```

### 查看 wxpython 是否在环境变量中
```bash
brew info wxpython
```
这说明正常
```bash
# taoyi @ TYMAC in ~ [1:57:29] C:1
$ brew info wxpython
wxpython: stable 3.0.2.0 (bottled)
Python bindings for wxWidgets
https://www.wxwidgets.org/
/usr/local/Cellar/wxpython/3.0.2.0_1 (1,108 files, 37.9MB) *
  Poured from bottle on 2018-09-05 at 01:53:47
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/wxpython.rb
==> Dependencies
Required: python@2 ✔, wxmac ✔
```


### 安装ride。
RIDE 是``Robot Framework``测试数据的编辑器。它使测试用例的创建、运行、测试项目的组织可以在图形界面下完成。
#### 源码安装。[下载地址](https://pypi.python.org/pypi/robotframework-ride)
```bash
cd .../robotframework-ride/
python setup.py install
```
#### 通过pip安装
```bash
pip install robotframework-ride
```
最新版本``1.5.2.1``可能会出现闪退的问题，那就需要降级，先卸载该版本，然后下载``1.5.2``版本

### 命令行启动ride
#### Windows
定位到ride安装的位置，`C:\Anaconda2\Scripts\`
```bash
python ride.py
```
#### mac
ride.py已经自动加入到了环境变量下面
可以直接通过运行``ride.py``执行

### 安装robotframework-appiumlibrary
```bash
pip install robotframework-appiumlibrary
```

### 安装robotframework-selenium2library
```bash
pip install robotframework-selenium2library
```

### Mac 下 pkg 安装 Python2.7，启动 ride.py
Mac 下 pkg 安装 Python2.7 的情况下，pip 快捷目录为`/usr/local/bin/pip`，也就是`/Library/Frameworks/Python.framework/Versions/2.7/bin/pip`对应的软连接的位置的文件，对应的第三方库安装位置为`/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/`。
然后通过`/usr/local/bin/pip install robotframework-ride==1.5.2`来安装`ride.py`，再通过`brew`来安装`wxpython`，最后就能通过`/Library/Frameworks/Python.framework/Versions/2.7/bin/ride.py`来启动`ride.py`，如果`/usr/local/bin/ride.py`没有生成的话。

### **Mac下一定能成功启动ride的方法**
#### brew 安装 python@2和python
```bash
brew install python@2
brew install python
```
如果检查系统中存在用安装包安装过的python，则全部删除干净，包括`/usr/local/bin`目录下存在的和python相关的所有软链和硬链
然后用上述命令安装好python，同时就会在`/usr/local/bin`目录下新增对应的软链命令。

#### 安装 wxpython
首先使用brew来安装wxpython
```bash
brew install wxpython
```
后面会说到，如果不行的话，就需要用pip来安装wxpython
```bash
# 使用指定的pip来安装wxpython
/usr/local/bin/pip3 install wxpython
```
该命令安装的是python3支持的ride，后面会说

#### 安装ride
```bash
# 由于默认情况下会安装1.7.3.1版本，该版本在mac下会报pywin32不存在的问题，怀疑这个版本是只支持Windows系统的，所以安装如下版本
/usr/local/bin/pip3 install robotframework-ride==1.7.3
```
正常情况下，按照如上的步骤，ride是一定能够启动的
```bash
/usr/local/bin/ride.py
```

#### 解释下为啥都用绝对路径来调用命令，而不是使用比如`pip3`
原因是，可能我们安装了虚拟环境，且虚拟环境在环境变量初始化的时候被提前了，这样就不会去寻找`/usr/local/bin`目录下的命令，可以使用which命令确认一下
如果which命令显示的就是`/usr/local/bin`目录下的命令，那就可以直接调用，不需要使用绝对路径访问了

```bash
# taoyi @ TyMac in ~ [0:12:56] 
$ which ride.py 
/Users/taoyi/.pyenv/shims/ride.py
```
这种情况就需要使用`/usr/local/bin/ride.py`来启动ride

```bash
# taoyi @ TyMac in ~ [0:13:00] 
$ which ride.py
/usr/local/bin/ride.py
```
这种情况就只需要使用`ride.py`来启动ride



### 问题解决

#### 遇到ride无法启动的问题【Windows】
```bash
Python 2.7.11 |Anaconda 4.0.0 (64-bit)| (default, Feb 16 2016, 09:58:36) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> from robotide import main
wxPython not found.
You need to install wxPython 2.8 toolkit with unicode support to run RIDE.
wxPython 2.8.12.1 can be downloaded from
http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/
```
安装的ride是基于wxPython 2.8.12.1 编译的，所以就需要安装 wxPython 2.8.12.1。

还有另一个问题，可能会遇到ride界面工具crash的问题
需要删除``.robotframework``
```bash
rm -rf ~/.robotframework/
```

#### mac 强制安装 wxpython2.8.12.1 或 wxpython3.0.2.0
1. 下载[wxPython2.8-osx-unicode-2.8.12.1-universal-py2.7.dmg](https://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/wxPython2.8-osx-unicode-2.8.12.1-universal-py2.7.dmg/download)
2. 下载[wxPython3.0-osx-3.0.2.0-cocoa-py2.7.dmg (36.0 MB)
](https://nchc.dl.sourceforge.net/project/wxpython/wxPython/3.0.2.0/wxPython3.0-osx-3.0.2.0-cocoa-py2.7.dmg)
3. 打开得到``wxPython2.8-osx-unicode-universal-py2.7.pkg``；右键显示包内容，再得到``wxPython2.8-osx-unicode-universal-py2.7.pax.gz``和``postflight``；解压``wxPython2.8-osx-unicode-universal-py2.7.pax.gz``，再得到``/usr/local/lib/wxPython-unicode-2.8.12.1``，把该文件夹放入系统的``/usr/local/lib/``中，切换到``postflight``目录，运行命令``sudo ./postflight``，安装好wxpython2.8.12.1。
4. 执行``ride.py``提示：
    ```bash
    python should be executed in 32-bit mode with wxPython on OSX.
    ```
    是因为wxpython是32位的，而我们安装的是64位的。
    输入以下命令强制执行32位：
    ```bash
    defaults write com.apple.versioner.python Prefer-32-Bit -bool yes
    ```

#### ride 一次使用后再次打开崩溃的问题
因为用``pip install robotframework-ride``安装的``ride``是1.5.2.1版本，会出现这个问题，所以安装指定的1.5.2版本
```bash
pip install robotframework-ride==1.5.2
```

#### 切换使用``pyenv``来管理python环境后，``ride.py``无法启动
因为安装的``ride.py``在启动时，调用了虚拟环境的``python``，但是虚拟环境的python无法启动GUI界面，所以如果需要使用``ride.py``的GUI界面，就需要从系统python安装的``ride.py``去启动。
这样就需要使用系统的``pip``，也就是``/usr/local/bin/``目录下的``pip``来安装``ride.py``。
然后通过``/usr/local/bin/ride.py``来启动``ride.py``。

#### wxpython 缺失问题解决
```bash
# taoyi @ TYMAC in ~/Desktop [21:22:36]
$ /usr/local/bin/ride.py
Wrong wxPython version.
You need to install wxPython 2.8.12.1 with unicode support to run RIDE.
wxPython 2.8.12.1 can be downloaded from http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/
```

因为brew默认启用的地址为：/Users/taoyi/Library/Python/2.7/lib/python/site-packages/
后面的文件夹路径若没有则需要新建：mkdir -p /Users/taoyi/Library/Python/2.7/lib/python/site-packages
再执行：echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/taoyi/Library/Python/2.7/lib/python/site-packages/homebrew.pth

#### ``ImportError: cannot import name 'pub'`` 问题解决
```bash
pip install pypubsub
```