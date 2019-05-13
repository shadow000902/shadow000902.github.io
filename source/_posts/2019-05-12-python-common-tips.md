---
title: Python相关问题解决总结
date: 2019-05-12 18:25:27
categories: [Python]
tags: [python]
---

##### `pytest`每次运行都会报`ValueError: option names {'--alluredir'} already added`
原因是同时安装了`pytest-allure-adaptor`和`allure-pytest`，而它俩又都被引用了，造成了冲突。
解决方案：

	卸载掉其中一个
	全局搜索哪些地方引用了，处理掉别的引用

