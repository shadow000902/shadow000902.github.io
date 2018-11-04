---
title: Python基础知识整理
date: 2018-02-14 18:40:37
categories: [Python]
tags: [python]
---

#### 基础方法
##### 字符串大小写转换
```python
text.title()                # 首字母转大写
text.upper()                # 字符串转大写
text.lower()                # 字符串转小写
```

  <!--more-->

##### 对list进行排序
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))                             # 临时性字母正序排列
print(sorted(cars, reverse=True)                # 临时性字母倒叙排列
cars.sort()                                     # 永久性字母正序排列
cars.sort(reverse=True)                         # 永久性字母倒叙排列
print(cars)                                     # 默认排序
```

##### 访问list元素
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars[0])                                  # 访问第一个元素
# 当访问的list长度总是会变的情况下，可以使用这种方式访问list最后一个元素
print(cars[-1])                                 # 访问倒数第一个元素，即list最后一个元素
```

##### list中增删元素
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

##### 获取list长度
```python
len(cars)
```

##### 复制list
```python
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]                      # 复制整个列表以 [:] 来表示
```

##### 检查特定值是否在list中
```python
banned_users = ['andrew', 'carolina', 'david']
user1 = 'andrew'
user2 = 'and'
print(user1 in banned_users)                    # 返回true
print(user2 not in banned_users)                # 返回true
print(user1 not in banned_users)                # 返回false
print(user2 in banned_users)                    # 返回false
```

##### 在list中检索值
```bash
>>> a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
>>> a_list.count('new')       ①
2
>>> 'new' in a_list           ②
True
>>> a_list.index('mpilgrim')  ③
3
```

##### ``if``判断条件为``list``注意点
在判断条件为``list``时，如果``list``为空，即记过为``false``，只有在``list``有一个元素时，才为``true``。
```python
requested_toppings = []

if requested_toppings:
    print('requested_toppings not empty')
else:
    print('requested_toppings is empty')
```
这里实际执行的就是``else``中的语句，因为``requested_toppings``是空的，返回的``false``。

##### 多个``list``判断
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

##### 使用函数``range()``
```python
for value in range(1, 5):                       # 生成有序数值
    print(value)                                # 它只会打印4个数值，最后一个数值不会打印
num = list(range(1, 6))                         # 创建数值列表
print(num)                                      # 结果：[1, 2, 3, 4, 5]

even_num = list(range(2, 11, 2))                # 使用range()还可以指定步长
print(even_num)                                 # 结果：[2, 4, 6, 8, 10]
```

##### 对数值列表执行简单的统计计算
```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)                                     # 取最小值
max(digits)                                     # 取最大值
sum(digits)                                     # 求总和
```

##### **列表解析**
1. 复杂模式1
```python
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
```
2. 较复杂模式2
```python
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
```
3. 列表解析
```python
squares = [value**2 for value in range(1,11)]
print(squares)
```
要使用这种语法，首先指定一个描述性的列表名，如``squares``；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为``value**2``，它计算平方值。接下来，编写一个``for``循环，用于给表达式提供值，再加上右方括号。在这个示例中，``for``循环为``for value in range(1,11)``，它将值1~10提供给表达式``value**2``。请注意，这里的``for``语句末尾没有冒号。

##### 使用列表的一部分
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

##### 元组``tuple``
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

##### 集合``{ }``
一个简单的集合可以包含任何数据类型的值。如果有两个集合，则可以执行像联合、交集以及集合求差等标准集合运算。
1. 从list创建集合
```bash
>>> a_list = ['a', 'b', 'mpilgrim', True, False, 42]
>>> a_set = set(a_list)                           ①
>>> a_set                                         ②
# 集合是 无序的。该集合并不记得用于创建它的列表中元素的最初顺序。
{'a', False, 'b', True, 'mpilgrim', 42}
```
2. 创建空集合
```bash
# 要创建空集合，可不带参数调用 set() 。
>>> a_set = set()    ①
>>> a_set            ②
# 打印出来的空集合表现形式看起来有点儿怪。也许，您期望看到一个 {} 吧 ？该符号表示一个空的字典，而不是一个空的集合。
set()
>>> type(a_set)      ③
<class 'set'>
```
3. 修改集合
有两种方法可向现有集合中添加值： add() 方法和 update() 方法。
集合是装 唯一值 的袋子。如果试图添加一个集合中已有的值，将不会发生任何事情。将不会引发一个错误；只是一条空操作。

4. 从集合中删除元素
有三种方法可以用来从集合中删除某个值。前两种，discard() 和 remove() 有细微的差异。集合也有个 pop() 方法。
``pop()``方法从集合中删除某个值，并返回该值。然而，由于集合是无序的，并没有“最后一个”值的概念，因此无法控制删除的是哪一个值。它基本上是随机的。

5. 常见集合操作
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

##### 字典``dict``
字典 是键值对的无序集合。向字典添加一个键的同时，必须为该键增添一个值。（之后可随时修改该值。） Python 的字典为通过键获取值进行了优化，而不是反过来。
1. 修改字典
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

2. 混合值字典，value不为单个值
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

3. grades['']

  - 是否可迭代``Iterable``
  - 类似一个概念，实例才是可被CPU操作的，真实存在的东西。

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

  封装  访问限制

强制__init__(self, name, come_from)的属性不能被修改：
    __name
    __come_from
    
1.  封装 将类的属性私有化

2.  继承 

3.  多态 多种状态，接口多种不同实现方式即为多态


#### 解析
##### 处理文件和目录
``Python3``带有一个模块叫做``os``，代表``操作系统(operating system)``。``os``模块 包含非常多的函数用于获取(和修改)本地目录、文件进程、环境变量等的信息。
```python
import os
import glob
import humansize

pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
### 当前工作目录
# 获取当前工作目录
print(os.getcwd())

# 改变当前工作目录
os.chdir('/Users/pilgrim/diveintopython3/examples')

### 处理文件名和目录名
# os.path.join() 函数从一个或多个路径片段中构造一个路径名
print(os.path.join('/Users/pilgrim/diveintopython3/examples/', 'humansize.py'))

# 在和文件名拼接前，join函数给路径名添加一个额外的斜杠；无论你使用哪种形式的斜杠，Python 都可以访问到文件。
print(os.path.join('/Users/pilgrim/diveintopython3/examples', 'humansize.py'))

# 获取当前用户的Home目录
print(os.path.expanduser('~'))

# 分割完整路径名，目录名和文件名
os.path.split(pathname)
# 输出：('/Users/pilgrim/diveintopython3/examples', 'humansize.py')

(dirname, filename) = os.path.split(pathname)
# 将split函数的返回值赋值给一个二元组。每个变量获得了返回元组中的对应元素的值

(shortname, extension) = os.path.splitext(filename)
# 输出：('humansize', '.py')
# os.path.splitext() 函数，它分割一个文件名并返回短文件名和扩展名

### 罗列目录内容
# glob 模块是Python标准库中的另一个工具，它可以通过编程的方法获得一个目录的内容，并且它使用熟悉的命令行下的通配符。
glob.glob('examples/*.xml')
# 通配符是一个目录名加上 “*.xml”， 它匹配examples子目录下的所有.xml 文件

glob.glob('*test*.py')
# 在当前工作目录中找出所有扩展名为.py并且在文件名中包含单词test 的文件

metadata = os.stat('feed.xml')
# os.stat() 函数返回一个包含多种文件元信息的对象
metadata.st_mtime
# 返回最后修改时间，时间戳
metadata.st_size
# 返回文件的字节大小

humansize.approximate_size(metadata.st_size)
# 将st_size 属性作为参数传给approximate_size() 函数。

### 构建绝对路径
print(os.path.realpath('feed.xml'))
# 输出：/Users/pilgrim/diveintopython3/examples/feed.xml
# os.path.realpath()函数，返回当前文件或者目录的绝对路径
```

##### 列表解析
列表解析提供了一种紧凑的方式，实现了通过对列表中每一个元素应用一个函数的方法来将一个列表映射到另一个列表。
```python
import os, glob
import humansize

a_list = [1, 9, 8, 4]
a_list = [elem * 2 for elem in a_list]
# Python会在内存中构造新的列表，在列表解析完成后将结果赋值给原来的变量

glob.glob('*.xml')
# 输出：['feed-broken.xml', 'feed-ns0.xml', 'feed.xml']
[os.path.realpath(f) for f in glob.glob('*.xml')]
# 输出：['c:\\Users\\pilgrim\\diveintopython3\\examples\\feed-broken.xml','c:\\Users\\pilgrim\\diveintopython3\\examples\\feed-ns0.xml','c:\\Users\\pilgrim\\diveintopython3\\examples\\feed.xml']
[f for f in glob.glob('*.py') if os.stat(f).st_size > 6000]

# 列表解析并不限制表达式的复杂程度
[(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.xml')]
# 这个列表解析找到当前工作目录下的所有.xml文件， 对于每一个文件构造一个包含文件大小(通过调用os.stat()获得)和绝对路径(通过调用os.path.realpath())的元组。

[(humansize.approximate_size(os.stat(f).st_size), f) for f in glob.glob('*.xml')]
# 这个列表解析在前一个的基础上对每一个.xml文件的大小应用approximate_size()函数。
```

##### 字典解析
```python
# 列表解析
metadata = [(f, os.stat(f)) for f in glob.glob('*test*.py')]
# 字典解析
metadata_dict = {f:os.stat(f) for f in glob.glob('*test*.py')}
# 首先，它被花括号而不是方括号包围; 第二，对于每一个元素它包含由冒号分隔的两个表达式，而不是列表解析的一个。冒号前的表达式(在这个例子中是f)是字典的键;冒号后面的表达式(在这个例子中是os.stat(f))是值。

type(metadata_dict)
# 输出：<class 'dict'>

humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size) for f, meta in metadata_dict.items() if meta.st_size > 6000}

list(humansize_dict.keys())
# 获取key值，并生成list

# 交换字典的键和值
a_dict = {'a': 1, 'b': 2, 'c': 3}
{value:key for key, value in a_dict.items()}
# 输出：{1: 'a', 2: 'b', 3: 'c'}
```

##### 集合解析

集合也有自己的集合解析的语法。它和字典解析的非常相似，唯一的不同是集合只有值而没有键:值对。
```python
a_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{x for x in a_set if x % 2 == 0}
# 输出：{0, 8, 2, 4, 6}
# 同列表解析和字典解析一样， 集合解析也可以包含if 字句来在将元素放入结果集合前进行过滤。
```

#### 正则表达式

替换操作
```python
import re

s = '100 NORTH BROAD ROAD'

s[:-4] + s[-4:].replace('ROAD', 'RD.')
# 输出：'100 NORTH BROAD RD.'

# 正则表达式模块的re.sub()函数可以做字符串替换
re.sub('ROAD$', 'RD.', s)
# 输出：'100 NORTH BROAD RD.'
```

电话号码解析实例
```python
import re

# 电话号码样式：
    # 800-555-1212
    # 800 555 1212
    # 800.555.1212
    # (800) 555-1212
    # 1-800-555-1212
    # 800-555-1212-1234
    # 800-555-1212x1234
    # 800-555-1212 ext. 1234
    # work 1-(800) 555.1212 #1234

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
# 我们通常从左到右的阅读正则表达式。首先是匹配字符串开始位置，然后是(\d{3})。\d{3}表示什么意思？\d表示任意的数字（0到9），{3}表示一定要匹配3个数字。这个是你前面看到的{n,m}表示方法。把他们放在圆括号中，表示必须匹配3个数字，并且把他们记做一个组。分组的概念我们后面会说到。然后匹配一个连字符，接着匹配另外的3个数字，他们也同样作为一个组。然后又是一个连字符，后面还要准确匹配4个数字，他们也作为一位分组。最后匹配字符串结尾。

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
# 这个正则表达式和前面的一样。匹配了字符串开始位置，然后是一个三个数字的分组，接着一个连字符，又是一个三个数字的分组，又是一个连字符，然后一个四个数字的分组。这三个分组匹配的内容都会被记忆下来。和上面不同的是，这里多匹配了一个连字符以及一个分组，这个分组里的内容是匹配一个或更多个数字。最后是字符串结尾。

phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
# 注意了！你匹配了字符串开始，然后是3个数字的分组，接着是\D+，这是什么？好吧，\D匹配除了数字以外的任意字符，+的意思是一个或多个。因此\D+匹配一个或一个以上的非数字字符。这就是你用来替换连字符的东西，它用来匹配不同的分隔符。

phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# 这里和上面唯一不同的地方是，把所有的+换成了*。号码之间的分隔符不再用\D+来匹配，而是使用\D*。还记得+表示一个或更多吧？好，现在可以解析号码之间没有分隔符的情况了。

phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# 现在除了在第一个分组之前要用\d*匹配0个或更多非数字字符外，这和前面的例子是相同的。注意你不会对这些非数字字符分组，因为他们不在圆括号内，也就是说不是一个组。如果发现有这些字符，这里只是跳过他们，然后开始对后面的区域码匹配、分组。

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# 注意正则表达式没有^。不会再匹配字符串开始位置了。正则表达式不会匹配整个字符串，而是试图找到一个字符串开始匹配的位置，然后从这个位置开始匹配。

# 最终匹配的正则表达式：
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
```

到此应该熟悉了下面的技巧：
```bash
^         # 匹配字符串开始位置。
$         # 匹配字符串结束位置。
\b        # 匹配一个单词边界。
\d        # 匹配一个数字。
\D        # 匹配一个任意的非数字字符。
x?        # 匹配可选的x字符。换句话说，就是0个或者1个x字符。
x*        # 匹配0个或更多的x。
x+        # 匹配1个或者更多x。
x{n,m}    # 匹配n到m个x，至少n个，不能超过m个。
(a|b|c)   # 匹配单独的任意一个a或者b或者c。
(x)       # 这是一个组，它会记忆它匹配到的字符串。你可以用re.search返回的匹配对象的groups()函数来获取到匹配的值。
```

#### 闭合和生成器

##### 正则表达式使用

```python
import re
re.sub('([^aeiou])y$', r'\1ies', 'vacancy')
# 该分组用于保存字母 y 之前的字符。然后在替换字符串中，用到了新的语法： \1，它表示“嘿，记住的第一个分组呢？把它放到这里。”在此例中， 记住了 y 之前的 c ，在进行替换时，将用 c 替代 c，用 ies 替代 y 。（如果有超过一个的记忆分组，可以使用 \2 和 \3 等等。）
```





[深入python3](https://woodpecker.org.cn/diveintopython3/index.html)