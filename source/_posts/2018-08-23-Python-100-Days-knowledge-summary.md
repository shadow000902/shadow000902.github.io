---
title: Python-100-Days 知识小结
date: 2018-08-23 23:52:25
categories: [Python]
tags: [python]
---

1. ``range``
    ```python
    range(101)                  # 产生一个0到100的整数序列
    range(1, 100)               # 产生一个1到99的整数序列
    range(1, 100, 2)            # 产生一个1到99的奇数序列，其中2是步长，即数值序列的增量
    range(100, 1, -2)           # 产生一个100到2的偶数序列，其中-2是步长，最后一个序列值是2
    ```

  <!--more-->

2. ``input``
    ```python
    raw = input('请输入：')     # 用于读取控制台输入的值
    ```

3. Python内置函数
    - 数学相关: abs / divmod / pow / round / min / max / sum
    - 序列相关: len / range / next / filter / map / sorted / slice / reversed
    - 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
    - 数据结构: dict / list / set / tuple
    - 其他函数: all / any / id / input / open / print / type

4. Python常用模块
    - 运行时服务相关模块: copy / pickle / sys / ...
    - 数学相关模块: decimal / math / random / ...
    - 字符串处理模块: codecs / re / ...
    - 文件处理相关模块: shutil / gzip / ...
    - 操作系统服务相关模块: datetime / os / time / logging / io / ...
    - 进程和线程相关模块: multiprocessing / threading / queue
    - 网络应用相关模块: ftplib / http / smtplib / urllib / ...
    - Web编程相关模块: cgi / webbrowser
    - 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

5. 函数的参数
    - 默认参数
    - 可变参数
    - 关键字参数
    - 命名关键字参数
    ```python
    # 可变参数
    def f2(*args):
        sum = 0
        for num in args:
            sum += num
        return sum

    print(f2(1, 2, 3))
    ```
    ```python
    # 关键字参数
    def f3(**kw):
        if 'name' in kw:
            print('欢迎你%s!' % kw['name'])
        elif 'tel' in kw:
            print('你的联系电话是: %s!' % kw['tel'])
        else:
            print('没找到你的个人信息!')

    param = {'name': '骆昊', 'age': 38}
    f3(**param)
    f3(name='骆昊', age=38, tel='13866778899')
    ```

    `*args`是非关键字参数，用于元组，`**kw`是关键字参数，用于字典
    ```python
    # *args 是非关键字参数，用于元组
    def tupleArgs(arg1, arg2= 'B', *arg3):
        print('arg 1:%s ' % arg1)
        print('arg 2:%s ' % arg2)
        for eachArgNum in range(len(arg3)):
            print('the %d in arg 3 :%s ' % (eachArgNum,arg3[eachArgNum]))
    if __name__ == '__main__':
        tupleArgs('A')
        #   arg 1:A
        #   arg 2:B
        tupleArgs('23','C')
        #   arg 1:23
        #   arg 2:C
        tupleArgs('12','A','GF','L')
        #   arg 1:12
        #   arg 2:A
        #   the 0 in arg 3 :GF
        #   the 1 in arg 3 :L

    # **kw 是关键字参数，用于字典
        def dictArgs(kw1, kw2= 'B', **kw3):
        print('kw 1:%s ' % kw1)
        print('kw 2:%s ' % kw2)
        for eachKw in kw3:
            print('the %s ---->:%s ' % (eachKw,kw3[eachKw]))
    if __name__ == '__main__':
        dictArgs('A')
        #   kw 1:A 
        #   kw 2:B 
        dictArgs('23','C')
        #   kw 1:23
        #   kw 2:C 
        dictArgs('12','A', c = 'C',d = '12121212')
        #   kw 1:12  
        #   kw 2:A 
        #   the d ---->:12121212 
        #   the c ---->:C 
        dictArgs('kw',c = 'C',d = '12121212',kw = 'KW')
        #   kw 1:kw 
        #   kw 2:B 
        #   the kw ---->:KW 
        #   the d ---->:12121212 
        #   the c ---->:C
    ```

