---
title: Python常用函数整理
date: 2018-08-23 23:52:25
categories: [Python]
tags: [python]
---

1. ``range``
    ```python
    range(101)                  # 产生一个0到100的整数序列
    range(1, 100)               # 产生一个1到99的整数序列
    range(1, 100, 2)            # 产生一个1到99的奇数序列，其中2是步长，即数值序列的增量
    range(100, 1, -2)           # 产生一个100到2的偶数序列，其中-2是步长，最后一个序列值是2
    ```

<!--more-->

2. ``input``
    ```python
    raw = input('请输入：')     # 用于读取控制台输入的值
    ```

3. Python内置函数
    - 数学相关: abs / divmod / pow / round / min / max / sum
    - 序列相关: len / range / next / filter / map / sorted / slice / reversed
    - 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
    - 数据结构: dict / list / set / tuple
    - 其他函数: all / any / id / input / open / print / type

4. Python常用模块
    - 运行时服务相关模块: copy / pickle / sys / ...
    - 数学相关模块: decimal / math / random / ...
    - 字符串处理模块: codecs / re / ...
    - 文件处理相关模块: shutil / gzip / ...
    - 操作系统服务相关模块: datetime / os / time / logging / io / ...
    - 进程和线程相关模块: multiprocessing / threading / queue
    - 网络应用相关模块: ftplib / http / smtplib / urllib / ...
    - Web编程相关模块: cgi / webbrowser
    - 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

5. 函数的参数
    - 默认参数
    - 可变参数
    - 关键字参数
    - 命名关键字参数
    ```python
    # 可变参数
    def f2(*args):
        sum = 0
        for num in args:
            sum += num
        return sum

    print(f2(1, 2, 3))
    ```
    ```python
    # 关键字参数
    def f3(**kw):
        if 'name' in kw:
            print('欢迎你%s!' % kw['name'])
        elif 'tel' in kw:
            print('你的联系电话是: %s!' % kw['tel'])
        else:
            print('没找到你的个人信息!')

    param = {'name': '骆昊', 'age': 38}
    f3(**param)
    f3(name='骆昊', age=38, tel='13866778899')
    ```
