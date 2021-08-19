---
title: 基于Docker&Selenium的WEB自动化平台搭建
date: '2019-09-19T00:24:23.000Z'
categories:
  - 环境搭建
  - Selenium
tags:
  - docker
  - selenium
---

# 2019-09-19-Docker-Selenium-environment-build

## 安装`Docker`

[MAC平台](https://download.docker.com/mac/stable/Docker.dmg) [Windows平台](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) [Ubuntu平台](https://www.runoob.com/docker/ubuntu-docker-install.html) [Centos7平台](https://blog.csdn.net/xinzhifu1/article/details/83579256)

## 下载主`hub`镜像`selenium/hub`

```bash
# 安装
docker pull selenium/hub
# 启动容器
docker run -d -P --name selenium-hub selenium/hub
```

`-d` 表示容器以守护态（Daemonized）形式运行。 `-P` 表示 Docker 会随机映射一个 49000~49900 的端口到内部容器开放的网络端口。

## 下载主`node chrome`镜像`selenium/node-chrome`

```bash
# 安装
docker pull selenium/node-chrome
# 启动容器
docker run -d --link selenium-hub:hub selenium/node-chrome
```

`--link` 通过 link 关联`selenium-hub`容器，并为其设置了别名`hub`

## 查看容器

```bash
$ docker ps -a
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS                     PORTS                                            NAMES
65bdddeb9293        selenium/node-chrome   "/opt/bin/entry_poin…"   17 seconds ago      Up 16 seconds                                                               intelligent_mirzakhani
a280e0bce3a4        selenium/hub           "/opt/bin/entry_poin…"   38 seconds ago      Up 36 seconds              0.0.0.0:32768->4444/tcp                          selenium-hub
```

`Selenium/hub`容器的端口号为`4444`，对`MAC`映射的端口为`32768`，前面通过`-P`参数自动分配。

## 工作原理

selenium Grid脚本 -&gt; ubuntu\(32768\) -&gt; Hub容器\(4444\) -&gt; Node Chrome 容器

## 创建Grid测试脚本与运行

```python
# grid_demo.py

from selenium import webdriver
from time import sleep

driver = webdriver.Remote(
command_executor='http://127.0.0.1:32768/wd/hub',
desired_capabilities={'browserName': 'chrome'}
)

driver.get('https://www.baidu.com')
print("get baidu")

driver.find_element_by_id("kw").send_keys("docker selenium")
driver.find_element_by_id("su").click()

sleep(1)

driver.get_screenshot_as_file("~/baidu_img.png")

driver.quit()
print("end...")
```

```bash
docker run --name=chrome -p 5902:5900 \
    -e NODE_MAX_INSTANCES=5 \
    -e NODE_MAX_SESSION=5 \
    -e NODE_REGISTER_CYCLE=5000 \
    -e DBUS_SESSION_BUS_ADDRESS=/dev/null \
    --link hub -d selenium/node-chrome-debug:3.7.1-beryllium
```

