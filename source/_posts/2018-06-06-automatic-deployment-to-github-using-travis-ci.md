---
title: 使用Travis CI自动部署Hexo博客到Github上
date: '2018-06-06T23:49:49.000Z'
categories:
  - Tools
tags:
  - hexo
  - github
  - travis ci
---

# 2018-06-06-Automatic-deployment-to-Github-using-Travis-CI

## `Travis CI`介绍

`Travis CI`是目前新兴的开源持续集成构建项目，它与`jenkins`，`GO`的很明显的特别在于采用`yaml`格式，同时他是在在线的服务，不像`jenkins`需要你本地打架服务器，简洁清新独树一帜。目前大多数的`github`项目都已经移入到`Travis CI`的构建队列中，据说`Travis CI`每天运行超过_4000_次完整构建。对于做开源项目或者`github`的使用者，如果你的项目还没有加入`Travis CI`构建队列，那么我真的想对你说out了。

## 博客架构

使用Hexo来搭建的，托管到Github提供的Gitpage服务上。 `master`：博客的静态文件，也就是`hexo`生成后的`HTML`文件，因为要使用`Gitpage`服务，所以他规定的网页文件必须是在`master`分支

## 具体项目在`Travis CI`的设置

使用`GitHub`账号登录[Travis CI官网](https://travis-ci.org/)，并同步`GitHub`的项目到`Travis CI`。

在`Travis CI`开启项目

然后进入项目在`Travis CI`的设置页，配置好选项和参数。

`Build only if .travis.yml is present`：只有在.travis.yml文件中配置的分支改变了才构建 `Build pushed branches`：当推送完这个分支后开始构建

## `Travis CI`访问`GitHub`的设置

在github上生成Access Token：

生成完后，你需要拷贝下来，只有这时候他才显示，再次进来为了安全它就不会显示了；如果忘了只能重新生成一个了，拷贝完以后我们需要到`Travis CI`网站下配置。

配置在这里的主要原因是为了安全，写在代码里，就保证不了安全了，所以就以环境变量的形式配置在项目设置里，需要的时候，从配置里去引用它。

## 配置`Travis CI`执行脚本`.travis.yml`

```text
language: node_js
node_js: stable

# S: Build Lifecycle
install:
  # 更新所有在package.json中设置的第三方库
  - npm install
  # 修复更新的错误
  - npm audit fix


#before_script:
 # - npm install -g gulp

script:
  # 设置git用户名
  - git config user.name "shadow000902"
  # 设置git邮箱
  - git config user.email "shadow000902@gmail.com"
  # 创建主题文件夹
  - mkdir -p themes
  - cd themes

  # 因为主题是属于另一个git项目，无法发布到博客源码所在的项目，所以需要重新从git拉取
  # 下载自己的主题``next-6``
  - git clone https://github.com/shadow000902/next-6.git

  # 因为第三方插件都是一个独立的git项目，无法发布到另一个git项目中，所以需要在主题拉取后，再独立的拉取代码到对应的主题插件目录下
  # 在主题中加载第三方插件``algolia``
  - git clone https://github.com/theme-next/theme-next-algolia-instant-search next-6/source/lib/algolia-instant-search
  # 在主题中加载第三方插件``fancybox``
  - git clone https://github.com/theme-next/theme-next-fancybox3 next-6/source/lib/fancybox
  # 在主题中加载第三方插件``pace``
  - git clone https://github.com/theme-next/theme-next-pace next-6/source/lib/pace
  # 以上的两个操作没有的话，博客部署后，就处于无主题的状态，是无法访问的

  - cd ..
  - hexo g

after_script:
  - cd ./public
  - git init
  - git config user.name "shadow000902"
  - git config user.email "shadow000902@gmail.com"
  - git add .
  - git commit -m "Update docs"
  - git push --force --quiet "https://${blogSource_Token}@${blogSource_Git}" master:master
# E: Build LifeCycle

branches:
  only:
    - blog_source
env:
 global:
   - blogSource_Git: github.com/shadow000902/shadow000902.github.io.git
```

以上脚本需要提交到博客源代码的根目录下：

## 完工

以上操作都完毕后，只要在博客源代码`git`项目中，如果有更新，或者在`.travis.yml`文件有更新时，项目就会自动部署，并更新博客内容。

