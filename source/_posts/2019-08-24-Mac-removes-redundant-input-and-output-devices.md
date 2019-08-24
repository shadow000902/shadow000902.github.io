---
title: Mac删除多余的输入输出设备
date: 2019-08-24 11:12:45
categories: [Tips]
tags: [mac]
---

查看3个目录：
```shell script
/Library/Extensions/
/System/Library/Extensions/
/Library/Audio/Plug-Ins/HAL/
```

  <!--more-->

比如`Apowersoft_Audio Device`，软件卸载后，在`/System/Library/Extensions/`目录下会残留一个`Apowersoft_AudioDevice.kext`
删除该文件，然后重启电脑，就能发现，该多余的音频设备就已经不存在了

再比如`Easy Connect Audio`,软件卸载后，在`/System/Library/Extensions/`目录下会残留一个`Antecea_AudioDiv.kext`
删除该文件并重启后，就能删除该多余的输入输出设备了