---
title: Mac上MySQL的简单使用
date: 2017-06-03 17:20:13
categories: [Database]
tags: [mysql]
---

1. 启动、停止、重启MySQL服务
	```bash
	sudo /usr/local/MySQL/support-files/mysql.server start
	sudo /usr/local/mysql/support-files/mysql.server stop
	sudo /usr/local/mysql/support-files/mysql.server restart
	```

  <!--more-->

2. 登录MySQL数据库
	```bash
	mysql -h 地址 -P 端口 -u 用户名 -p 密码
	```

3. 查看数据库
	```mysql
	show databases;
	```

4. 查看当前库的所有表
	```mysql
	show tables;
	```

5. 字符匹配查询
	```mysql
	# 查询 Attributes 中包含 SQL 字符的数据
	select * from database where Attributes like "%SQL%";
	# 查询 Attributes 中以 a 开头以 b 结尾的字符串数据
	select * from database where Attributes like "a%b";
	# 查询 Attributes 中以 m 开头以 n 结尾的3个字符的数据，中间 _ 只能代表一个字符
	select * from database where Attributes like "m_n";
	# 查询出指定字段
	select name,id,age from database [where 条件];
	```

6. 多条件查询
	```mysql
	select * from database where Attributes1=a and Attributes2 like "My_SQL";
	select * from database where Attributes1=a or Attributes2 like "My_SQL";
	```

7. 查询不重复的记录
	```mysql
	# 查询name不一样的数据
	select distinct name from database;
	# 查询name和age都不一样的数据
	select distinct name,age from database;
	```
	1.distinct必须放在最开头
    2.distinct只能使用需要去重的字段进行操作。  ----也就是说我distinct了name,age两个字段，我后面想根据id进行排序，是不可以的，因为只能name,age两个字段进行操作.
    3.distinct去重多个字段时，含义是：几个字段`同时重复`时才会被`过滤`。

8. 对查询结果进行排序
	```mysql
	# 倒叙（降序）排列
	select * from database orderby id desc;
	# 正序（升序）排列
	select * from database orderby id asc;
	```

9. 分组查询
	```mysql
	select name,id from database GROUP BY id;
	# 当id字段的值相等时，再按照name字段分组
	select name,id from database GROUP BY name,id;
	```

10. 限制查询结果的数量
	```mysql
	# **前面的数字表示从第n+1条开始取，后面的食指表示取m条数据**
	# 取两条数据，正序，从第三条开始
	select * from database orderby id asc limit 2,3;
	# 取两条数据，倒序，从倒数第三条结束，只显示倒数前两条
	select * from database orderby id desc limit 2,3;
	```

11. 聚合
	```mysql
	select 字段 fun_name from 表名 [where 条件] [group by field1,field2...] [with rollup] [having 条件];
	```
	1.fun_name 表示要做的聚合操作，也就是说聚合函数，常用的有 : sum(求和)、count(*)(记录数)、max(最大值)、min(最小值)。
	2.group by关键字 表示要进行分类聚合的字段。比如要按照部门分类统计员工数量，部门就应该写在group by 后面。
	3.with rollup 是可选语法，表明是否对分类聚合后的结果进行再汇总
	4.having 关键字表示对分类后的结果再进行条件过滤。
	
	```mysql
	# 库表使用Horgarts课程的示例库的salaries表
	# 统计总行数
	select count(1) from salaries;
	# 统计每个员工下发了多少个月的工资
	select emp_no,count(1) from salaries group by emp_no;
	# 既要统计每个员工发了几个月工资，也要统计总共发了多少个月工资
	select emp_no,count(1) from salaries group by emp_no with rollup;
	# 统计发工资月数超过17的员工和具体发工资的月数
	select emp_no,count(1) from salaries group by emp_no having count(1) > 17;
	# 统计总工资和最小最大工资
	select sum(salary),max(salary),min(salary) from salaries;
	```

12. 表连接
	示例数据：
	员工表staff

	| id  | name |
	| --- | --- |
	|1|Steve|
	|2|Jobs|
	|3|Drake|
	|4|Tom|
	|5|Jay|
	|6|Li|
	|7|Chuan|
	|8|Anna|
	|9|Satan|
	
	职位表deptno

	| name  | deptname |
	| --- | --- |
	|Steve|tech|
	|Jobs|seal|
	|Drake|tech|
	|Tom|seal|
	|Jay|tech|
	|Li|hr|
	|Chuan|ceo|
	|Anna|seal|
	|Satan|driver|

	表连接分为内连接和外连接。
	他们之间最主要的区别：内连接仅选出两张表中互相匹配的记录，外连接会选出其他不匹配的记录。

	```mysql
	select staff.name,deptname from staff,deptno where staff.name=deptno.name;
	```

	*外连接*分为左连接和右连接
	**左连接**：包含所有左边表中的记录，甚至是右边表中没有和他匹配的记录。
	**右连接**：包含所有右边表中的记录，甚至是右边表中没有和他匹配的记录。

	```mysql
	select staff.name,deptname from staff left join deptno on staff.name=deptno.name;
	```
	```mysql
	select deptname,deptno.name from staff right join deptno on deptno.name=staff.name;
	```