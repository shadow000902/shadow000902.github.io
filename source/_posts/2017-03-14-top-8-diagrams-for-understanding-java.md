---
title: Top 8 Diagrams for Understanding Java
date: '2017-03-14T17:10:45.000Z'
categories:
  - Java
tags:
  - java
---

# 2017-03-14-Top-8-Diagrams-for-Understanding-Java

## String Immutability【字符串不变性】

The following diagram shows what happens for the following code:

```java
String s = "abcd";
s = s.concat("ef");
```

## The equals\(\) and hashCode\(\) Contract【equals\(\)方法、hashCode\(\)方法的区别】

HashCode is designed to improve performance. The contract between equals\(\) and hasCode\(\) is that: 1. If two objects are equal, then they must have the same hash code. 2. If two objects have the same hashcode, they may or may not be equal.

## Java Exception Class Hierarchy【Java异常类的层次结构】

Red colored are checked exceptions which must either be caught or declared in the method’s throws clause.

## Collections Class Hierarchy【集合类的层次结构】

Note the difference between Collections and Collection.

## Java synchronization【Java同步】

Java synchronization mechanism can be illustrated by an analogy to a building.

## Aliasing【别名】

Aliasing means there are multiple aliases to a location that can be updated, and these aliases have different types.

## Stack and Heap【堆和栈】

This diagram shows where methods and objects are in run-time memory.

## JVM Run-Time Data Areas【Java虚拟机运行时数据区域】

_原文链接： programcreek 翻译： ImportNew.com - era\_misa_ _译文链接：_ [http://www.importnew.com/11725.html](http://www.importnew.com/11725.html)

