---
title: Flask使用小结【更新ING】
date: '2019-09-02T19:21:29.000Z'
categories:
  - Flask
tags:
  - flask
---

# 2019-09-02-Flask-problems-resolve

## `Can't locate revision identified by '3ba21fe709f1'` 问题处理

```bash
# taoyi @ TyMac in ~ [16:26:14] 
$ flask db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [root] Error: Can't locate revision identified by '3ba21fe709f1'
```

1. 查询对应表中的数据

   ```text
    mysql> SELECT * FROM alembic_version;
    +-------------+
    | version_num |
    +-------------+
    | 3ba21fe709f1 |
    +-------------+
    1 row in set (0.00 sec)
   ```

2. 删除版本控制的数据表

   ```text
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

## `query.filter`常见操作符

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

## 多条件筛选接口

```python
@api.route('/gitCommit/find', methods=['GET', 'POST'])
@login_required
@cost_count
def gitcommit_find():
    data = request.json
    projectName = data.get('project_name')
    branchName = data.get('branch_name')
    commitMessage = data.get('title')

    period = data.get('period')

    time_start = period[0] if period else None
    time_end = period[1] if period else None
    page = data.get('page') if data.get('page') else 1
    per_page = data.get('sizePage') if data.get('sizePage') else 20

    '''
    筛选的时候会遇到多个筛选条件，但都是非必填的
    把存在的筛选条件添加到数组中，然后进行解包
    最后把解包后的数据添加到筛选条件中
    '''

    filterList = []

    if projectName is not None:
        filterList.append(GitCommits.project_name)
    if branchName is not None:
        filterList.append(GitCommits.branch_name)
    if commitMessage is not None:
        filterList.append(GitCommits.title.like('%' + commitMessage + '%'))
    if time_start is not None:
        filterList.append(time_start < GitCommits.create_at < time_end)

    _data = GitCommits.query.filter(*filterList)

    pagination = _data.order_by(GitCommits.create_at.desc()).paginate(page, per_page=per_page, error_out=False)
    _data = pagination.items
    total = pagination.total

    end_data = [{'id':c.id,
                 'project_id': c.project_id,
                 'project_name': c.project_name,
                 'branch_name': c.branch_name,
                 'commit_message': c.title,
                 'author_name': c.author_name,
                 'create_at': c.create_at} for c in _data]

    print(end_data)
    return jsonify({'data': end_data, 'total': total, 'status': 1})
```

