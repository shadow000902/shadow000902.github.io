---
title: Python小技巧
date: 2018-03-06 21:08:43
categories: [Python]
tags: [python]
---

##### 安装指定版本的第三方库
```bash
pip install robotframework==2.8.7
```
要用``pip``安装指定版本的``Python``包，只需通过``==``操作符指定即可。

  <!--more-->

##### 将当前虚拟环境中的依赖包以版本号生成至文件中：
```bash
pip freeze > requirements.txt
```

##### 在指定位置安装第三方
```bash
pip install -t /Users/taoyi/.pyenv/versions/2.7.14/lib/python2.7/site-packages lxml
```
``pip``安装的包不一定是用户想要的位置，此时可以用``-t``选项来指定位置。

##### 通过requirement.txt文件来管理pip的第三方库
文件内容如下：
```bash
robotframework==3.0.2
robotframework-ride==1.5.2
robotframework-appiumlibrary==1.4.6
robotframework-DatabaseLibrary==1.0.1
robotframework-Selenium2Library==3.0.0
robotframework-requests==0.4.7
robotframework-sshlibrary==2.1.3
robotframework-HttpLibrary==0.4.2
requests==2.18.4
PyMySQL==0.8.0
MySQL-python==1.2.5
```
然后通过以下命令来批量安装第三方库
```bash
pip install -r requirement.txt
```

##### 查看有更新的``pip``第三方库
```zsh
# taoyi @ TaoYi-Mac in ~ [16:27:56]
$ pip list --outdate --trusted-host pypi.douban.com
Package                                     Version Latest    Type
------------------------- ------- ------- -----
robotframework-ride             1.5.2     1.5.2.1 sdist
robotframework-sshlibrary 2.1.3     3.0.0     sdist
setuptools                                28.8.0    39.1.0    wheel
```

##### 更新指定的第三方库
```bash
pip install --upgrade robotframework-sshlibrary
```

##### 查看第三方库的详细信息
```bash
pip show robotframework-sshlibrary
```

##### pip配置文件更新
``pip``配置文件是``~/.pip/pip.conf``文件
```bash
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[global]                                                                                            # 设置pip的全局的源
index-url = http://pypi.douban.com/simple

[install]                                                                                         # pip install指定的安装源
trusted-host=pypi.douban.com

[list]                                                                                                # pip list命令接口的展示方式设置
format=columns
```

##### ``print('*',end='')``中``end``问题
end是print（）函数的一个参数。end 是输出语句结束以后附加的字符串，它的默认值是换行（’\n’）。
```python
print('')#end值为默认值（换行\n）
print('*',end = ' ')                # end值为空格
print('*',end = '')                 # 默认为末尾换行/n，end=''末尾为空所以不换行
print('*',end = '1')                # end值为字符串‘1’
print('*',end = '12')             # end值为字符串‘12’
```

##### 打印中的赋值语句
```python
print ('%d * %d = %d' %(i, j, i * j), end='\t')
# 三个%d分别从后面跟着的3个参数取对应的值
```

##### VSCode的代码段设置
```json
{
    "MarkDown insert Pyhton": {
        "prefix": "MDP",
        "body": [
            "```python\n\n\n```",
            "$2"
        ],
        "description": "MarkDown insert Pyhton"
    }
}
```

