---
title: android无线adb连接和投屏
date: 2019-05-26 01:33:02
categories: [Tips]
tags: [adb]
---

#### `adb`无线连接
1. 手机有线模式下连接电脑，且手机开启了USB调试模式，效果如下
    ```bash
    # taoyi @ TyMac in ~ [1:18:55] 
    $ adb devices
    List of devices attached
    63faca2b	device
    ```

  <!--more-->

2. 执行命令打开`tcpip`端口
    ```bash
    # taoyi @ TyMac in ~ [1:18:59] 
    $ adb tcpip 5555
    restarting in TCP mode port: 5555
    ```
3. 执行无线连接安卓手机命令
    先要拔除USB连接
    ```bash
    # taoyi @ TyMac in ~ [1:24:58] 
    $ adb connect 192.168.31.233:5555
    connected to 192.168.31.233:5555
    ```
    出现这个提示，说明无线连接成功了。
4. 验证连接是否成功
    ```bash
    # taoyi @ TyMac in ~ [1:25:21] C:1
    $ adb devices
    List of devices attached
    192.168.31.233:5555	device
    ```
    出现如上提示，说明无线模式的调试模式也可以有效进行了。
5. 关闭前面打开的无线连接端口的设备
    ```bash
    # taoyi @ TyMac in ~ [1:25:21] C:1
    $ adb devices
    List of devices attached
    192.168.31.233:5555	device
    192.168.31.233:5556	offline
    ```
    如上之前打开过一个`5556`的端口，因为也没有用到，且是掉线状态，如果留着，那连接的设备就不是唯一了，需要进行指定了，造成了一定的麻烦，所以需要手动删除该连接的设备，实际也就是关闭该设备的在线状态
6. 查看端口占用的PID信息等
    ```bash
    # taoyi @ TyMac in ~ [1:54:51] C:130
    $ lsof -i tcp:5555
    COMMAND   PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    adb     94280 taoyi   14u  IPv4 0x38c46a3265bac391      0t0  TCP 192.168.31.71:49360->192.168.31.233:personal-agent (ESTABLISHED)
    ```

    ```bash
    # taoyi @ TyMac in ~ [1:53:59] 
    $ ps -ef | grep fork-server
      UID   PID  PPID   C STIME   TTY         TIME CMD
      501 94280     1   0  3:44下午 ??         2:00.63 adb -L tcp:5037 fork-server server --reply-fd 5
      501 21281 16612   0  1:56上午 ttys000    0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn fork-server
    ```
7. `kill`掉刚才已经`offline`的设备的链接的`PID`，就可以删除该设备了


#### 无线投屏
1. 安卓投屏软件
    ```bash
    brew install scrcpy
    ```
2. 在完成上一节中的无线连接调试后，完成无线投屏
    ```bash
    # taoyi @ TyMac in ~ [1:27:04] 
    $ scrcpy                
    /usr/local/Cellar/scrcpy/1.8/share/scrcpy/scrcpy-server.jar: 1 file pushed. 0.4 MB/s (19850 bytes in 0.048s)
    2019-05-26 01:27:32.921 scrcpy[17790:9101920] INFO: Initial texture: 1080x2248
    ```
    在完成`scrcpy`的安装后，直接执行`scrcpy`的命令就可以完成无线投屏了。
3. `scrcpy`常用命令
    ```bash
    # 设置端口
    scrcpy -p 27184
    # 查看帮助
    scrcpy --help
    # 设置码率（默认8M）
    scrcpy -b 8M
    # 限制投屏尺寸
    scrcpy -m 1024
    # 裁剪投屏屏幕(长:宽:偏移x:偏移y)
    scrcpy -c 800:800:0:0
    # 投屏并录屏
    scrcpy -r file.mp4
    # 不投屏只录屏
    scrcpy -Nr file.mp4
    # 手指触摸的时候显示轨迹球
    scrcpy -t
    # 显示版本信息
    scrcpy -v
    ```

4. 快捷方式
    
    Action|Shortcut
    ---|---
    切换全屏模式|Ctrl+f
    将窗口调整为1：1（完美像素）|Ctrl+g
    调整窗口大小以删除黑色边框|Ctrl+x / 双击黑色背景
    设备HOME键|Ctrl+h / 鼠标中键
    设备BACK键|Ctrl+b / 鼠标右键
    设备任务管理键|Ctrl+s
    设备 菜单 键|Ctrl+m
    设备音量+键|Ctrl+↑
    设备音量-键|Ctrl+↓
    设备电源键|Ctrl+p
    点亮手机屏幕|鼠标右键
    复制内容到设备|Ctrl+v
    启用/禁用FPS计数器（stdout）|Ctrl+i
    安装APK|将apk文件拖入投屏
    传输文件到设备|将文件拖入投屏（非apk）