6. 集合的常用操作
    - 交集
    - 并集
    - 差集
    - 子集
    - 超集

7. 面向对象

    {% asset_img oop-zhihu.png 面向对象的另类解释 %}

    表示属性时，大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻。

   ```python
    class Test:

        def __init__(self, foo):
        """构造器"""
        """定义函数的参数"""
            self.__foo = foo

        def __bar(self):
            print(self.__foo)
            print('__bar')

    def main():
        """入口函数"""
        test = Test('hello')
        test._Test__bar()
        print(test._Test__foo)

    if __name__ == "__main__":
        main()
        # test = Test('hello')
        # test._Test__bar()
        # print(test._Test__foo)
   ```

8. 类与对象
   简单的说，类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有点像用概念在解释概念，但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。

9. 类之间的关系
    简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。
        - is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
        - has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
        - use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。
    {% asset_img uml-components.png uml-components %}
    {% asset_img uml-example.png uml-example %}
10. 时间元组

    | 序号 | 属性    | 字段         | 值                                   |
    | ---- | ------- | ------------ | ------------------------------------ |
    | 0    | tm_year | 4位数年      | 2008                                 |
    | 1    | tm_mon  | 月           | 1 到 12                              |
    | 2    | tm_mday | 日           | 1到31                                |
    | 3    | tm_hour | 小时         | 0到23                                |
    | 4    | tm_min  | 分钟         | 0到59                                |
    | 5    | tm_sec  | 秒           | 0到61 (60或61 是闰秒)                |
    | 6    | tm_wday | 一周的第几日 | 0到6 (0是周一)                       |
    | 7    | tm_yday | 一年的第几日 | 1到366 (儒略历)                      |
    | 8    | tm_isdt | 夏令时       | -1, 0, 1, -1是决定是否为夏令时的旗帜 |

11. 使用``@property``
    Python内置的@property装饰器就是负责把一个方法变成属性调用
    ```python
    class Person(object):

        def __init__(self, name, age):
            self._name = name
            self._age = age

        # 访问器 - getter方法
        @property
        def name(self):
            return self._name

        # 访问器 - getter方法
        @property
        def age(self):
            return self._age

        # 修改器 - setter方法
        @age.setter
        def age(self, age):
            self._age = age

        def play(self):
            if self._age <= 16:
                print('%s正在玩飞行棋.' % self._name)
            else:
                print('%s正在玩斗地主.' % self._name)

    def main():
        person = Person('王大锤', 12)
        person.play()
        person.age = 22
        person.play()
        # person.name = '白元芳'  # AttributeError: can't set attribute

    if __name__ == '__main__':
        main()
    ```
    Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，那么如果想访问属性可以通过属性的`getter`（访问器）和`setter`（修改器）方法进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便。

12. 文件读写
    json模块主要有四个比较重要的函数，分别是：
        dump - 将Python对象按照JSON格式序列化到文件中
        dumps - 将Python对象处理成JSON格式的字符串
        load - 将文件中的JSON数据反序列化成对象
        loads - 将字符串的内容反序列化成Python对象
        
13. 文件读写模式

    | 操作模式 | 具体含义                         |
    | -------- | -------------------------------- |
    | `'r'`    | 读取 （默认）                    |
    | `'w'`    | 写入（会先截断之前的内容）       |
    | `'x'`    | 写入，如果文件已经存在会产生异常 |
    | `'a'`    | 追加，将内容写入到已有文件的末尾 |
    | `'b'`    | 二进制模式                       |
    | `'t'`    | 文本模式（默认）                 |
    | `'+'`    | 更新（既可以读又可以写）         |





 


[Python-100-Days](https://github.com/jackfrued/Python-100-Days.git)