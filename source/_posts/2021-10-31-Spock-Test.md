---
title: Spock 测试实践
date: 2021-10-31 19:27:13
categories: [Spock]
tags: [spock]
---

### 异常测试
#### 被测对象

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

#### Spock测试类
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


### 被测对象有调用父类时的测试方法
#### 被测对象
```java
package com.shadow.cloud.dennis.chain.biz.extension.member.changyi;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.shadow.api.rpc.annotation.ExtensionService;
import com.shadow.cloud.dennis.chain.api.enums.GenderEnum;
import com.shadow.cloud.dennis.chain.api.model.User;
import com.shadow.cloud.dennis.chain.api.model.UserRecord;
import com.shadow.cloud.dennis.chain.biz.common.cloud.UserAPI;
import com.shadow.cloud.dennis.chain.biz.extension.ExtensionBase;
import com.shadow.cloud.dennis.chain.biz.extension.member.changyi.api.DennisCrmClient;
import com.shadow.cloud.dennis.chain.biz.extension.member.changyi.bean.QueryMemberInfoCrmRequest;
import com.shadow.cloud.dennis.chain.biz.extension.member.changyi.bean.QueryMemberInfoCrmResponse;
import com.shadow.cloud.dennis.chain.biz.quartz.JobConstant;
import com.shadow.cloud.dennis.chain.biz.quartz.JobEntity;
import com.shadow.cloud.dennis.chain.biz.quartz.MemberCreateJob;
import com.shadow.cloud.dennis.chain.biz.quartz.SchedulerConfig;
import com.shadow.cloud.dennis.chain.biz.service.UserService;
import com.shadow.cloud.dennis.chain.biz.utils.OutParamUtil;
import com.shadow.cloud.dennis.chain.dal.mapper.UserRecordMapper;
import com.shadow.cloud.extension.api.scrm.GetCustomerExtPoint;
import com.shadow.cloud.extension.param.scrm.*;
import com.shadow.cloud.metadata.common.OutParam;
import com.shadow.cloud.open.sdk.gen.v3_0_1.model.ShadowUserBasicGetResult;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;


@Slf4j
@ExtensionService("getCustomerExtPoint")
@Service
public class GetCustomerEx extends ExtensionBase implements GetCustomerExtPoint {


    @Resource
    private DennisCrmClient dennisCrmClient;

    @Autowired
    protected UserService userService;

    @Autowired
    private UserRecordMapper userRecordMapper;


    @Autowired
    private UserAPI userAPI;


    @Override
    public OutParam<CustomerProfileDTO> execute(CustomerIdentifyDTO customerIdentifyDTO) {
        CustomerProfileDTO customerProfileDTO = new CustomerProfileDTO();
        try {
            String yzOpenId = customerIdentifyDTO.getYzOpenId();


            if (!isBinding(yzOpenId)) {//没绑定的情况重试
                log.info("客户会员信息查询扩展点，查询长益crm会员信息失败,不存在会员绑定关系，扩展点请求参数 ： {}", JSON.toJSONString(customerIdentifyDTO));
                CreateCustomerRequestDTO createCustomerRequestDTO = new CreateCustomerRequestDTO();
                createCustomerRequestDTO.setCustomerIdentifyDTO(customerIdentifyDTO);
                CustomerProfileCreateDTO customerProfileCreateDTO = new CustomerProfileCreateDTO();
                //查询手机号
                ShadowUserBasicGetResult shadowUserBasicInfoByOpenId = userAPI.getShadowUserBasicInfoByOpenId(customerIdentifyDTO.getKdtId().toString(), customerIdentifyDTO.getYzOpenId());
                if (shadowUserBasicInfoByOpenId.getSuccess() && shadowUserBasicInfoByOpenId.getData() != null && shadowUserBasicInfoByOpenId.getData().getMobile() != null) {
                    customerProfileCreateDTO.setRegisterMobile(shadowUserBasicInfoByOpenId.getData().getMobile());
                    createCustomerRequestDTO.setCustomerProfileCreateDTO(customerProfileCreateDTO);
                    insertUserRecord(createCustomerRequestDTO);
                } else {
                    log.info("客户会员信息查询扩展点，请求有赞Api返回参数 ： {}", JSON.toJSONString(shadowUserBasicInfoByOpenId));
                }
                return OutParamUtil.failResult("查询失败", customerProfileDTO);
            }


            QueryMemberInfoCrmResponse queryMemberInfoCrmResponse = this.queryMemberInfoCrm(yzOpenId);
            log.info("客户会员信息查询扩展点, 查询三方会员信息，三方响应参数 ：  {} ", JSON.toJSONString(queryMemberInfoCrmResponse));
            if (queryMemberInfoCrmResponse != null && queryMemberInfoCrmResponse.isSuccess()) {
                customerProfileDTO.setName(queryMemberInfoCrmResponse.getMemberName());
                String memberSex = queryMemberInfoCrmResponse.getMemberSex();
                if (StringUtils.isNotBlank(memberSex)) {
                    customerProfileDTO.setGender(GenderEnum.getEnum(memberSex).shortValue());
                }
                customerProfileDTO.setBirthday(queryMemberInfoCrmResponse.getMemberBirthday());
                //是否会员
                customerProfileDTO.setIsMember(false);
                ContactAddressDTO contactAddressDTO = new ContactAddressDTO();
                //地域编码
                contactAddressDTO.setAreaCode(queryMemberInfoCrmResponse.getMemberAddress());
                contactAddressDTO.setAddress(queryMemberInfoCrmResponse.getMemberAddress());
                customerProfileDTO.setContactAddressDTO(contactAddressDTO);
                customerProfileDTO.setEmail(queryMemberInfoCrmResponse.getMemberEmail());
                return OutParamUtil.successResult(customerProfileDTO);

            } else {
                //查询失败
                log.error("客户会员信息查询扩展点, 查询三方会员信息失败，三方响应参数 : {} ", JSONObject.toJSONString(queryMemberInfoCrmResponse));
                return OutParamUtil.failResult("查询失败", customerProfileDTO);
            }

        } catch (Exception e) {
            log.error("长益crm查询会员信息失败！", e);

        }
        return OutParamUtil.failResult("查询失败", customerProfileDTO);
    }


    public QueryMemberInfoCrmResponse queryMemberInfoCrm(String yzOpenId) {


        try {
            QueryMemberInfoCrmResponse memberInfoCrmFromRedis = getMemberInfoCrmFromRedis(yzOpenId);
            if (memberInfoCrmFromRedis != null) {
                memberInfoCrmFromRedis.setSuccess(true);
                return memberInfoCrmFromRedis;
            } else {
                User user = getUser(yzOpenId);
                //查询会员信息
                QueryMemberInfoCrmRequest queryMemberInfoCrmRequest = new QueryMemberInfoCrmRequest();
                queryMemberInfoCrmRequest.setCondType("3");
                queryMemberInfoCrmRequest.setCondValue(user.getMobile());
                QueryMemberInfoCrmResponse queryMemberInfoCrmResponse = dennisCrmClient.post(queryMemberInfoCrmRequest);
                if (queryMemberInfoCrmResponse.isSuccess()) {
                    setMemberInfoCrmToRedis(queryMemberInfoCrmResponse, user);
                }
                return queryMemberInfoCrmResponse;
            }
        } catch (Exception e) {
            log.info("查询会员信息失败===", e);
        }
        return null;

    }


    /**
     * 添加重试记录
     *
     * @param createCustomerRequestDTO
     * @param
     */
    public void insertUserRecord(CreateCustomerRequestDTO createCustomerRequestDTO) {
        //用户在crm中存在，只用建立关系
        try {
            UserRecord bind = new UserRecord();
            bind.setMsgId(createCustomerRequestDTO.getCustomerIdentifyDTO().getYzOpenId());
            bind.setKdtId(createCustomerRequestDTO.getCustomerIdentifyDTO().getKdtId());
            bind.setMsgInfo(JSON.toJSONString(createCustomerRequestDTO));
            bind.setStatus(0);
            bind.setTimes(0);
            bind.setType(1);

            try {
                int count = userRecordMapper.insertSelective(bind);
            } catch (Exception e) {
                userRecordMapper.updateByMsgIdToTime(createCustomerRequestDTO.getCustomerIdentifyDTO().getYzOpenId());
            }
            SchedulerConfig.addJob(new JobEntity(JobConstant.MENBER_CREATE_GROUP + createCustomerRequestDTO.getCustomerIdentifyDTO().getYzOpenId(), JobConstant.MENBER_CREATE_GROUP, MemberCreateJob.class.getName(), createCustomerRequestDTO.getCustomerIdentifyDTO().getYzOpenId(), 1));

        } catch (Exception e) {
            log.error("客户会员信息查询扩展点中添加重试记录出错", e);
        }

    }

}
```

