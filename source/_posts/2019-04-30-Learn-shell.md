---
title: shell学习笔记
date: 2019-04-30 17:07:00
categories: [Shell]
tags: [shell]
---

##### 命令嵌套【嵌套语句通过 \`\` 来标记】
```bash
for list in \
`find /root/.jenkins/jobs/DEBUG-UZAO-*/ -maxdepth 1 -type f -name config.xml`\
;do sed -i s/$now_branch/$new_branch/g $list\
;done
```

  <!--more-->


