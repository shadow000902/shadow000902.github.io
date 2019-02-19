#### blog_source
##### 项目目录结构
```bash
── LICENSE
├── README.md
├── _config.yml                                     # 博客配置文件
├── db.json
├── debug.log
├── git_push.sh
├── node_modules                                    # 执行 npm install 后，第三方包存放的地址
│   ├── JSONStream
│   ├── a-sync-waterfall
...
│   ├── [省略很多npm包]
...
│   ├── ws
│   ├── y18n
│   ├── yallist
│   └── yargs
├── package-lock.json
├── package.json                                    # 项目所有的第三方 npm 包列表，执行 npm install 会安装里面所有的包
├── scaffolds
│   ├── draft.md
│   ├── page.md
│   └── post.md
├── shadow000902.github.io.iml
├── source
│   ├── 404.html
│   ├── CNAME                                       # 域名映射文件
│   ├── _drafts                                     # 草稿存放地
│   ├── _posts                                      # 文章存放地
│   ├── about
│   ├── categories
│   ├── favicon.ico
│   ├── images
│   ├── pay.png
│   └── tags
├── themes
│   └── next-6                                      # 项目主题
├── update_native.sh
└── update_online.sh
```