##### 共享本地文件给局域网访问
```bash
python -m http.server
```
共享当前运行该命令的本地目录，给予在局域网内访问；默认共享端口为8000，即访问地址为：[localhost:8000](http://localhost:8000)

##### 字典在for循环中数据覆盖的分析与解决
预期打印出来的list为：[{'num': 0}, {'num': 1}, {'num': 2}]，结果为[{'num': 2}, {'num': 2}, {'num': 2}]
```python
lists=[]
dictionary={"num":""}
for i in range(3):
    dictionary["num"]=i
    lists.append(dictionary)
print(lists)                 #[{'num': 2}, {'num': 2}, {'num': 2}]
```
解决：将字典写在for循环中，得到预期的list[{'num': 0}, {'num': 1}, {'num': 2}]
```python
lists=[]
for i in range(3):
    dictionary = {"num": ""}
    dictionary["num"]=i
    lists.append(dictionary)
print(lists)                 #[{'num': 0}, {'num': 1}, {'num': 2}]
```
原因分析：

    1. dictionary（字典）赋给list的是一个位置
    
    2. dictionary定义在循环外，每次使用list.append(dictionary)赋给 list的都是相同的位置，即指向了同一块的地址；当在同一地址的dictionary的值已经改变了，所以list取到的之前位置的值改变了，表现出后面数据覆盖前面数据的表象

    3. dictionary定义在循环内，相当于每一次循环生成一个dictionary，占用不同的位置存储值，所以可以赋给list不同元素不同的位置，获得不同的值。 

总结：

    1. 对于不能理解地址，可以通过在循环中print(id(dictionary))，将地址打印出来对比分析

    2. 在python中，对象赋值实际上是对象的引用。当创建一个对象，然后把它赋给另一个变量的时候，python并没有拷贝这个对象，而只是拷贝了这个对象的引用

    3. 关于Python中复制、浅拷贝和深拷贝的区别
      - 直接赋值，传递对象的引用而已，原始列表改变，被赋值的b也会做相同的改变
      - copy浅拷贝，只拷贝父对象，不会拷贝对象的内部的子对象，所以原始数据改变，子对象会改变
      - copy深拷贝，包含对象里面的自对象的拷贝，所以原始对象的改变不会造成深拷贝里任何子元素的改变

##### 全局变量和局部变量
```python
def test():
    if value == 1:
        a += 1
    return a

value = a = 1
b = test()
```
执行上述代码就会出现`UnboundLocalError: local variable 'a' referenced before assignment`这个报错。
因为在函数内部对变量赋值进行修改后，该变量就会被Python解释器认为是局部变量而非全局变量，当程序执行到a+=1的时候，因为这条语句是给a赋值，所以a成为了局部变量，那么在执行return a(或是print a)的时候，因为a这个局部变量还没有定义，自然就会抛出这样的错误。

解决方案一：
当全局变量。就是使用global关键字，在函数内部先声明a这个变量是全局变量。代码如下：
```python
def test():
    global a
    if value == 1:
        a += 1
    return a

value = a = 1
b = test()
```
这时，a就成为了全局变量，在函数内部修改该变量，也就没有问题了。
这种情况外面的a执行完函数是2，而函数返回的也是2。

解决方案二：
当局部变量。就是这个变量只在函数内使用，那么只要在函数内把这个变量定义一下就行了。代码如下：
```python
def test():
    a = 1
    if value == 1:
        a += 1
    return a

value = a = 1
b = test()
```
这种情况外面的a执行完函数还是1，而函数返回的则是2。

##### `requests.post`使用
1. 带数据『data』的post
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    url = ''.join([host,endpoint])
    data = {'key1':'value1','key2':'value2'}
    
    r = requests.post(url,data=data)
    #response = r.json()
    print (r.text)
    ```

2. 带header的post
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    
    url = ''.join([host,endpoint])
    headers = {"User-Agent":"test request headers"}
    
    # r = requests.post(url)
    r = requests.post(url,headers=headers)
    #response = r.json()
    ```

3. 带json的post
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    
    url = ''.join([host,endpoint])
    data = {
        "sites": [
                    { "name":"test" , "url":"www.test.com" },
                    { "name":"google" , "url":"www.google.com" },
                    { "name":"weibo" , "url":"www.weibo.com" }
        ]
    }
    
    r = requests.post(url,json=data)
    # r = requests.post(url,data=json.dumps(data))
    response = r.json()
    ```

4. 带参数『params』的post
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    
    url = ''.join([host,endpoint])
    params = {'key1':'params1','key2':'params2'}
    
    # r = requests.post(url)
    r = requests.post(url,params=params)
    #response = r.json()
    print (r.text)
    ```

5. 普通文件上传
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    
    url = ''.join([host,endpoint])
    #普通上传
    files = {
                'file':open('test.txt','rb')
            }
    
    r = requests.post(url,files=files)
    print (r.text)
    ```

6. 定制化文件上传
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    
    url = ''.join([host,endpoint])
    #自定义文件名，文件类型、请求头
    files = {
            'file':('test.png',open('test.png','rb'),'image/png')
    }
    
    r = requests.post(url,files=files)
    print (r.text)
    ```

7. 多文件上传
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    
    url = ''.join([host,endpoint])
    #多文件上传
    files = [
        ('file1',('test.txt',open('test.txt', 'rb'))),
        ('file2', ('test.png', open('test.png', 'rb')))
        ]
    
    r = requests.post(url,files=files)
    print (r.text)
    ```

8. 流式上传
    ```python
    # -*- coding:utf-8 -*-
    import requests
    import json
    
    host = "http://httpbin.org/"
    endpoint = "post"
    
    url = ''.join([host,endpoint])
    
    #流式上传
    with open( 'test.txt' ) as f:
        r = requests.post(url,data = f)
    
    print (r.text)
    ```