# -*- coding: utf-8 -*-

def story(**kwds):
    return 'Once upon a time. there was a ' \
           ' %(job)s called %(name)s.' % kwds

def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x,y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:                # 如果没有为stop提供值……
        start, stop = 0, start      # 指定参数
    result = []
    i = start                       # 计算start索引
    while i < stop:                 # 直到计算到stop的索引
        result.append(i)            # 将索引添加到result内……
        i += step                   # 用step (>0) 增加索引i……
    return result