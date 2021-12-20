---
title: Spock 测试框架学习
date: 2021-10-31 19:27:13
categories: [Spock]
tags: [spock]
---

### 异常测试

被测试方法：

 <!--more-->

<script>
    if("spockTest"===prompt("请输入文档密码"))
    {
        alert("密码正确");
    }
    else
    {
        alert("密码错误返回主页");
        location="/";
    }
</script>

```groovy
/**
 * 校验请求参数user是否合法
 * @param user
 * @throws APIException
 */
public void validateUser(UserVO user) throws APIException {
    if (user == null) {
        throw new APIException("10001", "user is null");
    }
    if (null == user.getName() || "".equals(user.getName())) {
        throw new APIException("10002", "user name is null");
    }
    if (user.getAge() == 0) {
        throw new APIException("10003", "user age is null");
    }
    if (null == user.getTelephone() || "".equals(user.getTelephone())) {
        throw new APIException("10004", "user telephone is null");
    }
    if (null == user.getSex() || "".equals(user.getSex())) {
        throw new APIException("10005", "user sex is null");
    }
    if (null == user.getUserOrders() || user.getUserOrders().size() <= 0) {
        throw new APIException("10006", "user order is null");
    }
    for (OrderVO order : user.getUserOrders()) {
        if (null == order.getOrderNum() || "".equals(order.getOrderNum())) {
            throw new APIException("10007", "order number is null");
        }
        if (null == order.getAmount()) {
            throw new APIException("10008", "order amount is null");
        }
    }
}
```

Spock测试方法：
```groovy
/**
 * 校验用户请求参数的测试类
 * @author 公众号:Java老K
 * 个人博客:www.javakk.com
 */
class UserControllerTest extends Specification {

    def userController = new UserController()

    @Unroll
    def "验证用户信息的合法性: #expectedMessage"() {
        when: "调用校验用户方法"
        userController.validateUser(user)

        then: "捕获异常并设置需要验证的异常值"
        def exception = thrown(expectedException)
        exception.errorCode == expectedErrCode
        exception.errorMessage == expectedMessage

        where: "表格方式验证用户信息的合法性"
        user           || expectedException | expectedErrCode | expectedMessage
        getUser(10001) || APIException      | "10001"         | "user is null"
        getUser(10002) || APIException      | "10002"         | "user name is null"
        getUser(10003) || APIException      | "10003"         | "user age is null"
        getUser(10004) || APIException      | "10004"         | "user telephone is null"
        getUser(10005) || APIException      | "10005"         | "user sex is null"
        getUser(10006) || APIException      | "10006"         | "user order is null"
        getUser(10007) || APIException      | "10007"         | "order number is null"
        getUser(10008) || APIException      | "10008"         | "order amount is null"
    }

    def getUser(errCode) {
        def user = new UserVO()
        def condition1 = {
            user.name = "杜兰特"
        }
        def condition2 = {
            user.age = 20
        }
        def condition3 = {
            user.telephone = "15801833812"
        }
        def condition4 = {
            user.sex = "男"
        }
        def condition5 = {
            user.userOrders = [new OrderVO()]
        }
        def condition6 = {
            user.userOrders = [new OrderVO(orderNum: "123456")]
        }

        switch (errCode) {
            case 10001:
                user = null
                break
            case 10002:
                user = new UserVO()
                break
            case 10003:
                condition1()
                break
            case 10004:
                condition1()
                condition2()
                break
            case 10005:
                condition1()
                condition2()
                condition3()
                break
            case 10006:
                condition1()
                condition2()
                condition3()
                condition4()
                break
            case 10007:
                condition1()
                condition2()
                condition3()
                condition4()
                condition5()
                break
            case 10008:
                condition1()
                condition2()
                condition3()
                condition4()
                condition5()
                condition6()
                break
        }
        return user
    }
}
```

