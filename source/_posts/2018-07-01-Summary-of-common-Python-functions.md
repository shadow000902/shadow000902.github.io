---
title: Python常用函数总结
date: 2018-07-01 10:18:17
categories: [学习笔记, Python]
tags: [python]
---

### 常用内置函数（不用``import``就可以直接使用）

  <!--more-->

| 函数                          | 说明                                                            |
| ----------------------------- | --------------------------------------------------------------- |
| ``help(obj)``                 | 在线帮助, obj可是任何类型                                       |
| ``callable(obj)``             | 查看一个obj是不是可以像函数一样调用                             |
| ``repr(obj)``                 | 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝 |
| ``eval_r(str)``               | 表示合法的python表达式，返回这个表达式                          |
| ``dir(obj)``                  | 查看obj的name space中可见的name                                 |
| ``hasattr(obj,name)``         | 查看一个obj的name space中是否有name                             |
| ``getattr(obj,name)``         | 得到一个obj的name space中的一个name                             |
| ``setattr(obj,name,value)``   | 为一个obj的name space中的一个name指向vale这个object             |
| ``delattr(obj,name)``         | 从obj的name space中删除一个name                                 |
| ``vars(obj)``                 | 返回一个object的name space。用dictionary表示                    |
| ``locals()``                  | 返回一个局部name space。用dictionary表示                        |
| ``globals()``                 | 返回一个全局name space。用dictionary表示                        |
| ``type(obj)``                 | 查看一个obj的类型                                               |
| ``isinstance(obj,cls)``       | 查看obj是不是cls的instance                                      |
| ``issubclass(subcls,supcls)`` | 查看subcls是不是supcls的子类                                    |

### 类型转换函数

| 函数                  | 说明                                     |
| --------------------- | ---------------------------------------- |
| ``chr(i)``            | 把一个ASCII数值，变成字符                |
| ``ord(i)``            | 把一个字符或者Unicode字符，变成ASCII数值 |
| ``oct(x)``            | 把整数x变成八进制表示的字符串            |
| ``hex(x)``            | 把整数x变成十进制表示的字符串            |
| ``str(obj)``          | 得到obj的字符串描述                      |
| ``list(seq)``         | 把一个sequence转换为一个list             |
| ``tuple(seq)``        | 把一个sequence转换为一个tuple            |
| ``dict(),dict(list)`` | 转换层一个dictionary                     |
| ``int(x)``            | 转换成一个integer                        |
| ``long(x)``           | 转换成一个long integer                   |
| ``float(x)``          | 转换成一个浮点数                         |
| ``complex(x)``        | 转换成复数                               |
| ``max(...)``          | 求最大值                                 |
| ``min(...)``          | 求最小值                                 |

### 和操作系统相关的调用
系统相关的信息模块：``import sys``

| 函数                                | 说明                                               |
| ----------------------------------- | -------------------------------------------------- |
| ``sys.argv``                        | 是一个list，包含所有的命令行参数                   |
| ``sys.stdout,sys.stdin,sys.stderr`` | 分别表示标准输入输出，错误输出的对象               |
| ``sys.stdin.readline()``            | 从标准输入读一行，sys.stdin.readline("a")屏幕输出a |
| ``sys.exit(exit_code)``             | 退出程序                                           |
| ``sys.modules``                     | 是一个dictionary，表示系统中所有可用的module       |
| ``sys.platform``                    | 得到运行的操作系统环境                             |
| ``sys.path``                        | 是一个list，知名所有查找的module，package的路径    |

### 操作系统相关的调用和操作
相关的信息模块：``import os``

| 函数               | 说明                                                                             |
| ------------------ | -------------------------------------------------------------------------------- |
| ``os.environ``     | 一个dictionary包含环境变量的映射关系，os.environ["HOME"]可以得到环境变量HOME的值 |
| ``os.chdir(dir)``  | 改变当前目录，os.chdir('~/Desktop')                                              |
| ``os.getcwd()``    | 得到当前目录                                                                     |
| ``os.getegid()``   | 得到有效组id，os.getgid()得到组id                                                |
| ``os.geteuid()``   | 得到有效用户id，os.getuid()得到组id                                              |
| ``os.getgroups()`` | 得到用户组名称列表                                                               |
| ``os.getlogin()``  | 得到用户登录名称                                                                 |
| ``os.getenv``      | 得到环境变量                                                                     |
| ``os.putenv``      | 设置环境变量                                                                     |
| ``os.umask``       | 设置umask                                                                        |
| ``os.system(cmd)`` | 利用系统调用，运行cmd命令                                                        |

### 用``os.path``编写平台无关的程序

| 函数                                                            | 说明                                                                  |
| --------------------------------------------------------------- | --------------------------------------------------------------------- |
| ``os.path.abspath("1.txt")==os.path.join(os.getcwd(),"1.txt")`` |
| ``os.path.split(os.getcwd())``                                  | 用于分开一个目录名称中的目录部分和文件名称部分                        |
| ``os.path.join(os.getcwd(),os.pardir,'a','a.doc')``             | 全称路径名称，os.pardir表示当前平台下上一级目录的字符                 |
| ``os.path.getctime("/root/1.txt")``                             | 返回1.txt的ctime（创建时间）时间戳                                    |
| ``os.path.exists(os.getcwd)``                                   | 判断文件是否存在                                                      |
| ``os.path.expanduser('~/dir')``                                 | 把~扩展成用户根目录                                                   |
| ``os.path.expandvars('$PATH')``                                 | 扩展环境变量PATH                                                      |
| ``os.path.isfile(os.getcwd())``                                 | 判断是否是目录，1是0否                                                |
| ``os.path.isdir('~/Desktop')``                                  | 判断是否是目录，1是0否                                                |
| ``os.path.islink('/home/taoyi/test.sql')``                      | 是否是符号连接                                                        |
| ``os.path.ismout(os.getcwd)``                                   | 是否是文件系统安装点                                                  |
| ``os.path.samefile(os.getcwd(),'/home/taoyi')``                 | 看看两个文件名是不是指的是同一个文件                                  |
| ``os.path.walk('/home/taoyi',test_fun,"a.c")``                  | 遍历/home/taoyi下所有子目录包括目录，对于每个目录都会调用函数test_fun |

### 文件操作

| 函数                       | 说明                                                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| ``f=open("filename","r")`` | r只读；w写；rw读写；rb读二进制；wb写二进制；w+写追加                                                                            |
| ``f.write("a")``           | 写字符串                                                                                                                        |
| ``f.read()``               | 全读出来，f.read(size)表示从文件中读取size个字符                                                                                |
| ``f.readline()``           | 读一行，到文件结尾，返回空串；f.readlines()                                                                                     |
| ``f.tell()``               | 返回当前文件读取位置                                                                                                            |
| ``f.seek(off,where)``      | 定位文件读写位置，off表示偏移量，正数向文件尾移动，负数表示向开通移动，where为0表示从开始算起，1表示从当前位置算，2表示从结尾算 |
| ``f.flush()``              | 刷新缓存                                                                                                                        |
| ``f.close()``              | 关闭文件                                                                                                                        |
