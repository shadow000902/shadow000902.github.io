---
title: Mac中Node多版本管理
date: '2020-07-16T01:34:01.000Z'
categories:
  - Tips
tags:
  - node
---

# 2020-07-16-Node-Version-Manage

1. 安装`brew`

   ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
   ```

2. 安装`NVM`

   ```bash
    brew install nvm
   ```

3. 配置环境变量 在环境变量文件中加入如下内容，如`zsh`即为`~/.zshrc`

   ```bash
    export NVM_DIR=~/.nvm
    source $(brew --prefix nvm)/nvm.sh
   ```

4. 安装指定版本的`node`

   ```bash
    nvm install 8.17.0        
    Downloading and installing node v8.17.0...
    Downloading https://nodejs.org/dist/v8.17.0/node-v8.17.0-darwin-x64.tar.xz...
    ######################################################################################################################################################### 100.0%
    Computing checksum with shasum -a 256
    Checksums matched!
    Now using node v8.17.0 (npm v6.13.4)
    Creating default alias: default -> 8.17.0 (-> v8.17.0)
   ```

5. `nvm`常用命令

   ```bash
    nvm ls-remote           # 查看所有的node可用版本
    nvm install xxx         # 下载你想要的版本
    nvm use xxx             # 使用指定版本的node
    nvm alias default xxx   # 每次启动终端都使用该版本的node
   ```

6. 问题解决
7. 问题如下：

   ```bash
     nvm ls-remote
     dyld: Library not loaded: /usr/local/opt/openssl/lib/libssl.1.0.0.dylib
       Referenced from: /usr/local/opt/curl-openssl/bin/curl
       Reason: image not found
     dyld: Library not loaded: /usr/local/opt/openssl/lib/libssl.1.0.0.dylib
       Referenced from: /usr/local/opt/curl-openssl/bin/curl
       Reason: image not found
                 N/A
   ```

8. 解决方法：

   ```bash
     brew switch openssl 1.0.2s
     Cleaning /usr/local/Cellar/openssl/1.0.2s
     Opt link created for /usr/local/Cellar/openssl/1.0.2s
   ```

