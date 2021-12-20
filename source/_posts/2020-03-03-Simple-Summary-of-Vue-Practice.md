---
title: Vue入门实践学习总结
date: 2020-03-03 14:17:26
categories: [Vue]
tags: [vue]
---

### 学习资料
[官网](https://cn.vuejs.org/)
[官方入门教程](https://cn.vuejs.org/v2/guide/)
VuePC端UI组件库：[Element](https://element.eleme.cn/)、[iView](https://www.iviewui.com/)、[vue-element-admin](https://panjiachen.github.io/vue-element
-admin-site/#/)、[更多](https://www.jianshu.com/p/669d3e41dca6)

  <!--more-->

### 列表增加筛选项
1. 列表头增加筛选项『下拉选择、输入框』
    在<template>......</template>中增加如下代码
    ```vue
    <el-form-item label="角色">
        <!--
        增加角色筛选
        筛选下拉项来源为：roleData，从接口获取赋值
        示例[{role_id: 1, role_name: "测试人员"}, {role_id: 2, role_name: "管理员"}]
        -->
        <el-select v-model="form.role_id"
                   placeholder="请选择角色"
                   clearable
                   filterable
                   @change="initUserChoice"
                   value-key="role_id"
                   style="padding-right:3px">
            <el-option
                    v-for="(item) in roleData"
                    :key="item.role_id"
                    :label="item.role_name"
                    :value="item.role_id">
            </el-option>
        </el-select>
    </el-form-item>
    <el-form-item label="状态">
        <!--
        增加状态筛选
        筛选下拉项来源为：userStatusList，筛选值为自己自定义的list
        示例：
            [
                {
                    'id': '0',
                    'name': '冻结'
                },
                {
                    'id': '1',
                    'name': '正常'
                }
            ]
        -->
        <el-select
                v-model="form.status"
                placeholder="请选择状态"
                clearable
                filterable
                @change="initUserChoice"
                value-key="status"
                style="padding-right: 3px"
        ><el-option
                v-for="item in userStatusList"
                :key="item.id"
                :label="item.name"
                :value="item.id">
        </el-option>
        </el-select>
    </el-form-item>
    ```

2. 筛选字段定义
    ①定义筛选字段所需的自定义下来列表项
    ②增加两个筛选的值的字段定义
    ```vue
    <script>
        export default {
            data() {
                return {
                    userStatusList: [
                        {
                            'id': '0',
                            'name': '冻结'
                        },
                        {
                            'id': '1',
                            'name': '正常'
                        }
                    ],
                    form: {
                        role_id: '',
                        status: ''
                    }
                }
            }
        }
    </script>
    ```

3. 筛选接口增加筛选字段的传参
    在请求接口中新增两个字段：role_id、status
    ```vue
    <script>
        export default {
            methods: {
                findUser() {
                    var roleItem = '';
                    this.$axios.post(this.$api.findUserApi, {
                        'role_id': this.form.role_id,
                        'status': this.form.status,
                    }).then((response) => {
                        }
                    )
                }
            }
        }
    </script>
    ```

### 文本换行
1. 通过 `css属性`实现

    示例1：
    ```vue
    <p style="white-space: pre-wrap;" v-text='item.des'></p>
    ```
    示例2：
    ```vue
    <el-row>
       <el-col>职位描述：</el-col>
       <el-col style="white-space: pre-wrap;">{{resumeDetails.postDescribe}}</el-col>
    </el-row>
    ```
    `white-space`的各属性详情可以阅读[这里](https://www.w3school.com.cn/cssref/pr_text_white-space.asp)

2. 通过`v-html`实现
    
    需要先把字符串里的`\n`替换为`<br>`，然后用`v-html`指令渲染字符串为`innerHTML`。
    ```vue
    // JS部分
    this.text = res.data.replace(/\n/g, '<br>')
    
    // HTML部分
    <div v-html="text"></div>
    ```