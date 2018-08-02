---
title: HTML基础学习笔记
date: 2018-08-02 22:46:02
categories: [HTML]
tags: [html]
---

#### 基础标签功能
  ``p``标签
```html
# 元素解释：网站上正常段落文本的首选元素。P是“paragraph”的缩写。
<p>我是一个p标签！</p>
```

  <!--more-->

  ``<!--  -->``注释
```html
# 元素解释：多行注释
<!--
    <h1>Hello World</h1>
    <p>Hello Paragraph</p>
-->
```

  颜色属性
```html
# 方式一：直接在标签内加样式
<h2 style="color: blue">CatPhotoApp</h2>
# 方式二：增加CSS样式
<style>
    # 对标签加样式，直接引用
    h2 {
        color: blue;
    }
</style>
<h2>CatPhotoApp</h2>
```

  应用类于HTML元素，对元素增加CSS样式
```html
<style>
    # 对元素的类加样式，需要在引用类的时候，加上``.``为前缀
    .sty-text {
        color: blue;
    }
</style>

<h2 class="sty-text">CatPhotoApp</h2>
```

  设置字体大小，字体类型
```html
# 方式一：直接在标签内加样式
<h2 style="font-size: 16px">CatPhotoApp</h2>
# 方式二：增加CSS样式
<style>
    # 对标签加样式，直接引用
    h2 {
        font-size: 16px;
        font-family: Monospace;
    }
</style>
<h2>CatPhotoApp</h2>

```