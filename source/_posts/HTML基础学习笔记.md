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

  添加图片
```html
# img 元素是自关闭元素，不需要结束标签。
<img src="https://www.your-image-source.com/your-image.jpg">
<img src="/statics/codecamp/images/relaxing-cat.jpg" alt = "your-image">
# alt 属性中的文本用于屏幕阅读器以提高可访问性，并且如果图像无法加载，则会显示。
```

  给图片添加格式
```html
<stype>
    .smaller-image {
        width: 100px;
    }
    .thick-green-border {
        <!-- 设置边框的宽度 -->
        border-width: 10px;
        <!-- 设置边框的类型 -->
        border-style: solid;
        <!-- 设置边框的颜色 -->
        border-color: green;
        <!-- 设置边框的圆角度数 -->
        border-radius: 10px;
        <!-- 设置一个圆形边框 -->
        border-radius: 50%;
    }
</style>
<img class="smaller-image thick-green-border" src="/statics/codecamp/images/relaxing-cat.jpg" alt = "your-image">
```

  锚点元素``a``
```html
<!-- 可以放在段落中间 -->
<p>这是一个a标签 <a href="https://www.w3cschool.cn">W3Cschool.cn</a>跳转到W3Cschool.cn</p>
<!-- 也可以独立使用 -->
<a href="https://www.w3cschool.cn">W3Cschool.cn</a>
```

  固定链接使用``#``
有时你想要在你的网站上添加一个 a 元素，但你还不知道将它链接到哪里，这时你可以使用固定连接。
```html
<a href="#">cat photos</a>
```

  为图片设置超链接
```html
<!-- 通过将某元素嵌套在a元素中使其变为一个链接。 -->
<a href="#"><img class="smaller-image thick-green-border" src="/statics/codecamp/images/relaxing-cat.jpg"></a>
```

  为图片添加``alt``描述
``alt``属性，是当图片无法显示时的替代文本。``alt``属性对于盲人或视觉障碍的用户理解图片中的内容非常重要，搜索引擎也会搜索``alt``属性来了解图片的内容。``alt``属性是一个必需的属性，为页面上的图片都加上``alt``属性是好习惯。
```html
<img src="www.your-image-source.com/your-image.jpg" alt="your alt text">
```