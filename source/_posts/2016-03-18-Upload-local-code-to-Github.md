---
title: Git使用总结
date: 2016-03-18 14:54:16
categories: [Tips]
tags: [github]
---

### 上传本地代码到Github
1. 准备工作
    安装github for windows客户端

  <!--more-->

2. 上传代码
    1. 在自己的github账户上创建一个新的仓库（repository）
    2. 登录github for windows客户端，clone下来刚才创建的repository：
    {% asset_img clone刚才创建的repository到本地.png clone刚才创建的repository到本地 %}
    3. 复制本地完整代码到clone下来的repository文件夹中
    4. github for windows客户端自动检测未上传的文件，勾选需要上传的文件，commit到master或者其他分支中
    {% asset_img 上传代码.png 上传代码 %}
    5. 点击客户端右上角的Sync按钮
    
    至此，本地的代码就上传到了github上。

### 强制推送一个版本的代码到一个已存在的远程仓库
```shell
# taoyi @ tysYZMac in ~/Desktop/public on git:master x [17:00:23] 
$ git init
已重新初始化已存在的 Git 仓库于 /Users/taoyi/Desktop/public/.git/

# taoyi @ tysYZMac in ~/Desktop/public on git:master x [17:00:26] 
$ git add .

# taoyi @ tysYZMac in ~/Desktop/public on git:master x [17:00:36] 
$ git commit -m "Update docs"                
[master（根提交） 30f486f] Update docs
 602 files changed, 13450 insertions(+)
 create mode 100644 2016/01/01/2016-01-01-Java-Learning-Notes/index.html
 create mode 100644 2016/03/12/2016-03-12-Learning-Hexo/index.html
 ...
 ...
 create mode 100644 "tags/\350\275\257\344\273\266\346\265\213\350\257\225\346\265\201\347\250\213\347\256\241\347\220\206/index.html"
 create mode 100644 "tags/\351\207\215\347\255\276\345\220\215/index.html"

# taoyi @ tysYZMac in ~/Desktop/public on git:master o [17:01:12] C:130
$ git push --force https://e.coding.net/shadow000902/shadow000902.coding.me.git master:master                                         
Username for 'https://e.coding.net': 13003665526
Password for 'https://13003665526@e.coding.net': <令牌的Token>
枚举对象中: 1155, 完成.
对象计数中: 100% (1155/1155), 完成.
使用 8 个线程进行压缩
压缩对象中: 100% (821/821), 完成.
写入对象中: 100% (1155/1155), 31.79 MiB | 26.49 MiB/s, 完成.
总共 1155（差异 348），复用 0（差异 0），包复用 0
remote: Resolving deltas: 100% (348/348), done.
To https://e.coding.net/shadow000902/shadow000902.coding.me.git
 + 0a12f7e...30f486f master -> master (forced update)

```

### Git切换远程仓库地址
1. 方法一：直接修改远程仓库地址
    ```bash
    git remote set-url origin url
    ```

2. 方法二：删除本地远程仓库地址，然后添加新的仓库地址
    ```bash
    git remote rm origin
    git remote add origin url
    ```

3. 方法三：修改配置文件
    每个仓库在初始化时，都会有一个`.git`的隐藏目录，修改其中的`config`文件中的`url`
    ```bash
    [core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = true
    [remote "origin"]
        url = git://github.com/robbyrussell/oh-my-zsh.git
        fetch = +refs/heads/*:refs/remotes/origin/*
    [branch "master"]
        remote = origin
        merge = refs/heads/master
    ```
    
4. 查看远程仓库地址
    ```bash
    git remote -v
    ```

### 合并两个不同的仓库

```shell
# 本地仓库oldRepo中添加远程仓库newRepo
git remote add newRepo https://github.com/shadow000902/newRepo.git
# 从远程仓库newRepo中拉取数据到本地仓库中
git fetch newRepo
# 将远程仓库newRepo中拉取的develop分支作为新分支checkout到本地，新分支名为 newRepo/develop
git checkout -b newRepo/develop newRepo/develop
# 切换回本地仓库oldRepo的develop分支
git checkout develop
# 将 newRepo/develop 分支合并入 develop 分支
git merge newRepo/develop
# 解决冲突并推送到远程
...
```


