---
title: TestNG使用简单总结
date: 2020-04-19 18:03:46
categories: [TestNG]
tags: [testng, java]
---

### `TestNG`介绍

`TestNG`是一个开源自动化测试框架；`TestNG`表示**下一代**(**N**ext **G**eneration的首字母)。

  <!--more-->

TestNG的特点：

 - 注解
 - 使用Java和面向对象的功能
 - 灵活的运行时配置
 - 支持依赖测试方法，并行测试，负载测试，局部故障
 - 灵活的插件API
 - 支持多线程测试

### `TestNG`测试类配置注释说明

 注解                 | 描述
--------------------|----
 `@BeforeMethod`    | 在每个测试方法 前 执行
 `@AfterMethod`     | 在每个测试方法 后 执行
 `@BeforeClass`     | 被注释的方法将在当前类的第一个测试方法调用前运行
 `@AfterClass`      | 被注释的方法将在当前类的所有测试方法调用后运行
 `@BeforeGroups`    | 被配置的方法将在列表中的gourp前运行。这个方法保证在第一个属于这些组的测试方法调用前立即执行
 `@BeforeTest`      | 被注释的方法将在测试运行前运行
 `@AfterTest`       | 被注释的方法将在测试运行后运行
 `@BeforeSuite`     | 被注释的方法将在所有测试运行前运行
 `@AfterSuite`      | 被注释的方法将在所有测试运行后运行
 `alwaysRun`        | 对于每个bufore方法(beforeSuite, beforeTest, beforeTestClass 和 beforeTestMethod, 但是不包括 beforeGroups):\n如果设置为true，被配置的方法将总是运行而不管它属于哪个组。\n对于after方法(afterSuite, afterClass, ...): 如果设置为true，被配置的方法甚至在一个或多个先调用的方法失败或被忽略时也将运行。
 `dependsOnGroups`  | 这个方法依赖的组列表
 `dependsOnMethods` | 这个方法依赖的方法列表
 `enabled`          | 这个类的方法是否激活
 `groups`           | 这个类或方法所属的分组列表
 `inheritGroups`    | 如果设置为true，这个方法被属于在类级别被@Test annotation指定的组

### `testng.xml` 配置详解

#### `XML`规则

 - suite
 - --tests
 - ----parameters
 - ----groups
 - ------definitions
 - ------runs
 - ----classes
 - --parameters

#### `XML`简单的大概结构

```xml
<suite name="xxx">
    <test name="xxxx">
    　　<!-- 参数定义的方法 -->
    　　<parameter name="first-name" value="Cedric"/>
    
    　　<!-- groups的用法，前提是需要存在classes的组，否则所有方法不被运行 -->
    　　<groups>
    　　<!-- 定义组中组的方法 -->
    　　　　<define name="groups_name">
    　　　　　　<include name="group1"/>
    　　　　　　<include name="group2"/>
    　　　　</define>
    
    　　　　<run>
    　　　　　　<!-- 此处用组名来区别 -->
    　　　　　　<inclue name="groups_name" />
    　　　　　　<exclue name="groups_name" />
    　　　　　　</run>
    　　</groups>
    
    　　<!-- classes的用法，classes中包含类名，类名底下可以包含方法名或排除方法名 -->
    　　<classes>
    　　　　<class name="class1">
    　　　　　　<methods>
    　　　　　　　　<!-- 此处用方法名来区别 -->
    　　　　　　　　<inclue name="method_name" />
    　　　　　　　　<exclue name="method_name" />
    　　　　　　</methods>
    　　　　</class>
    　　</classes>
    </test>
</suite>
```

#### 各个参数说明

1. `<suite>`
    说明：一个`xml`文件只能有一个`<suite>`，是一个`xml`文件的根级
    `<suite>`由`<test>`和`<parameters>`组成

    参数说明：

    参数                           |说明|使用方法|参数值