#### 被测对象父类
```java
package com.shadow.cloud.dennis.chain.biz.extension;

import com.shadow.cloud.dennis.chain.api.exception.NoSuchRedisKeyException;
import com.shadow.cloud.dennis.chain.api.model.User;
import com.shadow.cloud.dennis.chain.biz.common.rest.ezrpro.RestTemplateEzrpro;
import com.shadow.cloud.dennis.chain.biz.extension.member.changyi.bean.QueryMemberInfoCrmResponse;
import com.shadow.cloud.dennis.chain.biz.service.UserService;
import com.shadow.cloud.dennis.chain.biz.utils.RedisUtil;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;


@Slf4j
@Service
public class ExtensionBase{

    @Autowired
    protected UserService userService;
    @Autowired
    protected RestTemplateEzrpro baseRestTemplate;

    /***
     * 用户账号绑定数据，通过yzOpenId取值
     ****/
    public User getUserFromRedis(String yzOpenId) {
        try{
            User user =  RedisUtil.get("yz_open_id:" + yzOpenId, User.class);
            return user;
        } catch (NoSuchRedisKeyException e){
            log.error("获取redis用户数据失败", e);
        }
        return null;
    }

    /***
     * 用户详细信息，通过yzOpenId取值
     ****/
    public QueryMemberInfoCrmResponse getMemberInfoCrmFromRedis(String yzOpenId) {
        try{
            QueryMemberInfoCrmResponse queryMemberInfoCrmResponse =  RedisUtil.get("yz_open_id:MemberInfoCrm"+yzOpenId, QueryMemberInfoCrmResponse.class);
            return queryMemberInfoCrmResponse;
        } catch (NoSuchRedisKeyException e){
            log.error("获取redis用户数据失败", e);
        }
        return null;
    }

    /***
     * 用户账号绑定数据，通过accountId取值
     ****/
    public User getUserFromRedis(Long accountId) {
        try{
            User user =  RedisUtil.get("account_id:" + accountId, User.class);
            return user;
        } catch (NoSuchRedisKeyException e){
            log.error("获取redis用户数据失败", e);
        }
        return null;
    }

    /**
     * 有的扩展点只有yz_open_id，有的扩展点只有account_id，因此：
     * redis两个都保存了
     * ***/
    public void setUserToRedis(User user) {
        try{
            if(user.getYzOpenId() != null) {
                RedisUtil.set("yz_open_id:" + user.getYzOpenId(), user,120L,TimeUnit.MINUTES);
            }
            if(user.getAccountId() != null) {
                RedisUtil.set("account_id:" + user.getAccountId(), user,120L,TimeUnit.MINUTES);
            }
        } catch (Exception e){
            log.error("设置redis用户数据失败", e);
        }
    }

    /**
     * 有的扩展点只有yz_open_id，有的扩展点只有account_id，因此：
     * redis两个都保存了
     * ***/
    public void setMemberInfoCrmToRedis(QueryMemberInfoCrmResponse queryMemberInfoCrmResponse,User user) {

        try{
            if(user.getYzOpenId() != null) {
                RedisUtil.set("yz_open_id:MemberInfoCrm" + user.getYzOpenId(), queryMemberInfoCrmResponse,30L, TimeUnit.MINUTES);
            }
            if(user.getAccountId() != null) {
                RedisUtil.set("account_id:MemberInfoCrm" + user.getAccountId(), queryMemberInfoCrmResponse,30L, TimeUnit.MINUTES);
            }
        } catch (Exception e){
            log.error("设置redis用户数据失败", e);
        }
    }


    /***
     * 通过yz_open_id
     * 获取三方--有赞用户关联表中的纪录
     * ***/
    protected User getUser(String yzOpenId){

        User tmpUser = userService.getUserByYzOpenId(yzOpenId);
        return tmpUser;
    }

    /***
     * 通过accountId
     * 获取三方--有赞用户关联表中的纪录
     * ***/
    protected User getUser(Long accountId) {
        User tmpUser = userService.getUserByAccountId(String.valueOf(accountId));
        return tmpUser;
    }

    /***
     * 通过yz_open_id
     * 是否绑定过会员
     * ***/
    public boolean isBinding(String yzOpenId){
        User user = this.getUser(yzOpenId);
        if (null == user || user.getMemberId().isEmpty()) {//没绑定
            return false;
        }
        return true;
    }

    /***
     * 通过accountId
     * 是否绑定过会员
     * ***/
    protected boolean isBinding(Long accountId){
        User user = this.getUser(accountId);
        if (null == user || user.getMemberId().isEmpty()) {//没绑定
            return false;
        }
        return true;
    }

}
```