### 合并参数正常和异常用例，合并多个调用异常的用例
```groovy
package com.shadow.search.biz.impl

import com.shadow.platform.bootstrap.exception.BusinessException
import com.shadow.api.search.search.request.CustomerOperationInfoSyncRequest
import com.shadow.search.common.entity.SyncTemplate
import com.shadow.search.dal.async.CustomerOperationInfoAsyncActuator
import com.shadow.search.domain.search.repository.CustomerOperationRepository
import spock.lang.Specification

class CustomerOperationInfoSyncBizServiceImplSpec extends Specification {

    def customerOperationInfoSyncBizServiceImpl = new CustomerOperationInfoSyncBizServiceImpl()
    def customerOperationRepository = Mock(CustomerOperationRepository)
    def customerOperationInfoAsyncActuator = Mock(CustomerOperationInfoAsyncActuator)

    void setup() {
        customerOperationInfoSyncBizServiceImpl.customerOperationRepository = customerOperationRepository
        customerOperationInfoSyncBizServiceImpl.customerOperationInfoAsyncActuator = customerOperationInfoAsyncActuator
    }


    def "客户运营数据同步_batchSync_参数测试"(Long userId, Long kdtId, Long ts) {
        setup: "数据准备"
        def customerOperationInfo1 = [
                userId          : userId,
                kdtId           : kdtId,
//                wcKdtId         : 789,
                wecomStaffIds   : [12, 23, 34],
                wechatGroupIds  : ["123", "234", "345"],
//                salesmanStaffId : 123456,
                isWecomSalesman : 1,
                hasAddStaff     : 1,
                lastAddStaffTime: 123,
                ts              : ts
        ] as CustomerOperationInfoSyncRequest
        def customerOperationInfo2 = [
                userId          : userId,
                kdtId           : kdtId,
                wcKdtId         : 789,
                wecomStaffIds   : [12, 23, 34],
                wechatGroupIds  : ["123", "234", "345"],
                salesmanStaffId : 123456,
//                isWecomSalesman : 1,
//                hasAddStaff     : 1,
                lastAddStaffTime: 123,
                ts              : ts
        ] as CustomerOperationInfoSyncRequest
        def customerOperationEntityList = [
                customerOperationInfo1,
                customerOperationInfo2
        ]

        and: "Mock方法调用数据返回"
        batchPutCount * customerOperationRepository.batchPut(_) >> batchPutResp
        sendSyncDataMsgCount * customerOperationInfoAsyncActuator.sendSyncDataMsg(kdtId, userId, SyncTemplate.UPDATE) >> sendSyncDataMsgResp

        when: "执行需要测试的方法"
        def resp = customerOperationInfoSyncBizServiceImpl.batchSync(customerOperationEntityList)
        println resp
        throw new BusinessException(000000000, "success")

        then: "结果校验"
        def exception = thrown(expectedException)
        exception.code == expectedCode
        exception.message == expectedMessage


        where: "数据驱动"
        testName          | userId | kdtId    | ts                         | batchPutCount | batchPutResp | sendSyncDataMsgCount | sendSyncDataMsgResp || expectedException | expectedCode | expectedMessage
        "normal test 1"   | 123    | 59941009 | 123456                     | 1             | true         | 2                    | null                || BusinessException | 000000000    | "success"
        "normal test 2"   | 456    | 59941009 | 123456                     | 1             | true         | 2                    | null                || BusinessException | 000000000    | "success"
        "normal test 3"   | 789    | 59941009 | System.currentTimeMillis() | 1             | true         | 2                    | null                || BusinessException | 000000000    | "success"
        "userId is null"  | null   | 59941009 | System.currentTimeMillis() | 0             | false        | 0                    | null                || BusinessException | 145400001    | "参数错误"
        "userId is minus" | -1     | 59941009 | System.currentTimeMillis() | 0             | false        | 0                    | null                || BusinessException | 145400001    | "参数错误"
        "kdtId is null"   | 123456 | null     | System.currentTimeMillis() | 0             | false        | 0                    | null                || BusinessException | 145400001    | "参数错误"
        "kdtId is minus"  | 123456 | -1       | System.currentTimeMillis() | 0             | false        | 0                    | null                || BusinessException | 145400001    | "参数错误"
        "ts is null"      | 789    | 59941009 | null                       | 0             | false        | 0                    | null                || BusinessException | 145400001    | "参数错误"
        "ts is minus"     | 789    | 59941009 | -1                         | 0             | false        | 0                    | null                || BusinessException | 145400001    | "参数错误"
//        "batchPut exception"        | 123    | 59941009 | 1234567                    | 1             | { throw new IOException() } | 2                    | null                        || BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
//        "sendSyncDataMsg exception" | 123    | 59941009 | 1234567                    | 1             | true                        | 2                    | { throw new IOException() } || BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
    }

    def "客户运营数据同步_batchSync_调用异常测试"() {
        setup: "数据准备"
        def customerOperationInfoSyncRequest = [
                userId          : 123456,
                kdtId           : 59941009,
                wcKdtId         : 789,
                wecomStaffIds   : [12, 23, 34],
                wechatGroupIds  : ["123", "234", "345"],
                salesmanStaffId : 123456,
                isWecomSalesman : 1,
                hasAddStaff     : 1,
                lastAddStaffTime: 123,
                ts              : System.currentTimeMillis()
        ] as CustomerOperationInfoSyncRequest

        when: "执行需要测试的方法"
        customerOperationInfoSyncBizServiceImpl.batchSync([customerOperationInfoSyncRequest])

        then: "结果校验"
        // TODO 异常mock有问题
        batchPutCount * customerOperationRepository.batchPut(_) >> {
            if (testName.contains("normal batchPut")) {
                true
            } else {
                throw new IOException()
            }
        }
        sendSyncDataMsgCount * customerOperationInfoAsyncActuator.sendSyncDataMsg(59941009, 123456, SyncTemplate.UPDATE) >> { throw sendSyncDataMsgResp }

        def exception = thrown(expectedException)
        exception.code == expectedCode
        exception.message == expectedMessage

        where: "数据驱动"
        testName                                            | batchPutCount | sendSyncDataMsgCount | sendSyncDataMsgResp    || expectedException | expectedCode | expectedMessage
        "batchPut exception"                                | 1             | 0                    | null                   || BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
        "normal batchPut, sendSyncDataMsg IOException"      | 1             | 1                    | new IOException()      || BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
        "normal batchPut, sendSyncDataMsg RuntimeException" | 1             | 1                    | new RuntimeException() || BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
    }

    def "客户运营数据同步_delete_参数测试"(Long userId, Long kdtId) {
        setup: "数据准备"


        and: "Mock方法调用数据返回"
        deleteCount * customerOperationRepository.delete(kdtId, userId) >> deleteResp
        sendSyncDataMsgCount * customerOperationInfoAsyncActuator.sendSyncDataMsg(kdtId, userId, SyncTemplate.UPDATE) >> sendSyncDataMsgResp

        when: "执行需要测试的方法"
        def resp = customerOperationInfoSyncBizServiceImpl.delete(kdtId, userId)
        println resp
        throw new BusinessException(000000000, "success")

        then: "结果校验"
        def exception = thrown(expectedException)
        exception.code == expectedCode
        exception.message == expectedMessage

        where: "数据驱动"
        testName                    | userId | kdtId    | deleteCount | deleteResp | sendSyncDataMsgCount | sendSyncDataMsgResp | expectedException | expectedCode | expectedMessage
        "normal Test"               | 123456 | 59941009 | 1           | true       | 1                    | null                | BusinessException | 000000000    | "success"
        "userId and kdtId all zero" | 0      | 0        | 0           | null       | 0                    | null                | BusinessException | 145400001    | "参数错误"
        "userId is minus"           | -1     | 59941009 | 0           | null       | 0                    | null                | BusinessException | 145400001    | "参数错误"
        "kdtId is minus"            | 123456 | -1       | 0           | null       | 0                    | null                | BusinessException | 145400001    | "参数错误"
        "kdtId is null"             | 123456 | null     | 0           | null       | 0                    | null                | BusinessException | 145400001    | "参数错误"
        "userId is null"            | null   | 59941009 | 0           | null       | 0                    | null                | BusinessException | 145400001    | "参数错误"
    }

    def "客户运营数据同步_delete_调用异常测试"() {
        setup: "数据准备"
        def userId = 123456L
        def kdtId = 59941009L

        and: "Mock方法调用数据返回"
        deleteCount * customerOperationRepository.delete(kdtId, userId) >> {
            if (testName.contains("normal delete")) {
                true
            } else {
                throw deleteResp
            }
        }
        sendSyncDataMsgCount * customerOperationInfoAsyncActuator.sendSyncDataMsg(kdtId, userId, SyncTemplate.UPDATE) >> {throw sendSyncDataMsgResp}

        when: "执行需要测试的方法"
        customerOperationInfoSyncBizServiceImpl.delete(kdtId, userId)

        then: "结果校验"
        def exception = thrown(expectedException)
        exception.code == expectedCode
        exception.message == expectedMessage

        where: "数据驱动"
        testName                                                | deleteCount | deleteResp             | sendSyncDataMsgCount | sendSyncDataMsgResp    | expectedException | expectedCode | expectedMessage
        "delete throw IOException"                              | 1           | new IOException()      | 0                    | null                   | BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
        "delete throw RuntimeException"                         | 1           | new RuntimeException() | 0                    | null                   | BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
        "normal delete, sendSyncDataMsg throw IOException"      | 1           | null                   | 1                    | new IOException()      | BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
        "normal delete, sendSyncDataMsg throw RuntimeException" | 1           | null                   | 1                    | new RuntimeException() | BusinessException | 145400006    | "Hbase内部异常，内部将进行重试，保证最终一致性，外部无须重试"
    }
}
```

