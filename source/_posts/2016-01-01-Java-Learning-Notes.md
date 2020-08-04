---
title: Java学习笔记
date: 2020-07-23 15:51:04
categories: [学习笔记, Java]
tags: [java]
---

##### 泛型`<T extends Animal<T>>`的简单使用
```java
class Animal<T extends Animal<T>> {
    public T run() {
        System.out.println("奔跑");
        return (T)this;
    }
}
```

  <!--more-->

```java
class Cat extends Animal<Cat> {
    public Cat eat() {
        System.out.println("吃东西");
        return this;
    }
    public Cat sleep() {
        System.out.println("准备睡觉");
        return this;
    }
}

public static void main(String[] args){
    Cat cat = new Cat();
    // 链式调用
    cat.eat().run().sleep();
}
```

##### `For-Each`循环
语法格式如下：
```
for(type element: array)
    {
        System.out.println(element);
    }
```
实例：
```java
public class TestArray {
   public static void main(String[] args) {
      double[] myList = {1.9, 2.9, 3.4, 3.5};
 
      // 打印所有数组元素
      for (double element: myList) {
         System.out.println(element);
      }
   }
}
```

##### 配置文件的使用
```java
public class BaseConfig {
    public static String testEnv() {
        String testEnv = null;
        testEnv = System.getProperty("testEnv");
        if (null == testEnv) {
            testEnv = BT.GetProv("/config/application.properties", "testEnv");
            System.setProperty("testEnv", testEnv);
        }
        return testEnv.trim();
    }
}
```
 - 默认从`mvn`命令执行时，通过`-DtestEnv=test`传入的变量，来读取`testEnv`字段的配置
 - 如果传入的配置为空，就从配置文件中读取默认设置的值，并设置到系统配置中