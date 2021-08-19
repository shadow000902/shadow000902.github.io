---
title: Python相关问题解决总结
date: '2019-05-12T18:25:27.000Z'
categories:
  - Python
tags:
  - python
---

# 2019-05-12-python-common-tips

## `pytest`每次运行都会报`ValueError: option names {'--alluredir'} already added`

原因是同时安装了`pytest-allure-adaptor`和`allure-pytest`，而它俩又都被引用了，造成了冲突。 解决方案：

```text
卸载掉其中一个
全局搜索哪些地方引用了，处理掉别的引用
```

## `httprunner`框架中`https`请求报错解决

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

## 运行需要网络请求的`python`脚本，提示`libssl`找不到

报错提示如下：

```bash
# shadow @ shadow in /usr/local/lib [17:55:16] 
$ python
Python 3.7.0 (default, Oct  1 2018, 10:38:36) 
[Clang 10.0.0 (clang-1000.11.45.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ssl
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/shadow/.pyenv/versions/3.7.0/lib/python3.7/ssl.py", line 98, in <module>
    import _ssl             # if we can't import it, let the error propagate
ImportError: dlopen(/Users/shadow/.pyenv/versions/3.7.0/lib/python3.7/lib-dynload/_ssl.cpython-37m-darwin.so, 2): Library not loaded: /usr/local/opt/openssl/lib/libssl.1.0.0.dylib
  Referenced from: /Users/shadow/.pyenv/versions/3.7.0/lib/python3.7/lib-dynload/_ssl.cpython-37m-darwin.so
  Reason: image not found
```

**原因**： `brew`升级了`OpenSSL`版本到`OpenSSL@1.1`，所以`libssl.1.0.0.dylib`这个旧版本的库文件被卸载了，新的是`libssl.1.1.1.dylib`，旧版本的`python`没有更新链接，所以就会报找不到`/usr/local/opt/openssl/lib/libssl.1.0.0.dylib`

**解决方法**： 卸载之前引用了低版本的`python`，然后重新安装`python`就可以了

