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

##### `httprunner`框架中`https`请求报错解决
1. 接口请求的参数中，增加参数`'verify': False`
```python
_data = {'name': api_data.name,
         'verify': False,
         'request': {'method': api_data.method,
                     'files': {},
                     'data': {},
                     'headers': {}}}
```
2. 框架修改
修改`venv/lib/python3.7/site-packages/httprunner/parser.py`文件
修改参数`config.pop("verify", False)`中原来的`True`为`False`
```python
    config_variables = config.get("variables", {})
    config_base_url = config.pop("base_url", "")
    config_verify = config.pop("verify", False)
    functions = project_mapping.get("functions", {})
```