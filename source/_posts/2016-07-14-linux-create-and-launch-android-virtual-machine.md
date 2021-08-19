---
title: Linux命令创建及启动Android虚拟机
date: '2016-07-14T23:56:13.000Z'
categories:
  - Linux
tags:
  - linux
---

# 2016-07-14-Linux-create-and-launch-Android-virtual-machine

## 提升Android原生模拟器速度的方法

在Android SDK Manager中勾选中Inter X86 Emulator Accelerator \(HAXM installer\)，然后安装它

## 查看支持的模拟器Android版本号

```text
android list
```

显示如下：

```text
TaoYi-Mac:~ taoyi$ android list
Available Android targets:
----------
id: 1 or "android-23"
     Name: Android 6.0
     Type: Platform
     API level: 23
     Revision: 3
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, WXGA720, WXGA800, WXGA800-7in
 Tag/ABIs : default/armeabi-v7a, default/x86, default/x86_64, google_apis/armeabi-v7a, google_apis/x86, google_apis/x86_64
----------
id: 2 or "android-24"
     Name: Android N
     Type: Platform
     API level: 24
     Revision: 1
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, WXGA720, WXGA800, WXGA800-7in
 Tag/ABIs : no ABIs.
----------
id: 3 or "Google Inc.:Google APIs:23"
     Name: Google APIs
     Type: Add-On
     Vendor: Google Inc.
     Revision: 1
     Description: Android + Google APIs
     Based on Android 6.0 (API level 23)
     Libraries:
      * com.android.future.usb.accessory (usb.jar)
          API for USB Accessories
      * com.google.android.media.effects (effects.jar)
          Collection of video effects
      * com.google.android.maps (maps.jar)
          API for Google Maps
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, WXGA720, WXGA800, WXGA800-7in
 Tag/ABIs : no ABIs.
Available Android Virtual Devices:
Available devices definitions:
id: 0 or "tv_1080p"
    Name: Android TV (1080p)
    OEM : Google
    Tag : android-tv
---------
id: 1 or "tv_720p"
    Name: Android TV (720p)
    OEM : Google
    Tag : android-tv
---------
id: 2 or "wear_round"
    Name: Android Wear Round
    OEM : Google
    Tag : android-wear
---------
id: 3 or "wear_round_chin_320_290"
    Name: Android Wear Round Chin
    OEM : Google
    Tag : android-wear
---------
id: 4 or "wear_square"
    Name: Android Wear Square
    OEM : Google
    Tag : android-wear
---------
id: 5 or "Device001"
    Name: Device001
    OEM : User
---------
id: 6 or "Galaxy Nexus"
    Name: Galaxy Nexus
    OEM : Google
---------
id: 7 or "Nexus 10"
    Name: Nexus 10
    OEM : Google
---------
id: 8 or "Nexus 4"
    Name: Nexus 4
    OEM : Google
---------
id: 9 or "Nexus 5"
    Name: Nexus 5
    OEM : Google
---------
id: 10 or "Nexus 6"
    Name: Nexus 6
    OEM : Google
---------
id: 11 or "Nexus 7 2013"
    Name: Nexus 7
    OEM : Google
---------
id: 12 or "Nexus 7"
    Name: Nexus 7 (2012)
    OEM : Google
---------
id: 13 or "Nexus 9"
    Name: Nexus 9
    OEM : Google
---------
id: 14 or "Nexus One"
    Name: Nexus One
    OEM : Google
---------
id: 15 or "Nexus S"
    Name: Nexus S
    OEM : Google
---------
id: 16 or "2.7in QVGA"
    Name: 2.7" QVGA
    OEM : Generic
---------
id: 17 or "2.7in QVGA slider"
    Name: 2.7" QVGA slider
    OEM : Generic
---------
id: 18 or "3.2in HVGA slider (ADP1)"
    Name: 3.2" HVGA slider (ADP1)
    OEM : Generic
---------
id: 19 or "3.2in QVGA (ADP2)"
    Name: 3.2" QVGA (ADP2)
    OEM : Generic
---------
id: 20 or "3.3in WQVGA"
    Name: 3.3" WQVGA
    OEM : Generic
---------
id: 21 or "3.4in WQVGA"
    Name: 3.4" WQVGA
    OEM : Generic
---------
id: 22 or "3.7 FWVGA slider"
    Name: 3.7" FWVGA slider
    OEM : Generic
---------
id: 23 or "3.7in WVGA (Nexus One)"
    Name: 3.7" WVGA (Nexus One)
    OEM : Generic
---------
id: 24 or "4in WVGA (Nexus S)"
    Name: 4" WVGA (Nexus S)
    OEM : Generic
---------
id: 25 or "4.65in 720p (Galaxy Nexus)"
    Name: 4.65" 720p (Galaxy Nexus)
    OEM : Generic
---------
id: 26 or "4.7in WXGA"
    Name: 4.7" WXGA
    OEM : Generic
---------
id: 27 or "5.1in WVGA"
    Name: 5.1" WVGA
    OEM : Generic
---------
id: 28 or "5.4in FWVGA"
    Name: 5.4" FWVGA
    OEM : Generic
---------
id: 29 or "7in WSVGA (Tablet)"
    Name: 7" WSVGA (Tablet)
    OEM : Generic
---------
id: 30 or "10.1in WXGA (Tablet)"
    Name: 10.1" WXGA (Tablet)
    OEM : Generic
```