------------------------------|---|---|---
    `name`                       |必选项，<suite>的名字，将出现在reports里|name="XXX"|suite名字
    `junit`                      |是否执行Junit模式(识别setup()等)|junit="true"|true和false，默认false
    `verbose`                    |控制台输出的详细内容等级,0-10级（0无，10最详细）|verbose="5"|0到10
    `parallel`                   |是否在不同的线程并行进行测试，要与thread-count配套使用|parallel="mehods"|详见表格下内容，默认false
    `parent-module`              |和Guice框架有关，只运行一次，创建一个parent injector给所有guice injectors|
    `guice-stage`                |和Guice框架有关|guice-stage="DEVELOPMENT"|DEVELOPMENT，PRODUCTION，TOOL，默认"DEVELOPMENT"
    `configfailurepolicy`        |测试失败后是再次执行还是跳过，值skip和continue|configfailurepolicy="skip"|skip、continue，默认skip
    `thread-count`               |与parallel配套使用，线程池的大小，决定并行线程数量|thread-count="10"|整数，默认5
    `annotations`                |获取注解，值为javadoc时，使用JavaDoc的注释；否则用JDK5注释|annotations="javadoc"|javadoc
    `time-out`                   |设置parallel时，终止执行单元之前的等待时间（毫秒）|time-out="10000"|整数，单位毫秒
    `skipfailedinvocationcounts` |是否跳过失败的调用|skipfailedinvocationcounts="true"|true和false，默认false
    `data-provider-thread-count` |并发时data-provider的线程池数量|data-provider-thread-count="5"|整数
    `object-factory`             |一个实现IObjectFactory接口的类，实例化测试对象|object-factory="classname"|类名
    `allow-return-values`        |是否允许返回函数值|all-return-values="true"|true和false
    `preserve-order`             |是否按照排序执行|preserve-order="true"|true和false，默认true
    `group-by-instances`         |按照实例分组|group-by-instances="true"|true和false，默认false

2. `<test>`
    说明：一个<suite>下可以有多个<test>，可以通过<suite>的parallel="tests"来进行并行测试，必须和thread-count配套使用，否则是无效参数
    `<test>`由`<parameters>`、`<groups>`、`<classes>`三部分组成

    参数说明：

    参数                           |说明|使用方法|参数值
------------------------------|---|---|---
    `name`                       |test的名字，将出现在报告里|name="testname"|test的名字
    `junit`                      |是否按照Junit模式运行|junit="true"|true和false，默认false
    `verbose`                    |控制台输出的详细内容等级,0-10级（0无，10最详细），不在报告显示|verbose="5"|0到10
    `parallel`                   |是否在不同的线程并行进行测试，要与thread-count配套使用|parallel="mehods"|与suite的parallel一致，默认false
    `thread-count`               |与parallel配套使用，线程池的大小，决定并行线程数量|thread-count="10"|整数，默认5
    `annotations`                |获取注解，值为javadoc时，使用JavaDoc的注释；否则用JDK5注释|annotations="javadoc"|javadoc
    `time-out`                   |设置parallel时，终止执行单元之前的等待时间（毫秒）|time-out="10000"|整数，单位毫秒
    `enabled`                    |标记是否执行这个test|enabled="true"|true和false，默认true
    `skipfailedinvocationcounts` |是否跳过失败的调用|skipfailedinvocationcounts="true"|true和false，默认false
    `preserve-order`             |是否按照排序执行，如果是true，将按照xml文件中的顺序去执行|preserve-order="true"|true和false，默认true
    `allow-return-values`        |是否允许返回函数值|all-return-values="true"|true和false，默认false

3. `parallel`
    该参数的值可以是`false`、`methods`、`tests`、`classes`、`instances`。默认`false`
    `parallel`必须和`thread-count`配套使用，否则相当于无效参数，`thread-count`决定了并行测试时开启的线程数量

     - `parallel="mehods"`  TestNG将并行执行所有的测试方法在不同的线程里
     - `parallel="tests"`  TestNG将并行执行在同一个<test>下的所有方法在不同线程里
     - `parallel="classes"`  TestNG将并行执行在相同<class>下的方法在不同线程里
     - `parallel="instances"`  TestNG将并行执行相同实例下的所有方法在不同的线程里

4. `<parameter>`
    说明：提供测试数据，有`name`和`value`两个参数
    声明方法：`<parameter name = "parameter_name" value = "parameter_value "/>`
    `testng.xml`文件中的`<parameter>`可以声明在`<suite>`或者`<test>`级别，在`<test>`下的`<parameter>`会覆盖在`<suite>`下声明的同名变量
    使用示例：

    ```java
    public class TestParameterXML {

        @Test
        @Parameters({ "parameter_name1", "parameter_name2" })
        public void createConnection(String parameter_name1, int parameter_name2) {
    
            System.out.println("parameter_name1 : " + dbconfig);
            System.out.println("parameter_name2 : " + poolsize);
    
            Properties prop = new Properties();
            InputStream input = null;
        }
    }
    ```

