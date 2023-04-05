---
title: EXCEL使用小技巧
date: 2022-04-27 17:10:21
categories: [Excel]
tags: [excel]
---

### 单元格内容拆分，并获取其中某一部分

`LEFT(G2,FIND(",",G2)-1)`

`IF(ISERROR(LEFT(G2,FIND(",",G2)-1)),G2,LEFT(G2,FIND(",",G2)-1))`

FIND
LEFT

### 从表格查询内容单元格，并返回其右侧的单元格内容

VLOOKUP