## 创建AVD模拟器

```text
android create avd -n TestDevices001 -t 1 -b armeabi-v7a
```

```text
-t --target         # 新的AVD的Target ID（必须）
-c --sdcard         # 指定一个共享的SD存储卡的路径或者是为新的AVD定制的新的SD存储卡的容量大小，如：-t 512M。（“M”必须大写）
-p --path           # 新的AVD将被创建的位置路径
-n --Name           # 新的AVD的名字（必须）
-f --force          # 强制创建（覆盖已存在的AVD）
-s --skin           # 新的AVD的皮肤
-b --abi            # 例如android-24里面的abi有armeabi-v7a/x86/x86_64，此时就需要指定，如果只有一个abi，则不需要指定
```

## 查看AVD是否创建成功

```text
android list avd
```

结果如下，就说明创建成功了

```text
TaoYi-Mac:~ taoyi$ android list avd
Available Android Virtual Devices:
    Name: TestDevices001
    Path: /Users/taoyi/.android/avd/TestDevices001.avd
  Target: Android 6.0 (API level 23)
 Tag/ABI: default/armeabi-v7a
    Skin: WVGA800
```

## 启动AVD

```text
TaoYi-Mac:~ taoyi$ emulator -avd TestDevices001
emulator: WARNING: Increasing RAM size to 1024MB
emulator: WARNING: Classic qemu does not support SMP. The hw.cpu.ncore option from your config file is ignored.
Creating filesystem with parameters:
    Size: 69206016
    Block size: 4096
    Blocks per group: 32768
    Inodes per group: 4224
    Inode size: 256
    Journal blocks: 1024
    Label:
    Blocks: 16896
    Block groups: 1
    Reserved block group size: 7
Created filesystem with 11/4224 inodes and 1302/16896 blocks
```

```text
TaoYi-Mac:~ taoyi$ emulator  -port 5676  -avd TestDevices001  -no-window -no-skin -no-audio -no-boot-anim &
sh: 1: glxinfo: not found
emulator: WARNING: Increasing RAM size to 1024MB
sh: 1: glxinfo: not found
emulator: WARNING: Classic qemu does not support SMP. The hw.cpu.ncore option from your config file is ignored.

Your emulator is out of date, please update by launching Android Studio:
 - Start Android Studio
 - Select menu "Tools > Android > SDK Manager"
 - Click "SDK Tools" tab
 - Check "Android SDK Tools" checkbox
 - Click "OK"
```

## 删除AVD

```text
android delete avd -n TestDevices001
```

## 异常处理

1. `sdkmanager`命令执行，提示`Could not create settings`问题处理
2. 错误提示如下：

   ```bash
     $ ./sdkmanager --list
     Warning: Could not create settings
     java.lang.IllegalArgumentException
             at com.android.sdklib.tool.sdkmanager.SdkManagerCliSettings.<init>(SdkManagerCliSettings.java:428)
             at com.android.sdklib.tool.sdkmanager.SdkManagerCliSettings.createSettings(SdkManagerCliSettings.java:152)
             at com.android.sdklib.tool.sdkmanager.SdkManagerCliSettings.createSettings(SdkManagerCliSettings.java:134)
             at com.android.sdklib.tool.sdkmanager.SdkManagerCli.main(SdkManagerCli.java:57)
             at com.android.sdklib.tool.sdkmanager.SdkManagerCli.main(SdkManagerCli.java:48)
     Usage:
       sdkmanager [--uninstall] [<common args>] [--package_file=<file>] [<packages>...]
       sdkmanager --update [<common args>]
       sdkmanager --list [<common args>]
       sdkmanager --licenses [<common args>]
       sdkmanager --version
   ```

   即使设置了`ANDROID_SDK_HOME`环境变量，也把`sdkmanager`所在目录加入到了`PATH`，仍然会报同样的错误

