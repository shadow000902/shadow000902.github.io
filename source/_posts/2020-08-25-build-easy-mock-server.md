---
title: EasyMock服务搭建
date: '2020-08-25T18:07:04.000Z'
categories:
  - 环境搭建
  - Mock
tags:
  - mock
---

# 2020-08-25-Build-Easy-Mock-Server

## Mock服务搭建整体步骤

* 克隆`GitHub`代码仓库
* 安装`Node`环境
* 安装`MongoDB`服务
* 安装`Redis`服务
* 安装`Mock`服务

## 克隆代码

```bash
git clone https://github.com/easy-mock/easy-mock.git
cd easy-mock && npm install
```

## 安装Node服务

推荐使用`nvm`来管理本地`Node`服务，方便随意切换`Node`版本

```bash
brew install nvm
```

[Linux下安装Brew](https://shadow000902.space/2018/04/10/2018-04-10-Python-version-management-tool-pyenv-use-summary/) 然后再安装指定版本的Node

```bash
nvm install 10.22.0
```

## 安装MongoDB服务

[安装MongoDB服务](https://shadow000902.space/2017/01/18/2017-01-18-Useing-Extent-test-report/) 注意文件目录需要放在当前用户有权限的位置，否则可能会有无法辨别的报错信息

## 安装Redis服务

[Redis服务部署](https://shadow000902.space/2017/06/18/2017-06-18-Building-a-Redis-environment-under-Mac/)

## 启动Mock服务

基本命令如下：

```bash
$ npm run dev
# Visit http://127.0.0.1:7300

# More Commands
# Build front-end assets
$ npm run build

# Run Easy Mock as production environment (You should run `build` first)
$ npm run start

# Run unit test
$ npm run test

# Test lint
$ npm run lint
```

服务启动后，登录主页如下：

如果IP+Port的方式无法访问，可能就是网络上的访问的限制了，可以配置一个域名映射解决

## 异常处理

### curl报错

```bash
# shadow @ kickseed in ~/easy-mock on git:dev x [17:43:05] C:1
$ brew reinstall nvm
==> Reinstalling nvm 
==> Downloading https://github.com/creationix/nvm/archive/v0.33.11.tar.gz
Error: An exception occurred within a child process:
  RuntimeError: no executable curl was found
```

安装curl命令：

```bash
sudo apt-get install curl
```

### webpack报错

报错信息如下：

```bash
# shadow @ kickseed in ~/easy-mock on git:dev x [17:53:45] 
$ npm run build                                                 

> easy-mock@1.6.0 build /home/shadow/easy-mock
> cross-env NODE_ENV=production npm run build:dev


> easy-mock@1.6.0 build:dev /home/shadow/easy-mock
> rimraf dist && npm run build:client && npm run build:server


> easy-mock@1.6.0 build:client /home/shadow/easy-mock
> webpack --config build/webpack.client.config.js --progress --hide-modules

WARNING: NODE_ENV value of 'production' did not match any deployment config file names.
WARNING: See https://github.com/lorenwest/node-config/wiki/Strict-Mode
 23% building modules 116/140 modules 24 active ...odules/js-beautify/js/lib/beautify.jsnode[6188]: ../src/node_file.cc:943:void node::fs::Stat(const v8::FunctionCallbackInfo<v8::Value>&): Assertion `(argc) == (4)' failed.
 1: 0x8fb090 node::Abort() [node]
 2: 0x8fb165  [node]
 3: 0x93bb1a  [node]
 4: 0xb917ef  [node]
 5: 0xb92359 v8::internal::Builtin_HandleApiCall(int, v8::internal::Object**, v8::internal::Isolate*) [node]
 6: 0x3744a845be1d 
Aborted
npm ERR! code ELIFECYCLE
npm ERR! errno 134
npm ERR! easy-mock@1.6.0 build:client: `webpack --config build/webpack.client.config.js --progress --hide-modules`
npm ERR! Exit status 134
npm ERR! 
npm ERR! Failed at the easy-mock@1.6.0 build:client script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/shadow/.npm/_logs/2020-08-25T09_54_02_278Z-debug.log
npm ERR! code ELIFECYCLE
npm ERR! errno 134
npm ERR! easy-mock@1.6.0 build:dev: `rimraf dist && npm run build:client && npm run build:server`
npm ERR! Exit status 134
npm ERR! 
npm ERR! Failed at the easy-mock@1.6.0 build:dev script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/shadow/.npm/_logs/2020-08-25T09_54_02_300Z-debug.log
npm ERR! code ELIFECYCLE
npm ERR! errno 134
npm ERR! easy-mock@1.6.0 build: `cross-env NODE_ENV=production npm run build:dev`
npm ERR! Exit status 134
npm ERR! 
npm ERR! Failed at the easy-mock@1.6.0 build script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/shadow/.npm/_logs/2020-08-25T09_54_02_315Z-debug.log
```

需要安装webpack，命令如下：

```bash
sudo apt-get install webpack
```

### node报错

```bash
# shadow @ kickseed in ~/easy-mock on git:dev x [17:54:02] C:134
$ npm run dev  

> easy-mock@1.6.0 dev /home/shadow/easy-mock
> nodemon --ignore views/ --ignore public/ app

[nodemon] 1.14.11
[nodemon] to restart at any time, enter `rs`
[nodemon] watching: *.*
[nodemon] starting `node app.js`
server started at http://0.0.0.0:7300
{"t":{"$date":"2020-08-25T17:54:29.409+08:00"},"s":"I",  "c":"NETWORK",  "id":22943,   "ctx":"listener","msg":"connection accepted","attr":{"remote":"127.0.0.1:59488","sessionId":5,"connectionCount":1}}
{"t":{"$date":"2020-08-25T17:54:29.415+08:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:59488","client":"conn5","doc":{"driver":{"name":"nodejs","version":"2.2.34"},"os":{"type":"Linux","name":"linux","architecture":"x64","version":"4.4.0-140-generic"},"platform":"Node.js v10.22.0, LE, mongodb-core: 2.1.18"}}}
{"t":{"$date":"2020-08-25T17:54:29.435+08:00"},"s":"I",  "c":"NETWORK",  "id":22943,   "ctx":"listener","msg":"connection accepted","attr":{"remote":"127.0.0.1:59492","sessionId":6,"connectionCount":2}}
{"t":{"$date":"2020-08-25T17:54:29.440+08:00"},"s":"I",  "c":"NETWORK",  "id":22943,   "ctx":"listener","msg":"connection accepted","attr":{"remote":"127.0.0.1:59494","sessionId":7,"connectionCount":3}}
{"t":{"$date":"2020-08-25T17:54:29.443+08:00"},"s":"I",  "c":"NETWORK",  "id":22943,   "ctx":"listener","msg":"connection accepted","attr":{"remote":"127.0.0.1:59496","sessionId":8,"connectionCount":4}}
/home/shadow/.nvm/versions/node/v10.22.0/bin/node[6242]: ../src/node_file.cc:943:void node::fs::Stat(const v8::FunctionCallbackInfo<v8::Value>&): Assertion `(argc) == (4)' failed.
 1: 0x8fb090 node::Abort() [/home/shadow/.nvm/versions/node/v10.22.0/bin/node]
 2: 0x8fb165  [/home/shadow/.nvm/versions/node/v10.22.0/bin/node]
 3: 0x93bb1a  [/home/shadow/.nvm/versions/node/v10.22.0/bin/node]
 4: 0xb917ef  [/home/shadow/.nvm/versions/node/v10.22.0/bin/node]
 5: 0xb92359 v8::internal::Builtin_HandleApiCall(int, v8::internal::Object**, v8::internal::Isolate*) [/home/shadow/.nvm/versions/node/v10.22.0/bin/node]
 6: 0x3a1c83a5be1d 
{"t":{"$date":"2020-08-25T17:54:39.976+08:00"},"s":"I",  "c":"NETWORK",  "id":22944,   "ctx":"conn8","msg":"connection ended","attr":{"remote":"127.0.0.1:59496","connectionCount":3}}
{"t":{"$date":"2020-08-25T17:54:39.976+08:00"},"s":"I",  "c":"NETWORK",  "id":22944,   "ctx":"conn7","msg":"connection ended","attr":{"remote":"127.0.0.1:59494","connectionCount":1}}
{"t":{"$date":"2020-08-25T17:54:39.976+08:00"},"s":"I",  "c":"NETWORK",  "id":22944,   "ctx":"conn6","msg":"connection ended","attr":{"remote":"127.0.0.1:59492","connectionCount":0}}
[nodemon] app crashed - waiting for file changes before starting...
{"t":{"$date":"2020-08-25T17:54:39.976+08:00"},"s":"I",  "c":"NETWORK",  "id":22944,   "ctx":"conn5","msg":"connection ended","attr":{"remote":"127.0.0.1:59488","connectionCount":2}}
```

切换node版本为8.17.0

```bash
nvm install 8.17.0
```

