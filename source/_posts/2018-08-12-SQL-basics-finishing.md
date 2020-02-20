---
title: SQL基础知识整理
date: 2018-08-12 00:58:52
categories: [MySQL]
tags: [mysql]
---

### 数据库表操作
1. 登录
    ```bash
    [root@host]# mysql -u root -p
    Enter password:******
    ```

  <!--more-->

2. 创建数据库
    ```sql
    create W3CSCHOOL;
    ```

3. 删除数据库
    ```sql
    drop W3CSCHOOL;
    ```

4. 选择数据库
    ```sql
    use W3CSCHOOL;
    ```

5. 创建数据表
    ```sql
    CREATE TABLE w3cschool_tbl(
        w3cschool_id INT NOT NULL AUTO_INCREMENT,
        w3cschool_title VARCHAR(100) NOT NULL,
        w3cschool_author VARCHAR(40) NOT NULL,
        submission_date DATE,
        PRIMARY KEY ( w3cschool_id )
        );
    ```

6. 删除数据表
    ```sql
    DROP TABLE table_name ;
    ```

7. 用户管理
    7.1 新建用户
    ```sql
    CREATE USER 'username'@'host' IDENTIFIED BY 'password';
    ```
    7.2 授权
    ```sql
    GRANT privileges ON databasename.tablename TO 'username'@'host'
    ```
    - privileges：用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL
    - databasename：数据库名
    - tablename：表名，如果要授予该用户对所有数据库和表的相应操作权限则可用`*`表示，如`*.*`
    7.3 设置与更改用户密码
    ```sql
    SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
    ```
    如果是当前用户：
    ```sql
    SET PASSWORD = PASSWORD("newpassword");
    ```
    7.4 撤销用户权限
    ```sql
    REVOKE privilege ON databasename.tablename FROM 'username'@'host';
    ```
    7.5 删除用户
    ```sql
    DROP USER 'username'@'host';
    ```

### 增删改
1. 插入数据
    ```sql
    INSERT INTO table_name ( field1, field2,...fieldN )
                           VALUES
                           ( value1, value2,...valueN );
    ```

2. UPDATE查询
    ```sql
    UPDATE table_name SET field1=new-value1, field2=new-value2
    [WHERE Clause]
    ```

3. DELETE子句
    ```sql
    DELETE FROM table_name [WHERE Clause]
    ```

### 查
1. 查询数据
    1.1 基础查询语句
    ```sql
    SELECT column_name,column_name
    FROM table_name
    [WHERE Clause]
    [OFFSET M ][LIMIT N]
    ```
    通过``OFFSET``指定``SELECT``语句开始查询的数据偏移量。默认情况下偏移量为0。
    ``LIMIT``属性来设定返回的记录数。
    
    1.2 where子句
    ```sql
    SELECT field1, field2,...fieldN FROM table_name1, table_name2...
    [WHERE condition1 [AND [OR]] condition2.....
    ```
    WHERE子句也可以运用于SQL的 DELETE 或者 UPDATE 命令。
    WHERE 子句类似于程序语言中的if条件，根据 MySQL 表中的字段值来读取指定的数据。

2. LIKE子句
    从技术上说，`LIKE`是谓词（predicate），而不是操作符。
    使用`LIKE`子句，就必然会用到通配符。
    通配符搜索只能用于文本字段（字符串），非文本数据类型字段不能使用通配符搜索。
    2.1 百分号`%`通配符
    `%`表示任意字符出现任意多次。
    ```sql
    WHERE prod_name LIKE 'Fish%'
    ```
    ```sql
    WHERE prod_name LIKE '%bean bag%'
    ```
    ```sql
    WHERE prod_name LIKE 'F%y'
    ```
    `%`还能匹配0个字符。`%`代表搜索模式中给定位置的0个、1个或多个字符。
    `%`不匹配`NULL`
    2.2 下划线`_`通配符
    `_`匹配单个字符
    2.3 方括号`[]`通配符
    `[]`用来指定一个字符集。它必须匹配指定位置（通配符的位置）的一个字符，且该字符必须是指定字符集中存在的字符。
    ```sql
    WHERE cust_contact LIKE '[JM]%'
    ```
    `[JM]`匹配方括号中任意一个字符，它也只能匹配单个字符。
    ```sql
    WHERE cust_contact LIKE '[^JM]%'
    ```
    `[^JM]`匹配除方括号内的任意一个字符。它的另一种表达方式：
    ```sql
    WHERE NOT cust_contact LIKE '[JM]%'
    ```
    使用通配符搜索，一般会耗费更多的处理时间；把通配符置于开始处，搜索起来是最慢的。

3. 创建计算字段
    创建计算字段，并定义列名
    ```sql
    select Concat(vend_name, ' (', vend_country, ')') AS vend_title
    ```
    计算字段也可用于算数计算
    ```sql
    select quantity, quantity*item_price AS expended_price
    ```
    
### 使用函数处理数据
    函数的类型：
        - 用于处理文本字符串
        - 用于在数值数据上进行算术操作
        - 用于处理日期和时间值并从这些值中提取特定成分
        - 返回 DBMS 正使用的特殊信息
1. 文本处理函数

    |函数|说明|
    |---|---|
    |`LEFT()`(或使用子字符串函数)|返回字符串左边的字符|
    |`LENGTH()`(也使用`DATALENGTH()`或`LEN()`)|返回字符串的长度|
    |`LOWER()`|将字符串转化为小写|
    |`LTRIM()`|去掉字符串左边的空格|
    |`RIGHT()`或使用子字符串函数|返回字符串右边的字符|
    |`RTRIM()`|去掉字符串右边的空格|
    |`SOUNDEX()`|返回字符串的`SOUNDEX`值，对字符串进行发音比较，而不是字母比较|
    |`UPPER()`|将字符串转化为大写|

2. 聚集函数

    |函数|说明|
    |---|---|
    |`AVG()`|返回某列的平均值|
    |`COUNT()`|返回某列的行数，`COUNT(*)`计数值包含空值(`NULL`)，`COUNT(column)`对特定列计数，忽略空值(`NULL`)|
    |`MAX()`|返回某列的最大值|
    |`MIN()`|返回某列的最小值|
    |`SUM()`|返回某列值之和|

3. 分组数据
    涉及到两个新的 `SELECT` 语句子句：`GROUP BY` 子句和 `HAVING` 子句。
    
