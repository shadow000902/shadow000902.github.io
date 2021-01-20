---
title: web.py数据库操作介绍
date: 2017-01-11 20:35:36
categories: [Python]
tags: [web.py, 数据库]
---

### 安装包安装MySQL数据库

#### 本地数据库的安装[MySQL](http://dev.mysql.com/downloads/mysql/)
安装完后，会给出一个默认密码：

  <!--more-->

{% asset_img 初始化密码.png 初始化密码 %}

#### 启动本机上的MySQL
{% asset_img 启动MySQL-1.png 启动MySQL-1 %}
{% asset_img 启动MySQL-2.png 启动MySQL-2 %}
{% asset_img 启动MySQL-3.png 启动MySQL-3 %}

#### 修改MySQL默认密码

```bash
➜  ~ mysql -u root -p       
Enter password:         # 输入刚才安装后生成的密码
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 18
Server version: 5.7.17 MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SET PASSWORD = PASSWORD('123456');           # 重置密码
```
这样就把MySQL的登录密码设置成了``123456``

### Brew安装MySQL数据库

#### Brew执行安装命令
```bash
# taoyi @ taoyiDSC000331 in /usr/local [17:01:58] C:1
$ brew install mysql
...
==> mysql
We've installed your MySQL database without a root password. To secure it run:
    mysql_secure_installation

MySQL is configured to only allow connections from localhost by default

To connect run:
    mysql -uroot

To have launchd start mysql now and restart at login:
  brew services start mysql
Or, if you don't want/need a background service you can just run:
  mysql.server start
```

#### 设置MySQL的root账户密码
默认情况下，brew安装的MySQL是没有root密码的，基于安全考虑，需要设置一个密码
执行`mysql_secure_installation`命令后，跟着提示步骤走就可以了
```bash
# taoyi @ taoyiDSC000331 in /usr/local [18:02:32] 
$ mysql_secure_installation

Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: Y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
Please set the password for root here.

New password: 

Re-enter new password: 

Estimated strength of the password: 50 
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : a

New password: 

Re-enter new password: 

Estimated strength of the password: 50 
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : Y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : Y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : N

 ... skipping.
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : Y
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : Y
Success.

All done!
```

### 安装Web.py及相关数据库操作模块

1. 安装``web.py``
```bash
easy_install web.py
```
2. 安装``MySQLdb``
```bash
easy_install MySQLdb
```
3. 安装``psycopg2``
```bash
easy_install psycopg2
```
4. 安装``DBUtils``，用于连接池``database pool``功能
```bash
easy_install DBUtiles
```

### web.py操作数据库

#### 导入模块，定义数据库连接``db``
```bash
import web
db = web.database(dbn = 'mysql', db = 'mytable', user = 'root', pw = '123456')
# dbn 用于指定数据库类型
```

#### ``select``查询
```python
# 查询表
entries = db.select('mytable')

# where 条件
myvar = dict(name = "Bob")
results = db.select('mytable', myvar, where = "name = $name")
results = db.select('mytable', where = "id>100")

# 查询具体列
results = db.select('mytable', what = "id, name")

# order by
results = db.select('mytable', order = "post_date DESC")

# group
results = db.select('mytable', group = "color")

# limit
results = db.select('mytable', limit = 10)

# offset
results = db.select('mytable', offset = 10)
```

#### 插入
```python
db.insert('user', name = 'TY', age = 28, passwd = '123456', email = '526077432@qq.com')
# 插入利用了Python的**kw提供字段值，非常方便
```

#### 更新
```python
db.update('mytable', where = "id = 10", value1 = "foo")
db.update('user', where = 'id = $id', vars = {'id' : 100}, name = 'TY001', age = 29)
# update也充分利用了Python的**kw参数，只有传入的**kw才被update，其他字段保持不变。
# where和vars负责where语句的生成和绑定参数
```

#### 删除
```python
db.delete('mytable', where = "id = 10")
db.delete('user', where = 'id = $id', vars = {'id':100})
```

#### 复杂查询
```python
# count
results = db.query("SELECT COUNT(*) AS total_users FROM users")
print results[0].total_users

# join
results = db.query("SELECT * FROM entries JOIN users WHERE entries.author_id = users.id")

# 防止SQL注入
results = db.query("SELECT * FROM entries WHERE id = $id", vars = {'id':10})
```

#### 多数据库操作（web.py大于0.3）
```python
db1 = web.database(dbn = 'mysql', db = 'dbname1', user = 'foo')
db2 = web.database(dbn = 'mysql', db = 'dbname2', user = 'foo')

print db1.select('foo', where = 'id = 1')
print db2.select('bar', where = 'id = 5')
```

#### 事务
```python
t = db.transaction()
try:
    db.insert('person', name = 'foo')
    db.insert('person', name = 'bar')
except:
    t.rollback()
    raise
else:
    t.commit()

# Python 2.5+ 可以用with
from __future__ import with_statement
with db.transaction():
    db.insert('person', name = 'foo')
    db.insert('person', name = 'bar')
```

和Java比，web.py的db操作非常简单，这主要得益于python的**kw参数和内建的dict支持（对应Java的Map）。
