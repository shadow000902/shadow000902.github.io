---
title: Python基础知识整理
date: 2018-02-14 18:40:37
categories: [Python]
tags: [python]
---

#### 基础方法
  字符串大小写转换
```python
text.title()                # 首字母转大写
text.upper()                # 字符串转大写
text.lower()                # 字符串转小写
```

  <!--more-->

  对list进行排序
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))                             # 临时性字母正序排列
print(sorted(cars, reverse=True)                # 临时性字母倒叙排列
cars.sort()                                     # 永久性字母正序排列
cars.sort(reverse=True)                         # 永久性字母倒叙排列
print(cars)                                     # 默认排序
```

  访问list元素
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars[0])                                  # 访问第一个元素
# 当访问的list长度总是会变的情况下，可以使用这种方式访问list最后一个元素
print(cars[-1])                                 # 访问倒数第一个元素，即list最后一个元素
```

  list中增删元素
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)               # 根据值删除元素
motorcycles.append(too_expensive)               # 增加元素，元素增加到末尾
motorcycles.insert(0, too_expensive)            # 指定位置插入元素
del motorcycles[1]                              # 删除指定位置元素
motorcycles.pop()                               # 取出list中的最后一个元素
print(motorcycles)
```

  获取list长度
```python
len(cars)
```

  复制list
```python
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]                      # 复制整个列表以 [:] 来表示
```

  检查特定值是否在list中
```python
banned_users = ['andrew', 'carolina', 'david']
user1 = 'andrew'
user2 = 'and'
print(user1 in banned_users)                    # 返回true
print(user2 not in banned_users)                # 返回true
print(user1 not in banned_users)                # 返回false
print(user2 in banned_users)                    # 返回false
```

  在list中检索值
```bash
>>> a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
>>> a_list.count('new')       ①
2
>>> 'new' in a_list           ②
True
>>> a_list.index('mpilgrim')  ③
3
```

  ``if``判断条件为``list``注意点
在判断条件为``list``时，如果``list``为空，即记过为``false``，只有在``list``有一个元素时，才为``true``。
```python
requested_toppings = []

if requested_toppings:
    print('requested_toppings not empty')
else:
    print('requested_toppings is empty')
```
这里实际执行的就是``else``中的语句，因为``requested_toppings``是空的，返回的``false``。

  多个``list``判断
```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
    print("\nFinished making your pizza!")
```

  使用函数``range()``
```python
for value in range(1, 5):                       # 生成有序数值
    print(value)                                # 它只会打印4个数值，最后一个数值不会打印
num = list(range(1, 6))                         # 创建数值列表
print(num)                                      # 结果：[1, 2, 3, 4, 5]

