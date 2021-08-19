---
title: Linux环境下安装Brew
date: '2018-04-10T15:19:14.000Z'
categories:
  - Tips
tags:
  - linux
  - brew
---

# Linux环境下，安装brew

需要切换git源码地址中的`Linuxbrew`为`Homebrew`，后续，`Linuxbrew`不在更新 1. clone源码到用户目录下

```bash
git clone https://github.com/Linuxbrew/brew.git ~/.linuxbrew
```

1. 把homebrew-core克隆下来

   ```bash
   git clone https://github.com/Linuxbrew/homebrew-core ~/.linuxbrew/Library/Taps/homebrew
   ```

2. 设置环境变量

   ```bash
   export PATH="$HOME/.linuxbrew/bin:$PATH"
   export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH"
   export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"
   ```