5. `<DataProvider>`

    使用示例：

    ```java
    package com.yiibai;
    
    import org.testng.Assert;
    import org.testng.annotations.DataProvider;
    import org.testng.annotations.Test;
    
    public class TestParameterDataProvider {
    
        @Test(dataProvider = "provideNumbers")
        public void test(int number, int expected) {
            Assert.assertEquals(number + 10, expected);
        }
    
        @DataProvider(name = "provideNumbers")
        public Object[][] provideData() {
    
            return new Object[][] { { 10, 20 }, { 100, 110 }, { 200, 210 } };
        }   
    }
    ```

6. `<groups>`
    说明：要运行的组，可以自定义一个组，可以包括要执行的，还排除要执行的方法。必须和`<classes>`配套使用，从下面的类中找到对应名字的方法
    `<groups>`由`<difine>`和`<run>`、`<dependencies>`三部分组成。`<diffine>`可以将`group`组成一个新组，包括要执行和不执行的大组；`<run>`要执行的方法；`<dependencies>`指定了某`group`需要依赖的`group`（比如下面的例子，`group1`需要依赖`group2`和`group3`先执行）。

    声明方法：

    ```xml
    <groups>
         <define name ="all">
              <include name ="testgroup1"/>
              <exclude name ="testgroup2'/>
         </define>
         <run>
              <include name ="all"/>
              <include name ="testmethod1"/>
              <exclude name="testmethod2"/>
         </run>
         <dependencies>
              <group name ="group1" depends-on="goup2 group3"/>
         </dependencies>
    </groups>
    ```

7. `<classes>`
    说明：方法选择器，要执行的方法写在这里，参数有`name`和`priority`。
    注释：
    1.<classes>下必须写要执行的<class>，否则不会执行任何内容，如果填写了class没有写methods，会按照填写的class的下的注释@Test去执行所有的方法
    2.<classes>下的<methods>如果填写了<include>，那只会执行所填写的方法，没有填写的方法不会去执行

    声明方法：

    ```xml
    <classes>
         <class name="要执行的class名">
              <methods>
                   <include name ="要执行的方法名"/>
              </methods>
         </class> 
    </classes>
    ```

8. `<packages>`
    说明：`<packages>`指定包名代替类名。查找包下的所有包含`testNG annotation`的类进行测试

    声明方法：

    ```xml
    <packages>
         <package name="packagename"/>
         <package name="packagename">
              <include name="methodname"/>
              <exclude name="methodname"/>
         </package>
    </packages>
    ```

9. `<listener>`
    说明：指定`listeners`，这个`class`必须继承自`org.testng.ITestNGListener`。在`java`中使用`@Listeners({com.example.MyListener.class,com.example.MyMethodInterceptor.class})`的注释也可以有同样效果

    声明方法：

    ```xml
    <listeners>
         <listener class-name="com.example.MyListener"/>
         <listener class-name="com.example.MyMehodIntercepor"/>
    </listeners>
    ```

### 忽略测试

在测试用例写好，但是并没有调试或者说还没有测试通过时，希望先不要执行该测试，可以使用`@Test(enabled = false)`来忽略这个测试方法。默认情况下，`enabled`参数是`true`。

### 超时测试

`超时`表示如果单元测试花费的时间超过指定的毫秒数，那么`TestNG`将会终止它，并标记为失败。
`超时`也可用于性能测试，以确保方法在合理的时间内返回。
示例代码如下：

```java
package com.yiibai;
import org.testng.annotations.Test;
public class TestTimeout {

    @Test(timeOut = 5000) // time in mulliseconds
    public void testThisShouldPass() throws InterruptedException {
        Thread.sleep(4000);
    }

    @Test(timeOut = 1000)
    public void testThisShouldFail() {
        while (true){
            // do nothing
        }
    }
}
```

### 设置失败用例重跑

对于`TestNG`，首先重写接口`IRetryAnalyzer`，重写该接口中的`retry`方法，自定义需要重试的次数`maxRetryCount`，如果一个用例失败，自动进入`retry`方法，在此方法中判断已经重试的次数是否小于`maxRetryCount`，如果是，则返回`true`，则自动再次执行失败的用例，如果是失败的用例再次执行还是失败，那么还是自动调用`retry`方法，直到到重试次数大于设定的`maxRetryCount`了，则返回`false`，那么系统就是判定该方法失败了。
失败用例重跑方法代码：