### Spock 抛 MissingPropertyException 问题解决

有问题的测试代码：
```groovy
package foo.bar.test

import foo.bah.HttpRequestPropertyLoader
import spock.lang.Unroll
import javax.servlet.http.HttpServletRequest
import spock.lang.Specification

class HttpRequestPropertyLoaderTest extends Specification {

    HttpRequestPropertyLoader subjectUnderTest
    def result

    def setup() {
        subjectUnderTest = new HttpRequestPropertyLoader()
    }

    @Unroll("When my http request is #nullOrNot then when I get parameter from it the response=#response" )
    def "Test load data from request"() {
        given:
        HttpServletRequest mockHttpRequest = Mock()
        mockHttpRequest.getAttribute("foo") >> "bar"
        when:
        result = subjectUnderTest.loadStringFromHttpRequest(httpRequest, "foo")
        then:
        result == response
        where:
        httpRequest     | response | nullOrNot
        null            |  ""      | "null"
        mockHttpRequest | "bar"    | "not null"
    }
}
```

问题原因：`where块`在`given`之前运行块

解决问题后的代码：

```groovy
package foo.bar.test

import foo.bah.HttpRequestPropertyLoader
import spock.lang.Unroll
import javax.servlet.http.HttpServletRequest
import spock.lang.Specification

class HttpRequestPropertyLoaderTest extends Specification {

    HttpRequestPropertyLoader subjectUnderTest
    def result

    def setup() {
        subjectUnderTest = new HttpRequestPropertyLoader()
    }

    @Unroll("When my http request is #nullOrNot then when I get parameter from it the response=#response")
    def "Test load data from request"() {
        when:
        result = subjectUnderTest.loadStringFromHttpRequest(httpRequest, "foo")
        then:
        result == response
        where:
        httpRequest << {
            HttpServletRequest mockHttpRequest = Mock()
            mockHttpRequest.getAttribute("foo") >> "bar"
            [null, mockHttpRequest]
        }()
        response << ["", "bar"]
        nullOrNot << ["null", "not null"]
    }
}
```


### 参考
1. https://www.coder.work/article/6733126