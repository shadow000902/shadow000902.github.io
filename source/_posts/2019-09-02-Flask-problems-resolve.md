---
title: Flask使用小结【更新ING】
date: 2019-09-02 19:21:29
categories: [Flask]
tags: [flask]
---

#### `Can't locate revision identified by '3ba21fe709f1'` 问题处理
```bash
# taoyi @ TyMac in ~ [16:26:14] 
$ flask db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [root] Error: Can't locate revision identified by '3ba21fe709f1'
```

  <!--more-->

1. 查询对应表中的数据
```
mysql> SELECT * FROM alembic_version;
+-------------+
| version_num |
+-------------+
| 3ba21fe709f1 |
+-------------+
1 row in set (0.00 sec)
```
2. 删除版本控制的数据表
```mysql
DROP TABLE alembic_version;
```
3. 然后删除之前的`migrations`文件夹，重新生成迁移版本文件夹
```bash
flask db init
```
4. 然后重新生成迁移版本文件
```bash
flask db migrate
```

#### `query.filter`常见操作符
1. equals
```python
query.filter(User.name == 'ed')
```
2. not equals
```python
query.filter(User.name != 'ed')
```
3. LIKE
```python
query.filter(User.name.like('%ed%'))
```
4. IN
```python
query.filter(User.name.in_(['ed', 'wendy', 'jack']))

# works with query objects too:
query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))
```
5. NOT IN
```python
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
```
6. IS NULL
```python
query.filter(User.name == None)
 
# alternatively, if pep8/linters are a concern
query.filter(User.name.is_(None))
```
7. IS NOT NULL
```python
query.filter(User.name != None)
 
# alternatively, if pep8/linters are a concern
query.filter(User.name.isnot(None))
```
8. AND
```python
# use and_()
from sqlalchemy import and_
query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
# or send multiple expressions to .filter()
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')
# or chain multiple filter()/filter_by() calls
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')
```
9. OR
```python
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))
```
10. MATCH
```python
query.filter(User.name.match('wendy'))
```