even_num = list(range(2, 11, 2))                # 使用range()还可以指定步长
print(even_num)                                 # 结果：[2, 4, 6, 8, 10]
```

  对数值列表执行简单的统计计算
```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)                                     # 取最小值
max(digits)                                     # 取最大值
sum(digits)                                     # 求总和
```

  **列表解析**
 - 复杂模式1
```python
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
```
 - 较复杂模式2
```python
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
```
 - 列表解析
```python
squares = [value**2 for value in range(1,11)]
print(squares)
```
要使用这种语法，首先指定一个描述性的列表名，如``squares``；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为``value**2``，它计算平方值。接下来，编写一个``for``循环，用于给表达式提供值，再加上右方括号。在这个示例中，``for``循环为``for value in range(1,11)``，它将值1~10提供给表达式``value**2``。请注意，这里的``for``语句末尾没有冒号。

  使用列表的一部分
定义列表后，可从其中获取任何部分作为新列表。该技术称为对列表进行``切片``。
```bash
>>> a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
>>> a_list[1:3]            ①
# ① 通过指定两个索引值，可以从列表中获取称作“切片”的某个部分。返回值是一个新列表，它包含列表(??切片)中所有元素，按顺序从第一个切片索引开始（本例中为 a_list[1]），截止但不包含第二个切片索引（本例中的 a_list[3]）。
['b', 'mpilgrim']
>>> a_list[1:-1]           ②
# ② 如果切片索引之一或两者均为负数，切片操作仍可进行。如果有帮助的话，您可以这么思考：自左向右读取列表，第一个切片索引指明了想要的第一个元素，第二个切片索引指明了第一个不想要的元素。返回值是两者之间的任何值。 between.
['b', 'mpilgrim', 'z']
>>> a_list[0:3]            ③
# ③ 列表是以零为起点的，因此 a_list[0:3] 返回列表的头三个元素，从 a_list[0] 开始，截止到但不包括 a_list[3] 。
['a', 'b', 'mpilgrim']
>>> a_list[:3]             ④
# ④ 如果左切片索引为零，可以将其留空而将零隐去。因此 a_list[:3] 与 a_list[0:3] 是完全相同的，因为起点 0 被隐去了。
['a', 'b', 'mpilgrim']
>>> a_list[3:]             ⑤
# ⑤ 同样，如果右切片索引为列表的长度，也可以将其留空。因此 a_list[3:] 与 a_list[3:5] 是完全相同的，因为该列表有五个元素。此处有个好玩的对称现象。在这个五元素列表中， a_list[:3] 返回头三个元素，而 a_list[3:] 返回最后两个元素。事实上，无论列表的长度是多少, a_list[:n] 将返回头 n 个元素，而 a_list[n:] 返回其余部分。
['z', 'example']
>>> a_list[:]              ⑥
# ⑥ 如果两个切片索引都留空，那么将包括列表所有的元素。但该返回值与最初的 a_list 变量并不一样。它是一个新列表，只不过恰好拥有完全相同的元素而已。a_list[:] 是对列表进行复制的一条捷径。
['a', 'b', 'mpilgrim', 'z', 'example']
```

  元组``tuple``
元组：是不可变的列表。一旦创建之后，用任何方法都不可以修改元素。
```bash
>>> a_tuple = ("a", "b", "mpilgrim", "z", "example")
# 负的索引从元组的尾部开始计数，这和列表也是一样的。
>>> a_tuple[-1]
'example'
>>> a_tuple[1:3]
# 和列表一样，元组也可以进行切片操作。对列表切片可以得到新的列表；对元组切片可以得到新的元组。
('b', 'mpilgrim')
```

元组和列表的主要区别是元组不能进行修改。用技术术语来说，元组是``不可变更``的。从实践的角度来说，没有可用于修改元组的方法。列表有像``append()``、``extend()``、``insert()``、``remove()``和``pop()``这样的方法。这些方法，元组都没有。可以对元组进行切片操作（因为该方法创建一个新的元组），可以检查元组是否包含了特定的值（因为该操作不修改元组），还可以……就那么多了。
元组有什么好处:
 - 元组的速度比列表更快。如果定义了一系列常量值，而所需做的仅是对它进行遍历，那么请使用元组替代列表。
 - 对不需要改变的数据进行“写保护”将使得代码更加安全。使用元组替代列表就像是有一条隐含的 assert 语句显示该数据是常量，特别的想法（及特别的功能）必须重写。（？？）
 - 一些元组可用作字典键（特别是包含字符串、数值和其它元组这样的不可变数据的元组）。列表永远不能当做字典键使用，因为列表不是不可变的。

元组可转换成列表，反之亦然。内建的``tuple()``函数接受一个列表参数，并返回一个包含同样元素的元组，而``list()``函数接受一个元组参数并返回一个列表。从效果上看，``tuple()``冻结列表，而``list()``融化元组。

  集合``{ }``
一个简单的集合可以包含任何数据类型的值。如果有两个集合，则可以执行像联合、交集以及集合求差等标准集合运算。
 - 从list创建集合
```bash
>>> a_list = ['a', 'b', 'mpilgrim', True, False, 42]
>>> a_set = set(a_list)                           ①
>>> a_set                                         ②
# 集合是 无序的。该集合并不记得用于创建它的列表中元素的最初顺序。
{'a', False, 'b', True, 'mpilgrim', 42}
```
 - 创建空集合
```bash
# 要创建空集合，可不带参数调用 set() 。
>>> a_set = set()    ①
>>> a_set            ②
# 打印出来的空集合表现形式看起来有点儿怪。也许，您期望看到一个 {} 吧 ？该符号表示一个空的字典，而不是一个空的集合。
set()
>>> type(a_set)      ③
<class 'set'>
```
 - 修改集合
有两种方法可向现有集合中添加值： add() 方法和 update() 方法。
集合是装 唯一值 的袋子。如果试图添加一个集合中已有的值，将不会发生任何事情。将不会引发一个错误；只是一条空操作。

 - 从集合中删除元素
有三种方法可以用来从集合中删除某个值。前两种，discard() 和 remove() 有细微的差异。集合也有个 pop() 方法。
``pop()``方法从集合中删除某个值，并返回该值。然而，由于集合是无序的，并没有“最后一个”值的概念，因此无法控制删除的是哪一个值。它基本上是随机的。

 - 常见集合操作
```bash
>>> a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
# ① 要检测某值是否是集合的成员，可使用 in 运算符。其工作原理和列表的一样。
>>> 30 in a_set                                                     ①
True
>>> 31 in a_set
False
>>> b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
>>> a_set.union(b_set)                                              ②
# ② union() 方法返回一个新集合，其中装着 在两个 集合中出现的元素。
{1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}
>>> a_set.intersection(b_set)                                       ③
# ③ intersection() 方法返回一个新集合，其中装着 同时 在两个集合中出现的所有元素。
{9, 2, 12, 5, 21}
>>> a_set.difference(b_set)                                         ④
# ④ difference() 方法返回的新集合中，装着所有在 a_set 出现但未在 b_set 中的元素。
{195, 4, 76, 51, 30, 127}
>>> a_set.symmetric_difference(b_set)                               ⑤
# ⑤ symmetric_difference() 方法返回一个新集合，其中装着所有 只在其中一个 集合中出现的元素。
{1, 3, 4, 6, 8, 76, 15, 17, 18, 195, 127, 30, 51}
```

  字典``dict``
字典 是键值对的无序集合。向字典添加一个键的同时，必须为该键增添一个值。（之后可随时修改该值。） Python 的字典为通过键获取值进行了优化，而不是反过来。
 - 修改字典
```bash
>>> a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
>>> a_dict['database'] = 'blog'  ①
# ① 在字典中不允许有重复的键。对现有的键赋值将会覆盖旧值。
>>> a_dict
{'server': 'db.diveintopython3.org', 'database': 'blog'}
>>> a_dict['user'] = 'mark'      ②
# ② 可随时添加新的键值对。该语法与修改现有值相同。
>>> a_dict                       ③
# ③ 新字典项（键为 'user'，值为 'mark'）出现在中间。事实上，在第一个例子中字典项按顺序出现是个巧合；现在它们不按顺序出现同样也是个巧合。
{'server': 'db.diveintopython3.org', 'user': 'mark', 'database': 'blog'}
>>> a_dict['user'] = 'dora'      ④
# ④ 对既有字典键进行赋值只会用新值替代旧值。
>>> a_dict
{'server': 'db.diveintopython3.org', 'user': 'dora', 'database': 'blog'}
>>> a_dict['User'] = 'mark'      ⑤
# ⑤ 该操作会将 user 键的值改回 "mark" 吗？不会！仔细看看该键——有个大写的 U 出现在 "User" 中。字典键是区分大小写的，因此该语句创建了一组新的键值对，而不是覆盖既有的字典项。对你来说它们可能是一样的，但对于 Python 而言它们是完全不同的。
>>> a_dict
{'User': 'mark', 'server': 'db.diveintopython3.org', 'user': 'dora', 'database': 'blog'}
```

 - 混合值字典，value不为单个值
字典并非只能用于字符串。字典的值可以是任何数据类型，包括整数、布尔值、任何对象，甚至是其它的字典。而且就算在同一字典中，所有的值也无须是同一类型，您可根据需要混合匹配。字典的键要严格得多，可以是字符串、整数和其它一些类型。在同一字典中也可混合、匹配使用不同数据类型的键。
```bash
>>> SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
...             1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
>>> len(SUFFIXES)      ①
# ① 类似 列表 和 集合 ，len() 函数将返回字典中键的数量。
2
>>> 1000 in SUFFIXES   ②
# ② 而且像列表和集合一样，可使用 in 运算符以测试某个特定的键是否在字典中。
True
>>> SUFFIXES[1000]     ③
# ③ 1000 是 字典 SUFFIXES 的一个键；其值为一个 8 元素列表（确切地说，是 8 个字符串）。
['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
>>> SUFFIXES[1024]     ④
# ④ 同样， 1024 是字典 SUFFIXES 的键；其值也是一个 8 元素列表。
['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
>>> SUFFIXES[1000][3]  ⑤
# ⑤ 由于 SUFFIXES[1000] 是列表，可以通过它们的 0 基点索引来获取列表中的单个元素。
'TB'
```


  grades['']

1.  是否可迭代``Iterable``

2.  类似一个概念，实例才是可被CPU操作的，真实存在的东西。

```python
class People():
    def __init__(self):
        pass
    def have_some_food(self):
        print('Delicious!')
        
    def hava_a_drink(self):
        print('Thanks!')

if __name__ == '__main__':
    me = People()
    you = People()
    me.have_some_food()
    me.hava_a_drink()
```

15. 封装  访问限制

强制__init__(self, name, come_from)的属性不能被修改：
    __name
    __come_from
    
16. 封装 将类的属性私有化

17. 继承 

18. 多态 多种状态，接口多种不同实现方式即为多态


