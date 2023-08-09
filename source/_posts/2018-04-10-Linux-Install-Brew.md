---
title: Linux环境下安装Brew
date: 2018-04-10 15:19:14
categories: [Tips]
tags: [linux, brew]
---

### Linux环境下，自定义安装``brew``
需要切换git源码地址中的`Linuxbrew`为`Homebrew`，后续，`Linuxbrew`不在更新
1. clone源码到用户目录下
    ```bash
    git clone https://github.com/homebrew/brew.git ~/.homebrew
    ```

  <!--more-->

2. 把homebrew-core克隆下来
    ```bash
    git clone https://github.com/Homebrew/homebrew-core.git ~/.homebrew/Library/Taps/homebrew
    ```

3. 设置环境变量
```bash
export PATH="$HOME/.homebrew/bin:$PATH"
export MANPATH="$HOME/.homebrew/share/man:$MANPATH"
export INFOPATH="$HOME/.homebrew/share/info:$INFOPATH"
```

### brew官方安装方案
```bash
# ubuntu @ VM-4-14-ubuntu in ~ [17:00:38] C:1
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
==> This script will install:
/home/linuxbrew/.linuxbrew/bin/brew
/home/linuxbrew/.linuxbrew/share/doc/homebrew
/home/linuxbrew/.linuxbrew/share/man/man1/brew.1
/home/linuxbrew/.linuxbrew/share/zsh/site-functions/_brew
/home/linuxbrew/.linuxbrew/etc/bash_completion.d/brew
/home/linuxbrew/.linuxbrew/Homebrew

Press RETURN/ENTER to continue or any other key to abort:
[sudo] password for ubuntu:
==> /usr/bin/sudo /bin/chown -R ubuntu:ubuntu /home/linuxbrew/.linuxbrew/Homebrew
==> Downloading and installing Homebrew...
remote: Enumerating objects: 242456, done.
remote: Counting objects: 100% (103/103), done.
remote: Compressing objects: 100% (89/89), done.
remote: Total 242456 (delta 12), reused 96 (delta 10), pack-reused 242353
Receiving objects: 100% (242456/242456), 70.81 MiB | 581.00 KiB/s, done.
Resolving deltas: 100% (177525/177525), done.
From https://github.com/Homebrew/brew
 * [new branch]          dependabot/bundler/Library/Homebrew/json_schemer-0.2.25 -> origin/dependabot/bundler/Library/Homebrew/json_schemer-0.2.25
 * [new branch]          master                                                  -> origin/master
 * [new tag]             0.1                                                     -> 0.1
 * [new tag]             0.2                                                     -> 0.2
 * [new tag]             0.3                                                     -> 0.3
 * [new tag]             0.4                                                     -> 0.4
 * [new tag]             0.5                                                     -> 0.5
......
 * [new tag]             4.0.5                                                   -> 4.0.5
 * [new tag]             4.0.6                                                   -> 4.0.6
 * [new tag]             4.0.7                                                   -> 4.0.7
 * [new tag]             4.0.8                                                   -> 4.0.8
 * [new tag]             4.0.9                                                   -> 4.0.9
HEAD is now at 322a0189c Merge pull request #15529 from carlocab/deps-fix
==> Downloading https://ghcr.io/v2/homebrew/portable-ruby/portable-ruby/blobs/sha256:68923daf3e139482b977c3deba63a3b54ea37bb5f716482948878819ef911bad
Already downloaded: /home/ubuntu/.cache/Homebrew/portable-ruby-2.6.10_1.x86_64_linux.bottle.tar.gz
==> Pouring portable-ruby-2.6.10_1.x86_64_linux.bottle.tar.gz
Warning: /home/linuxbrew/.linuxbrew/bin is not in your PATH.
  Instructions on how to configure your shell for Homebrew
  can be found in the 'Next steps' section below.
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics data has been sent yet (nor will any be during this install run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations

==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
    (echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/ubuntu/.zprofile
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
- Install Homebrew's dependencies if you have sudo access:
    sudo apt-get install build-essential
  For more information, see:
    https://docs.brew.sh/Homebrew-on-Linux
- We recommend that you install GCC:
    brew install gcc
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh

```
