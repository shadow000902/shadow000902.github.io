---
title: Robot-Framework内置变量总结
date: 2018-10-10 01:17:33
categories: [RobotFramework]
tags: [robot-framework]
---

#### 操作系统相关变量
内置的操作系统相关的变量，减少了测试数据对操作系统之间的差异性的关注

  <!--more-->

| 变量       | 用途                                                                                                                                            |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| ${CURDIR}  | 测试数据文件所在目录的绝对路径，该参数是大小写敏感的                                                                                            |
| ${TEMPDIR} | 操作系统临时目录的绝对路径，在类 Unix 系统中，该路径通常是 /tmp；在 Windows 系统中，通常是 c:\Documents and Settings\<user>\Local Settings\Temp |
| ${EXECDIR} | 到测试开始执行的目录的绝对路径                                                                                                                  |
| ${/}       | 操作系统文件路径分隔符，在类 Unix 系统中为： ‘/’， 在 Windows 中则为： ‘\’                                                                  |
| ${:}       | 操作系统路径元素分隔符，在类 Unix 系统中为： ‘：’，在 Windows 中则为： ‘；’                                                                 |
| ${\n}      | 操作系统行分隔符，在类 Unix 系统中为： ‘\n’，在 Windows 中则为： ‘\r\n’                                                                     |

```robot
*** Test Cases ***
Example
    Create Binary File    ${CURDIR}${/}input.data    Some text here${\n}on two lines
    Set Environment Variable    CLASSPATH    ${TEMPDIR}${:}${CURDIR}${/}foo.jar
```

#### 数字变量
变量语法能用来创建 整型 和 浮点型 数据。当一个关键字需要 真实的数字而非对应的数字字符串作为参数时，这种创建数字变量的方法是很有用的。

```robot
*** Test Cases ***
Example 1A
    Connect    example.com    80    # Connect 获得两个字符串作为参数
Example 1B
    Connect    example.com    ${80}    # Connect 获得一个字符串和一个整数作为参数
Example 2
    Do X    ${3.14}    ${‐1e‐4}    # Do X 获得浮点数 3.14 和 ‐0.0001 作为参数
```

从二进制，八进制和十六进制值来创建整数也是可以的，创建时分别用： 0b, 0o 和 0x 作为相应的前缀，并且这种语法是大小写不敏感的。

```robot
*** Test Cases ***
Example
    Should Be Equal    ${0b1011}    ${11}
    Should Be Equal    ${0o10}    ${8}
    Should Be Equal    ${0xff}    ${255}
    Should Be Equal    ${0B1010}   ${0XA}
```

#### 布尔值和 None/ null变量
布尔值和 Python 的 None，Java 的 null 变量也可以用创建数字变量类似的语法创建：

```robot
*** Test Cases ***
Boolean
    Set Status    ${true}    # Set Status 获得布尔值 true 作为参数
    Create Y    something    ${false}    # Create Y 获得字符串和布尔值 false 作为参数

None
Do XYZ    ${None}    # Do XYZ 获得 Python None 作为参数

Null
    ${ret} = Get Value    arg    # Checking that Get Value returns Java null
    Should Be Equal    ${ret}    ${null}
```

这些变量也是大小写不敏感的，所以 ${True} 和 ${true} 是一样的。此外 ${None} 和 ${null} 是同义词，因为用 Jython 解释器执行用例时， Jython 会自动将 None 和 null 转换成正确格式。

#### 空格和空（empty）变量
可以分别使用 ${SPACE} 和 ${EMPTY} 来创建空格和空字符串变量。这些变量很有用，如果不使用这些变量的话，就需要对空格或空单元格进行转义。如果需要一个以上的空格，也可以使用扩展变量语法来轻易获得，形如： ${SPACE * 5}。下面的例子中，Should Be Equal 关键字得到的参数值是相等的，但很明显使用变量的方式比使用 ‘\' 转义的方式更易理解。