#### Spock测试类
```groovy
package com.shadow.cloud.dennis.chain.test

import com.shadow.cloud.dennis.chain.biz.common.cloud.UserAPI
import com.shadow.cloud.dennis.chain.biz.extension.member.changyi.GetCustomerEx
import com.shadow.cloud.dennis.chain.biz.extension.member.changyi.api.DennisCrmClient
import com.shadow.cloud.dennis.chain.biz.extension.member.changyi.bean.QueryMemberInfoCrmResponse
import com.shadow.cloud.dennis.chain.biz.service.UserService
import com.shadow.cloud.extension.param.scrm.CustomerIdentifyDTO
import com.shadow.cloud.dennis.chain.api.model.User
import com.shadow.cloud.open.sdk.gen.v3_0_1.model.ShadowUserBasicGetResult;
import spock.lang.Specification

class GetCustomerExTest extends Specification {

    def getCustomerExtPoint = Spy(GetCustomerEx.class)

    DennisCrmClient dennisCrmClient = Mock()
    UserService userService = Mock()
    UserAPI userAPI = Mock()

//    void setup() {
//        getCustomerExtPoint.dennisCrmClient = dennisCrmClient
//        getCustomerExtPoint.userService = userService
//    }

    def "Execute"(Long accountId, String accountType, Long kdtId, String mobile, Integer nodeKdtId, String yzOpenId) {
        setup: "验证扩展点"
        GetCustomerEx.metaClass.setProperty(getCustomerExtPoint, "userService", userService)
        GetCustomerEx.metaClass.setProperty(getCustomerExtPoint, "dennisCrmClient", dennisCrmClient)
        GetCustomerEx.metaClass.setProperty(getCustomerExtPoint, "userAPI", userAPI)
        def customerIdentifyDTO = new CustomerIdentifyDTO(
                accountId: accountId,
                accountType: accountType,
                kdtId: kdtId,
                mobile: mobile,
                nodeKdtId: nodeKdtId,
                yzOpenId: yzOpenId)
        def queryMemberInfoCrmResponse = [
                isSuccess: true
        ] as QueryMemberInfoCrmResponse

        def user = [
                accountId: accountId,
                memberId : "123456",
                kdtId    : kdtId,
                mobile   : mobile,
                yzOpenId : yzOpenId,
        ] as User

        def shadowUserBasicGetResultData = [
                mobile      : mobile,
                avatar      : null,
                nick_name   : null,
                yz_open_id  : yzOpenId,
                country_code: null
        ] as ShadowUserBasicGetResult.ShadowUserBasicGetResultData

        def shadowUserBasicGetResult = [
                code    : 200,
                data    : shadowUserBasicGetResultData,
                success : true,
                message : null,
                trace_id: null
        ] as ShadowUserBasicGetResult

        and: "Mock方法调用"
        0 * dennisCrmClient.post(_) >> queryMemberInfoCrmResponse
        1 * getCustomerExtPoint.getUser(yzOpenId) >> user >> user
        0 * userAPI.getShadowUserBasicInfoByOpenId(kdtId.toString(), yzOpenId) >> shadowUserBasicGetResult
        1 * getCustomerExtPoint.getMemberInfoCrmFromRedis(yzOpenId) >> queryMemberInfoCrmResponse
        0 * getCustomerExtPoint.setMemberInfoCrmToRedis(queryMemberInfoCrmResponse, user) >> null

        when: "预期结果"
        def resp = this.getCustomerExtPoint.execute(customerIdentifyDTO)

        then: "验证结果"
        assert resp.code == result
        where: "数据准备"
        accountId     | accountType     | kdtId    | mobile        | nodeKdtId  | yzOpenId                     || result
        "16285515049" | "ShaDowAccount" | 91020932 | "15512341234" | "91020932" | "DhYBgpIs910549797344243712" || "200"
    }

}
```

