# -*- coding: utf-8 -*- 
"""
    @Date: 2018-07-02 01:06:24
    @Author: shadow
    @Theme: 判断python字典中key是否存在
"""

# 方法一：使用自带函数实现
# 生成一个字典
d = {'name':{},'age':{},'sex':{}}
# 打印返回值
print d.has_key('name')
# 结果返回True


# 方法二：使用in方法
# 生成一个字典
d = {'name':{},'age':{},'sex':{}}
# 打印返回值，其中d.keys()是列出字典中所有的key
print &lsquo;name&lsquo; in d.keys()
# 结果返回True

#推荐使用第二种方法，因为``has_key()``是``python2.2``之前的方法，而且使用``in``的方法会更快一些。