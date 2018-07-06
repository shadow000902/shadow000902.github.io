# -*- coding: utf-8 -*-
"""
    @Date: 2018-07-02 01:09:44
    @Author: shadow
    @Theme: 时间处理和定时任务
"""

# 计算明天和昨天的日期
import datetime

today = datetime.date.today()
# 计算昨天的日期
yesterday = today - datetime.timedelta(days=1)
# 计算明天的日期
tomorrow = today + datetime.timedelta(days=1)

print yesterday, today, tomorrow