### Spock依赖整理
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>shadow-sd</artifactId>
        <groupId>com.shadow.sd</groupId>
        <version>1.1.6-RELEASE</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>shadow-sd-spock</artifactId>

    
    <properties>

        <groovy.version>3.0.9</groovy.version>
        <spock.version>2.0-groovy-3.0</spock.version>
        <junitplatform.version>1.8.2</junitplatform.version>


        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
    </properties>


    <dependencies>

        <!--被测对象 dependency-->
        <dependency>
            <groupId>com.shadow.sd</groupId>
            <artifactId>shadow-api</artifactId>
            <version>1.7.25-RELEASE</version>
            <scope>test</scope>
        </dependency>
        ......

        <!--groovy dependency-->
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy</artifactId>
            <version>${groovy.version}</version>
        </dependency>
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-json</artifactId>
            <version>${groovy.version}</version>
        </dependency>
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-templates</artifactId>
            <version>${groovy.version}</version>
        </dependency>
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-sql</artifactId>
            <version>${groovy.version}</version>
        </dependency>
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-xml</artifactId>
            <version>${groovy.version}</version>
        </dependency>
        <dependency>
            <groupId>org.codehaus.groovy</groupId>
            <artifactId>groovy-all</artifactId>
            <type>pom</type>
            <version>${groovy.version}</version>
            <exclusions>
                <exclusion>
                    <artifactId>groovy-test-junit5</artifactId>
                    <groupId>org.codehaus.groovy</groupId>
                </exclusion>
                <exclusion>
                    <artifactId>groovy-testng</artifactId>
                    <groupId>org.codehaus.groovy</groupId>
                </exclusion>
            </exclusions>
        </dependency>

        <!--spock dependency-->
        <dependency>
            <groupId>org.spockframework</groupId>
            <artifactId>spock-core</artifactId>
            <version>${spock.version}</version>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <artifactId>junit-platform-engine</artifactId>
                    <groupId>org.junit.platform</groupId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>com.athaydes</groupId>
            <artifactId>spock-reports</artifactId>
            <version>${spock.version}</version>
        </dependency>

        <!--junitplatform dependency-->
        <dependency>
            <groupId>org.junit.platform</groupId>
            <artifactId>junit-platform-launcher</artifactId>
            <version>${junitplatform.version}</version>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <artifactId>junit-platform-engine</artifactId>
                    <groupId>org.junit.platform</groupId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>org.junit.platform</groupId>
            <artifactId>junit-platform-engine</artifactId>
            <version>${junitplatform.version}</version>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <artifactId>junit-platform-commons</artifactId>
                    <groupId>org.junit.platform</groupId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>org.junit.platform</groupId>
            <artifactId>junit-platform-commons</artifactId>
            <version>${junitplatform.version}</version>
            <scope>test</scope>
        </dependency>

        <!--other dependency-->
        <dependency>
            <groupId>org.apache.ant</groupId>
            <artifactId>ant</artifactId>
            <version>1.10.11</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

### 参考
1. https://www.coder.work/article/6733126