3. _临时解决方案_： 在执行`sdkmanager`命令的时候，加上`--sdk_root=...`的参数

   ```bash
     ./sdkmanager --list --sdk_root=~/Downloads/tools/bin
     [=======================================] 100% Computing updates...             
     Available Packages:
   ```

   这样就能得到正确的输出了，但是每次都要加上`--sdk_root`也不是长久之计。

4. _根本解决方案_：

一句话描述即为：通过下载的`commandlinetools-mac-6609375_latest.zip`文件解压后，生成的目录中的`sdkmanager`，重新下载生成整个`androidsdk`目录，并加入到环境变量中，然后删除下载解压的目录，使用重新生成的目录。

* 下载创建新的基础`androidsdk`目录

  ```bash
    $ cd ~/androidsdk
    $ unzip commandlinetools-mac-6609375_latest.zip
    $ ll
    commandlinetools-mac-6609375_latest.zip
    tools
    $ cd tools/bin
    $ ./sdkmanager --sdk_root=~/androidsdk/tools "cmdline-tools;latest"
    $ cd ~/androidsdk/cmdline-tools/latest
    $ ll
    total 216
    -rwxr-xr-x@  1 shadow  staff    83K  7  2 10:59 NOTICE.txt
    drwxr-xr-x@  7 shadow  staff   224B  7  2 10:59 bin
    drwxr-xr-x@ 22 shadow  staff   704B  7  2 10:59 lib
    -rw-r--r--@  1 shadow  staff    17K  7  2 10:59 package.xml
    -rwxr-xr-x@  1 shadow  staff    84B  7  2 10:59 source.properties
  ```

    通过以上命令，即生成了可用的`sdkmanager`命令可用的`androidsdk`目录

* 设置环境变量

  设置环境变量的系统变量，增加一个`ANDROID_SDK_HOME`，设置为`~/androidsdk` 设置环境变量的用户变量，在`PATH`中增加`$ANDROID_SDK_HOME/cmdline-tools/latest/bin` 最后就可以删除之前下载解压的`tools`目录了

  ```bash
    $ sdkmanager --version                                          
    26.1.1
  ```

  然后命令就正常了，也不需要`--sdk_root`参数了

* `emulator`命令执行，提示`No such file or directory`问题处理
* SDK根目录如下：

  ```bash
    # shadow @ kickseed in ~/androidsdk [18:55:54] 
    $ ll
    total 36K
    drwxrwxr-x 3 shadow shadow 4.0K Jul 14 11:52 build-tools
    drwxrwxr-x 3 shadow shadow 4.0K Jul 14 11:32 cmdline-tools
    drwxrwxr-x 7 shadow shadow 4.0K Jul 14 11:48 emulator
    drwxrwxr-x 2 shadow shadow 4.0K Jul 14 11:52 licenses
    drwxrwxr-x 3 shadow shadow 4.0K Jul 14 11:46 patcher
    drwxrwxr-x 3 shadow shadow 4.0K Jul 14 11:49 platforms
    drwxrwxr-x 5 shadow shadow 4.0K Jul 14 11:45 platform-tools
    drwxrwxr-x 3 shadow shadow 4.0K Jul 14 11:52 system-images
    drwxrwxr-x 6 shadow shadow 4.0K Jul 16 18:54 tools
  ```

* 报错信息如下：

  ```bash
    emulator: error while loading shared libraries: libtcmalloc_minimal.so.4: cannot open shared object file: No such file or directory
  ```

  ```bash
    which emulator 
    /home/shadow/androidsdk/tools/emulator
  ```

  执行`which emulator`命令，发现调用的是`tools`目录下的`emulator`，导致无法找到创建的`avd`，因为安卓虚拟机对应的命令路径是在`emulator`目录下。 所以我们需要让默认调用的`emulator`命令变成`emulator`目录下的`emulator`命令 方法一：调整环境变量，让初始化环境变量的时候，`tools`目录位于`emulator`目录之前，这样就能确保`emulator`目录下的`emulator`命令覆盖`tools`目录下的命令 方法二：直接删除`tools`目录下的`emulator`命令文件

