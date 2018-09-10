---
title: SQL基础知识整理
date: 2018-08-12 00:58:52
categories: [MYSQL]
tags: [mysql]
---

#### 基础命令

登录
```bash
[root@host]# mysql -u root -p
Enter password:******
```

<!--more-->

创建数据库
```sql
create W3CSCHOOL;
```

删除数据库
```sql
drop W3CSCHOOL;
```

选择数据库
```sql
use W3CSCHOOL;
```

创建数据表
```sql
CREATE TABLE w3cschool_tbl(
    w3cschool_id INT NOT NULL AUTO_INCREMENT,
    w3cschool_title VARCHAR(100) NOT NULL,
    w3cschool_author VARCHAR(40) NOT NULL,
    submission_date DATE,
    PRIMARY KEY ( w3cschool_id )
    );
```

删除数据表
```sql
DROP TABLE table_name ;
```

插入数据
```sql
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```

查询数据
```sql
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[OFFSET M ][LIMIT N]
```
通过``OFFSET``指定``SELECT``语句开始查询的数据偏移量。默认情况下偏移量为0。
``LIMIT``属性来设定返回的记录数。

where子句
```sql
SELECT field1, field2,...fieldN FROM table_name1, table_name2...
[WHERE condition1 [AND [OR]] condition2.....
```
WHERE子句也可以运用于SQL的 DELETE 或者 UPDATE 命令。
WHERE 子句类似于程序语言中的if条件，根据 MySQL 表中的字段值来读取指定的数据。

UPDATE查询
```sql
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

DELETE子句
```sql
DELETE FROM table_name [WHERE Clause]
```

LIKE子句





MySQL命令终止符为分号``;``