```robot
*** Test Cases ***
One Space
    Should Be Equal     ${SPACE}     \ \
 
Four Spaces
    Should Be Equal     ${SPACE * 4}     \ \ \ \ \
 
Ten Spaces
    Should Be Equal     ${SPACE * 10}     \ \ \ \ \ \ \ \ \ \ \
 
Quoted Space
    Should Be Equal     "${SPACE}"     " "
 
Quoted Spaces
    Should Be Equal     "${SPACE * 2}"     " \ "
 
Empty
    Should Be Equal     ${EMPTY}     \
```

还有两个变量 @{EMPTY} 和 &{EMPTY}，他们分别表示 ‘空列表’ 和 ‘空字典’ 变量。 这两个变量也是有用的，例如在写测试模板的时候，模板关键字不带参数使用时。

```robot
*** Test Cases ***
Template
    [Template]     Some keyword
    @{EMPTY}
 
Override
    Set Global Variable     @{LIST}     @{EMPTY}
    Set Suite Variable     &{DICT}     &{EMPTY}
```

#### 自动变量
还有一些自动变量可以在测试数据中使用。这些变量在测试过程中可能有不同的取值，其中有一些甚至不是一直可用的。

| 变量                   | 解释                                                                                            | 使用地点            |
| ---------------------- | ----------------------------------------------------------------------------------------------- | ------------------- |
| ${TEST NAME}           | 当前测试用例的名称                                                                              | 测试用例中          |
| @{TEST TAGS}           | 当前测试用例被打上的所有标记，按字母顺序排列。可以使用 Set Tags 和 Remove Tags 关键字动态的修改 | 测试用例中          |
| ${TEST DOCUMENTATION}  | 当前测试用例的说明文档，可以使用 Set Test Documentation 关键字动态的修改                        | 测试用例中          |
| ${TEST STATUS}         | 当前测试用例的执行状态，PASS 或 FAIL                                                            | 测试用例 teardown时 |
| ${TEST MESSAGE}        | 当前测试用例的信息                                                                              | 测试用例 teardown时 |
| ${PREV TEST NAME}      | 前一个测试用例的名字，如果还没有测试用例被执行，则该值为空                                      | 所有地方            |
| ${PREV TEST STATUS}    | 前一个测试用例的执行状态，PASS/FAIL，如果还没有测试用例被执行，则该值为空                       | 所有地方            |
| ${PREV TEST MESSAGE}   | 前一个测试用例执行所产生的可能的错误信息                                                        | 所有地方            |
| ${SUITE NAME}          | 当前测试套件的全称                                                                              | 所有地方            |
| ${SUITE SOURCE}        | 当前测试套件文件或目录的绝对路径                                                                | 所有地方            |
| ${SUITE DOCUMENTATION} | 当前测试套件的说明文档，可以使用 Set Suite Documentation 关键字动态的改变                       | 所有地方            |
| &{SUITE METADATA}      | 当前测试套件的元数据                                                                            | 所有地方            |
| ${SUITE STATUS}        | 当前测试套件的执行状态， PASS 或 FAIL                                                           | 测试套件 teardown   |
| ${SUITE MESSAGE}       | 当前测试套件的全部信息，包括统计                                                                | 测试套件 teardown   |
| ${KEYWORD STATUS}      | 当前关键的执行状态，PASS 或 FAIL                                                                | 用户关键字 teardown |
| ${KEYWORD MESSAGE}     | 当前关键字执行时可能产生的错误信息                                                              | 用户关键字 teardown |
| ${LOG LEVEL}           | 当前日志级别                                                                                    | 所有地方            |
| ${OUTPUT FILE}         | 到输出文件的绝对路径                                                                            | 所有地方            |
| ${LOG FILE}            | 到日志文件的绝对路径，或者为NONE 当没有创建日志文件时                                           | 所有地方            |
| ${REPORT FILE}         | 到测试报告文件的绝对路径，或者为NONE 当没有创建测试报告文件时                                   | 所有地方            |
| ${DEBUG FILE}          | 到debug文件的绝对路径，或者为NONE 当没有创建debug文件时                                         | 所有地方            |
| ${OUTPUT DIR}          | 到输出目录的绝对路径                                                                            | 所有地方            |