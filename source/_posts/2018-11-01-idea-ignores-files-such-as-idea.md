---
title: IDEA忽略掉.idea等文件
date: '2018-11-01T00:43:44.000Z'
categories:
  - Tips
tags:
  - idea
---

# 2018-11-01-IDEA-ignores-files-such-as-idea

`idea`需要下载一个专门的`plugins`来`ignore`、`.idea`、`*.iml`等文件，名称为`.ignore`。

然后`git status`就会发现`.idea/`文件消失,但是也可能还是有,可能是因为对应的目录被`git`跟踪过，可以通过运行一下命令解决：

```bash
git rm -rf --cached .idea
```