```java
package com.shadow.qa.common.listeners;

import com.shadow.qa.common.tools.BT;
import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;
import org.testng.Reporter;
import org.testng.log4testng.Logger;

public class TestNGRetryAnalyzer implements IRetryAnalyzer {

    public static Logger logger = Logger.getLogger(TestNGRetryAnalyzer.class);

    private int retryCount = 0;
    private static final int maxRetryCount = Integer.parseInt(BT.GetProv("/config/application.properties", "maxRetryCount"));

    public boolean retry(ITestResult iTestResult) {
        if (retryCount < maxRetryCount) {
            String message = "方法<" + iTestResult.getName() + ">执行失败，重试第" + retryCount + "次";
            logger.info(message);
            Reporter.setCurrentTestResult(iTestResult);
            Reporter.log(message);
            retryCount++;
            BT.sleep(3000);
            return true;
        }
        return false;
    }
}
```

重写了`TestNG`的`IRetryAnalyzer`接口，那么就需要让系统调用我们重写的接口，需要让`TestNG`调用，还需要对`TestNG.xml`中的注解接口进行重写。先判断`TestNG.xml`中是否有重试分析器，如果没有，则调用我们自己重写类。
失败重跑监听器代码：

```java
package com.shadow.qa.common.listeners;

import org.testng.IAnnotationTransformer;
import org.testng.IRetryAnalyzer;
import org.testng.annotations.ITestAnnotation;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class RetryListener implements IAnnotationTransformer {
    @Override
    public void transform(ITestAnnotation iTestAnnotation, Class aClass, Constructor constructor, Method method) {
        IRetryAnalyzer iRetryAnalyzer= iTestAnnotation.getRetryAnalyzer();
        if(iRetryAnalyzer==null){
            iTestAnnotation.setRetryAnalyzer(TestNGRetryAnalyzer.class);
        }
    }
}
```

使用方法一：在`TestNG`的执行文件中配置
在`TestNG`的执行文件的`suite`标签中，增加一个监听器，用于监听`suite`下所有的用例执行情况。

```xml
<suite name="接口测试" verbose="1"  >
    <listeners>
        <listener class-name="com.shadow.qa.common.listeners.RetryListener"/>
    </listeners>
    <test name="网管层接口" preserve-order="true">
        <packages>
            <package name="com.shadow.qa.testCases.hhh.*"/>
        </packages>
    </test>
</suite>
```

使用方法二：对特定的用例进行设置
在用例的`@Test`中，增加失败用例重跑的参数

```java
@Test(dataProvider = "data", description = "Test", retryAnalyzer = TestNGRetryAnalyzer.class)
```

### 问题处理

#### 使用`groups`时，`@BeforeClass`、`@BeforeSuite`被跳过

有两种解决方式：

1. 在`@BeforeClass`中添加`alwaysRun=true`

    ```java
    public class classTest {
        @BeforeClass(alwaysRun=true)
        public void initTest() {};
    
        @Test(groups = {"testGroup"})
        public static void testMethod() {};
    }
    ```

    `testNG`文件中包含了`该class`中存在的`groups`时，`该class`中的`@BeforeClass`才会执行，所以不必担心在所有的`@BeforeClass`中都添加`alwaysRun=true`会造成没必要的`@BeforeClass`执行的问题。

2. 在`@BeforeClass`中也添加需要的`groups`参数

    ```java
    public class classTest {
        @BeforeClass(groups = {"testGroup"})
        public void initTest() {};
    
        @Test(groups = {"testGroup"})
        public static void testMethod() {};
    }
    ```

#### 执行某个包下所有包含某个分组的用例

testNG的xml配置文件如下：

```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="接口测试" verbose="1">
    <test name="网管层接口" preserve-order="true">
        <groups>
            <run>
                <include name="testGroup"/>
            </run>
        </groups>

        <packages>
            <package name="com.shadow.qa.testCases.api.*"/>
        </packages>
    </test>
</suite>
```

多数文档说`groups`必须和`classes`配合使用，但是`class`是无法用通配符的，会造成要枚举所有的`class`，这样就会非常麻烦；
实际上`groups`也可以和`packages`配合使用，`packages`可以使用通配符，这样就大大省去了去找所有有需要的`groups`的`class`的麻烦
