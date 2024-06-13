---
layout:     post
title:      "Python基本知识"
date:       2024-06-12 09:51:50
author:     "Bert"
header-style: text
tags:
  - Python
---

**Overview**

由于工作需要, 需要给`FAE`培训`python`的基础知识. 回顾自己的`python`历程, 没有系统的学习过`python`的语法, 都是要用到某个功能时, 通过`某度`或者`Chatgpt`获取所需的代码. 正好借助这个机会系统梳理下`python`的基础知识.



## Python基础

### Python简介

`Python`是一种高级**脚本**语言, 越高级的语言其`封装性`越好(用较小的代码, 即可实现较多的功能), 往往越容易入门.

`Python`的底层使用`C`语言设计, 具有很强的`可读性`,  虽然是一种强类型的语言(语法要求严格, 比如空格缩进要求等), 但是其入门比其它语言更简单, 以至于业界流传「懂英文, 就懂`Python`」.

**`Python`语言具有如下特性:**

+ **解释性**: 对开发者来说, 不需要编译, 开发完成直接可以运行.
+ **交互式**: `Python`提供了交互式的环境, 在命令行终端上直接执行`python`, 即可使用交互式方式执行代码.
+ **面向对象**: `Python`支持面向对象思想编程.



### Python环境搭建

`Python`官网下载: https://www.python.org/downloads/.



选择目标版本安装即可.

### Python Docs

`Python` Docs: https://docs.python.org/3/.



### Python运行

`Python`是一种跨平台语言, 即同一份代码, 可以在Windows或者Linux上运行, 程序员不需要关心平台的差异.

虽然从使用者的角度看, `Python`代码不需要编译, 直接可以运行. 但是从`Python`的内部执行过程中, 会先讲`.py`文件中的源代码编译成`字节码`(byte code), 然后再由`Python Virtual Machine`来进一步编译链接`字节码`成各个平台的机器码.

`Python字节码` 往往以`.pyc`的方式存在, 在python运行时, `Python脚本解释器`会根据代码中`import`来判断是否在`__pycache__`文件夹中生成`.pyc`文件.

> 目前有很多工具(比如`Python`自带的`uncompyle6`)可以反汇编`.pyc`成`.py`.

使用`.pyc`的最大作用是加快模块的导入, 也可以在编译时使用`Python -O`编译成`.pyo`格式. `.pyo`其也是`字节码`方式, 区别于`.pyc`, `.pyo`做了额外的优化, 去掉了`字节码`中的不必要信息, 减少了文件大小, 加快加载速度.

BTW. 还有另外一种`.pyd`格式, `.pyd`是已经在平台上编译打包而成的`机器码`. 虽然不能跨平台使用, 但是已经是`机器码`方式, 加载和运行速度会更快, 还有一种好处就是`.pyd`反汇编难度大大增加, 很难有现有的工具可以直接转成`.py`.



### Python基础语法

#### Python标识符

`Python标识符`(变量或函数命名)规则如下:

+ 区分大小写.
+ 可以包含英文, 数字以及下划线(_)组成, 但不能以数字开头, 也不能包含特殊符号.

以下划线(_)开头的标识符约定俗成规则:

| 下划线(_)开头组合           | 说明                                          |
| --------------------------- | --------------------------------------------- |
| 单下划线开头`_foo`          | 用于模块或者类内部, 不应该被模块外部直接访问. |
| 双下划线开头`__foo`         | 用于类的私有成员                              |
| 双下划线开头和结尾`__foo__` | 用于特殊方法专用标识.                         |

#### Python关键字

下面说明了`Python关键字`, 这些`关键字`不能用作`标识符`使用.

```python
and, exec, not, assert, finally, or, break, for, pass, class, from, print,
continue, global, raise, def, if, return, del, import, try, elif, in, while,
else, is, with, except, lambda, yield
```

#### Python行缩进

`Python`使用`行缩进`方式来表示一个代码块.

`行缩进`可以使用如下方式, 但是不能混用, **必须严格执行**.

+ 使用`TAB`
+ 使用2个`空格`
+ 使用4个`空格`

#### Python注释

`Python`使用`#`作为单行注释.

```python
#!/usr/bin/python
print('hello world') #打印
```

#### Python引号

`Python`使用`'`和`"`来定义`单行字符串`, 两者功能是等价的.

`Python`使用`'''`或者`"""`来表示多行字符串.

```python
line_string='hello string'

multi_line_string='''This is a string
that spans multiple lines
using triple single quotes.'''
```

#### Python打印

`Python`使用`print()`来打印变量.

`print`在调试过程中往往比较重要, 以下是常用的用法:

1. 分隔符(`sep`参数)

   默认情况, `print()`使用空格作为多个参数之间的分隔符, 通过`sep`参数可以自定义这个分隔符:

   ```python
   print('hello', 'world', sep='-') #输出: hello-world
   ```

2. 结束符(end参数)

   `print()`默认以换行符(`\n`)结束输出, 可以通过`end`参数修改这个行为:

   ```python
   print('hello', end=' ') #将'\n'替换为' '
   print('world')
   #输出: hello world
   ```

3. `f-string`格式化

   使用`{}`包裹变量或表达式, 实现快速且易读的字符串格式化:

   ```python
   name='Alice'
   age=30
   print(f'{name} is {age} years old.')
   #输出: Alice is 30 years old.
   ```

4. `str.format()`格式化

   这是一种较老但仍然强大的格式化方法, 允许更复杂的值替换和格式化:

   ```python
   print("The number {0} is less than {1}".format(1, 2))
   # 输出：The number 1 is less than 2
   ```

5. `%`格式化

   一种旧式的字符串格式化方法，类似于 C 语言中的 `printf`：

   ```python
   name = "Bob"
   age = 25
   print("%s is %d years old." % (name, age))
   # 输出：Bob is 25 years old.
   ```

6. 打印到文件

   默认情况下，`print()` 将内容输出到标准输出（通常是控制台）。通过 `file` 参数，可以将输出重定向到其他地方，例如文件：

   ```python
   with open('output.txt', 'w') as f:
       print('Hello file!', file=f)
   ```

### Python变量类型

`Python` 是一种动态类型的编程语言，这意味着在编写代码时**不需要声明变量的类型**。变量的类型是在运行时自动确定的。下面是 `Python` 中一些最常见的变量类型：

1. **整数（Integers）** - 这是用于表示整数的数据类型，例如：`1`, `100`, `-10`。
2. **浮点数（Floats）** - 用于表示带有小数的数字，例如：`1.0`, `3.14159`, `-0.01`。
3. **字符串（Strings）** - 用于表示文本数据，例如：`"hello"`, `"Python123"`。字符串在 Python 中是不可变的，这意味着一旦创建，它们的内容不能被修改。
4. **布尔值（Booleans）** - 代表逻辑值 True 或 False。
5. **列表（Lists）** - 用于存储一系列的元素。**列表是可变的**，可以包含不同类型的数据，例如：`[1, 2, 3]`, `["apple", "banana", "cherry"]`。
6. **元组（Tuples）** - 类似于列表，**但是它们是不可变的**。一旦创建，就不能更改，例如：`(1, 2, 3)`, `("a", "b", "c")`。
7. **字典（Dictionaries）** - 存储**键值对{key: value}**的数据结构。字典允许使用键来快速检索、添加、修改或删除数据，例如：`{"name": "John", "age": 30}`。
8. **集合（Sets）** - 无序的集合类型，不允许重复元素，适合进行集合操作，如并集、交集、差集等，例如：`{1, 2, 3}`。

Python 还支持更复杂的数据类型，如类（用于面向对象编程）和各种自定义数据类型。此外，标准库和第三方库提供了更多专用的数据类型，如 `NumPy` 的`数组`和 `Pandas` 的 `DataFrame`，这些都是数据科学中常用的类型。

### Python运算符

`Python` 中的运算符可以分为几个主要类别，用于执行数学运算、比较操作、逻辑操作、位运算等。下面是每类运算符的详细介绍：

1. **算术运算符**

这些运算符用于执行基本的数学计算：

- `+`：加法，例如 `a + b`
- `-`：减法，例如 `a - b`
- `*`：乘法，例如 `a * b`
- `/`：除法，返回浮点数，例如 `a / b`
- `//`：整除，返回商的整数部分，例如 `a // b`
- `%`：模运算，返回除法的余数，例如 `a % b`
- `**`：幂运算，返回一个数的指数次幂，例如 `a ** b`

2. **比较运算符**

这些运算符用于比较两个值之间的关系：

- `==`：等于，判断两个值是否相等
- `!=`：不等于，判断两个值是否不相等
- `>`：大于
- `<`：小于
- `>=`：大于或等于
- `<=`：小于或等于

3. **逻辑运算符**

用于布尔（逻辑）值之间的运算：

- `and`：逻辑与，如果两边的操作数都是 True，则结果为 True
- `or`：逻辑或，如果至少有一个操作数是 True，则结果为 True
- `not`：逻辑非，如果操作数为 True，则结果为 False

4. **位运算符**

在整数的位级进行操作：

- `&`：按位与
- `|`：按位或
- `^`：按位异或
- `~`：按位取反
- `<<`：左移
- `>>`：右移

5. **赋值运算符**

用于给变量赋值：

- `=`：基本赋值运算符，如 `a = b`
- `+=`：加后赋值，如 `a += b`（等同于 `a = a + b`）
- `-=`：减后赋值，如 `a -= b`
- `*=`：乘后赋值，如 `a *= b`
- `/=`：除后赋值，如 `a /= b`
- `%=`：模后赋值，如 `a %= b`
- `**=`：幂后赋值，如 `a **= b`
- `//=`：整除后赋值，如 `a //= b`

6. **成员运算符**

用于测试序列（列表、元组等）中是否包含指定的值：

- `in`：如果指定的值在序列中，则返回 True
- `not in`：如果指定的值不在序列中，则返回 True

7. 身份运算符

用于比较两个对象的存储单元：

- `is`：判断两个标识符是不是引用自一个对象
- `is not`：判断两个标识符是不是引用自不同对象

### Python条件语句

在 Python 中，条件语句是控制程序流程的基本结构之一，用于基于一定条件执行特定代码块。Python 的条件语句主要有三种形式：`if`、`elif`和`else`。

1. **`if` 语句**

`if` 语句是最基本的条件语句，用来执行一个条件为真时的代码块。

```python
if 条件:
    # 条件为 True 时执行的代码
```

例如：

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

2. **`elif` 语句**

`elif`（即 else if 的简写）用于检查多个表达式是否为真，并在前面的 `if` 或 `elif` 语句后执行一个为真的代码块。

```python
if 条件1:
    # 条件1为 True 时执行的代码
elif 条件2:
    # 条件2为 True 时执行的代码
```

例如：

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
```

3. **`else` 语句**

`else` 语句用于当所有 `if` 和 `elif` 中的条件都不为真时执行的代码块。

```python
if 条件:
    # 条件为 True 时执行的代码
else:
    # 所有条件都不为 True 时执行的代码
```

**例如：**

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

**组合使用**

`if`、`elif` 和 `else` 语句可以灵活组合使用，以处理多种逻辑情况。

```python
pythonx = 20
if x > 30:
    print("x is greater than 30")
elif x > 20:
    print("x is greater than 20 but not greater than 30")
elif x > 10:
    print("x is greater than 10 but not greater than 20")
else:
    print("x is 10 or less")
```

**嵌套条件**

条件语句可以嵌套使用，即在一个条件语句内部使用另一个条件语句。

```python
pythonx = 10
if x > 5:
    if x > 7:
        print("x is greater than 7")
    else:
        print("x is greater than 5 but not greater than 7")
else:
    print("x is 5 or less")
```

这种结构虽然可以处理更复杂的逻辑，但应谨慎使用以避免过度嵌套导致代码难以理解和维护。总的来说，`Python` 的条件语句是编写决策逻辑的重要工具，它的语法简洁明了，易于理解和使用。

### Python循环语句

在` Python` 中，循环语句允许我们执行一个代码块多次，这通常用于遍历数据结构中的元素或者重复执行某个操作直到满足特定条件。Python 主要提供了两种类型的循环语句：`for` 循环和 `while` 循环。

1. **`for` 循环**

`for` 循环在 Python 中用于迭代一个序列（如列表、元组、字典、集合或字符串）中的每个元素。

 **基本语法**

```python
for 变量 in 序列:
    # 执行的代码块
```

 **示例:**

```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for letter in 'hello':
    print(letter)
```

 **使用 `range()`:**

`range()` 函数常用于生成一个整数序列，与 `for` 循环结合使用，可以执行指定次数的循环。

```python
# 使用 range() 进行循环
for i in range(5):
    print(i)  # 打印 0 到 4
```

2. **`while` 循环**

`while` 循环允许执行一个代码块，只要循环的条件为真。

 **基本语法**

```python
while 条件:
    # 执行的代码块
```

 **示例:**

```python
# 当条件为真时循环执行
x = 0
while x < 5:
    print(x)
    x += 1
```

 **循环控制语句**

在循环中，你可能需要提前退出循环或者跳过某次循环迭代。`Python` 提供了一些控制语句来处理这些情况：

- `break`：退出循环。
- `continue`：跳过当前循环的剩余部分，并开始下一次迭代。
- `else`：可以与 `for` 或 `while` 循环一起使用，当循环正常结束时（没有触发 `break`）执行的代码块。

 **使用 `break` 和 `continue`:**

```python
# 使用 break 退出循环
for i in range(10):
    if i == 5:
        break
    print(i)  # 打印 0 到 4

# 使用 continue 跳过迭代
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 打印 1, 3, 5, 7, 9
```

 **使用 `else`:**

```python
# 循环结束时执行 else 块
for i in range(5):
    print(i)
else:
    print("Finished looping")
```

在 `Python` 中，循环语句的灵活性和简洁性使得处理各种迭代任务变得容易。通过结合使用 `for` 循环、`while` 循环和各种循环控制语句，你可以有效地控制程序的执行流程。

### Python字符串

在 `Python` 中，字符串是不可变的序列数据类型，用于存储文本信息。字符串可以用单引号（`'`）、双引号（`"`）或三引号（`'''` 或 `"""`）括起来。使用三引号可以定义多行字符串。

**访问字符串中的字符**

可以通过索引访问字符串中的单个字符。索引从 `0` 开始。

```python
s = 'Hello'
print(s[1])  # 输出 'e'
```

**字符串切片**

切片用于获取字符串的一部分。

```python
s = 'Hello, World!'
print(s[0:5])  # 输出 'Hello'
print(s[7:])   # 输出 'World!'
```

**常用字符串方法**

`Python` 字符串对象提供了许多用于常见文本处理任务的方法。

- `str.lower()` 或 `str.upper()`：返回字符串的小写或大写形式。

```python
print("HELLO".lower())  # 输出 'hello'
print("world".upper())  # 输出 'WORLD'
```

- `str.strip()`：去除字符串前后的空白字符。

```python
print("   hello   ".strip())  # 输出 'hello'
```

- `str.split()`：按照指定的分隔符将字符串分割成一个列表。

```python
print("a,b,c".split(','))  # 输出 ['a', 'b', 'c']
```

- `str.join()`：将序列中的元素以指定的字符连接生成一个新的字符串。

```python
print("-".join(["2023", "06", "12"]))  # 输出 '2023-06-12'
```

- `str.find()` 和 `str.replace()`：搜索子字符串及替换。

```python
s = "hello world"
print(s.find("world"))  # 输出 6
print(s.replace("world", "Python"))  # 输出 'hello Python'
```

**字符串不可变性**

在 `Python` 中，字符串是不可变的。这意味着一旦创建了一个字符串，就不能修改它的任何部分。尝试改变字符串的操作实际上会创建一个新的字符串。

**字符串和字节流相互转换**

在 `Python` 中，字符串（`String`）和字节流（`bytes`）是两种不同的数据类型，但它们之间可以相互转换。`字符串`通常用于**处理文本信息**，而`字节流`用于**处理二进制数据**，如文件数据或网络传输的原始数据。

+ **字符串转换为字节流**

要将`字符串`转换为`字节流`，你可以使用字符串的 `encode()` 方法。这个方法将字符串编码为字节，默认使用 `UTF-8` 编码，但你也可以指定其他编码方式。编码是将人类可读的字符串转换为计算机可存储和传输的二进制格式。

```python
s = "hello world"
bytes_data = s.encode()  # 默认使用UTF-8编码
bytes_data_utf16 = s.encode('utf-16')  # 使用UTF-16编码

print(bytes_data)  # 输出 b'hello world'
print(bytes_data_utf16)  # 输出 b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 \x00w\x00o\x00r\x00l\x00d\x00'
```

+ **字节流转换为字符串**

要将`字节流`转换回`字符串`，可以使用字节流对象的 `decode()` 方法。这个方法将字节流解码成字符串，同样默认使用 UTF-8 编码，但同样可以指定其他编码方式。解码是将二进制格式转换回人类可读的文本格式。

```python
bytes_data = b'hello world'
s = bytes_data.decode()  # 默认使用UTF-8解码
s_utf16 = bytes_data_utf16.decode('utf-16')  # 使用UTF-16解码

print(s)  # 输出 'hello world'
print(s_utf16)  # 输出 'hello world'
```

这种能力，即在字符串和字节流之间转换，是处理文件、网络通信等需要在文本和二进制数据之间切换的场景中非常重要的。

### Python列表

在 `Python` 中，`列表`（`list`）是一种非常灵活的数据结构，用于存储一系列的项目。**列表是可变的**，这意味着你可以**添加、移除或更改**`列表`中的元素。这使得列表成为非常强大和常用的数据类型之一。

**创建列表**

`列表`可以通过将元素放置在方括号 `[]` 中，用逗号分隔来创建。

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Hello", True, 3.14]
empty_list = []
```

**访问列表元素**

你可以通过索引来访问`列表`中的元素，索引从 `0` 开始。

```python
print(fruits[0])  # 输出 'apple'
print(numbers[1])  # 输出 2
```

**负数索引**可以用于从列表末尾开始访问元素，例如 `-1` 是最后一个元素的索引。

```python
print(fruits[-1])  # 输出 'cherry'
```

**修改列表元素**

你可以通过指定索引来修改`列表`中的元素。

```python
fruits[0] = "orange"
print(fruits)  # 输出 ['orange', 'banana', 'cherry']
```

**添加和移除元素**

- 使用 `append()` 方法在列表末尾添加元素。
- 使用 `insert()` 方法在指定位置插入元素。
- 使用 `remove()` 方法移除第一个匹配的元素。
- 使用 `pop()` 方法移除指定位置的元素，默认为最后一个。

```python
fruits.append("mango")
fruits.insert(1, "blueberry")
fruits.remove("banana")
popped_element = fruits.pop()  # 移除最后一个元素
print(fruits)  # 输出 ['orange', 'blueberry', 'cherry']
```

**列表切片**

`列表`切片允许你访问列表的一个子集。你可以指定起始和结束索引以及步长。

```python
numbers=[1, 2, 3, 4, 5]
print(numbers[1:4])  # 输出 [2, 3, 4]
print(numbers[:3])  # 输出 [1, 2, 3]
print(numbers[::2])  # 输出 [1, 3, 5]
```

**列表的遍历**

你可以使用 `for` 循环遍历列表中的每个元素。

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**列表推导**

`列表`推导提供了一种**简洁**的方式来创建列表。它通常用于从其他列表中生成新列表。

```python
squares = [x**2 for x in range(6)]
print(squares)  # 输出 [0, 1, 4, 9, 16, 25]
```

`列表`是 `Python` 编程中非常核心的部分，它们提供了强大的方式来组织和处理数据。

### Python元组

`Python` 中的`元组`（`tuple`）是一种不可变的序列类型，这意味着**一旦元组被创建，它的内容就不能被修改**。`元组`常用于存放一个**不应改变的数据集合**。`元组`的使用和`列表`非常相似，但元组由圆括号 `()` 包围，而`列表`由方括号 `[]` 包围。

**创建元组**

`元组`可以通过将元素放入圆括号中，元素之间用逗号分隔来创建。实际上，圆括号是可选的，关键是元素后的逗号。

```python
my_tuple = (1, 2, 3)
single_element_tuple = (4,)  # 单元素元组需要在元素后加逗号
no_parentheses = 5, 6, 7  # 圆括号是可选的
empty_tuple = ()
```

**访问元组元素**

访问`元组`中的元素的方式与访问列表的方式相同，使用索引：

```python
print(my_tuple[0])  # 输出 1
print(my_tuple[-1])  # 输出 3
```

**不可变性**

由于`元组`是不可变的，你不能修改元组中的元素：

```python
# my_tuple[0] = 10  # 这将引发一个TypeError
```

尽管`元组`本身是不可变的，但如果它包含**可变对象**（如`列表`），这些对象内部的内容是**可以被改变**的：

```python
t = (1, 2, [3, 4])
t[2][0] = 9
print(t)  # 输出 (1, 2, [9, 4])
```

**元组的操作**

- `+` 运算符可以用来**连接**两个元组。
- `*` 运算符可以用来**重复**`元组`中的元素。

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)  # 输出 (1, 2, 3, 4, 5, 6)
print(t1 * 2)  # 输出 (1, 2, 3, 1, 2, 3)
```

**元组的解包**

`元组`解包允许你将元组中的元素直接赋值给多个变量：

```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)  # 输出 1 2 3
```

**使用场景**

元组在Python中的常见用途包括用作**函数的返回值**，**允许函数返回多个值**，以及在数据结构中作为**不可变元素**的存储，例如作为**字典的键**。因为元组的不可变性，它们可以在需要固定数据结构的场合提供一种**安全的选择**。

`元组`与`列表`一样，也支持切片操作，并可用于循环和其他迭代环境中。元组由于其不可变性，在某些情况下比列表更优，尤其是在程序中需要确保数据不被修改时。

### Python字典

`Python` 中的`字典`（`dictionary`）是一种**可变的**容器模型，能够存储**任意类型**对象，其中的每个元素都是一个**键值对**。`字典`在 `Python` 中使用**哈希表**实现，因此它们的主要优势是具有非常快的查找速度。这种数据结构特别适用于需要**快速访问数据**的情况。

**创建字典**

`字典`可以使用花括号 `{}` 创建，或者通过 `dict()` 函数。键和值之间使用冒号 `:` 分隔。

```python
my_dict = {'name': 'Alice', 'age': 25}
empty_dict = {}  # 空字典
another_dict = dict(name='Bob', age=24) #{'name': 'Bob', 'age': 24}
```

**访问字典元素**

你可以通过`键`来访问字典中的元素：

```python
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])  # 输出 'Alice'
```

如果尝试访问字典中**不存在的键**，`Python` 会抛出 `KeyError`。为了避免这种错误，可以使用 `get()` 方法，这样如果键不存在时，可以返回默认值（默认为 `None`）：

```python
print(my_dict.get('height'))  # 输出 None
print(my_dict.get('height', 160))  # 如果 'height' 不存在，返回 160
```

**修改和添加字典元素**

`字典`是**可变**的，所以你可以**添加**新的`键值对`或**修改**已有的`键值对`：

```python
my_dict = {'name': 'Alice', 'age': 25}
my_dict['age'] = 26  # 修改已有的键
my_dict['gender'] = 'Female'  # 添加新的键值对
```

**删除字典元素**

你可以使用 `del` 关键字或者`字典`的 `pop()` 方法来**删除**元素：

```python
del my_dict['gender']  # 删除键 'gender'
age = my_dict.pop('age')  # 删除键 'age' 并返回其值
```

**字典键的要求**

`字典`的`键`必须是**不可变**类型，如字符串、数字或元组，这些类型是**可哈希**的。**不可哈希**的类型，**如列表或另一个字典，不能作为键**。

**字典的遍历**

可以通过多种方式遍历`字典`：

```python
my_dict = {'name': 'Alice', 'age': 25}
# 遍历所有键
for key in my_dict.keys():
    print(key)

# 遍历所有值
for value in my_dict.values():
    print(value)

# 遍历所有键值对
for key, value in my_dict.items():
    print(key, value)
```

**字典的应用**

`字典`是`Python` 中非常有用的数据结构，广泛用于需要快速查找数据的场景，如实现数据库结果的缓存、存储设置或配置选项、构建网络请求的参数等。由于其键值对结构，`字典`在处理 `JSON` 数据和其他形式的结构化数据时也非常方便。

总之，`Python` 的字典提供了一种灵活高效的方式来组织和管理数据，其快速的键访问能力让它在众多应用场景中都能表现出色。

### Python函数

`Python` 中的函数是一种组织代码的基本方式，使你可以把`代码块`封装成一个单元，这个单元可以接收输入参数，并返回一个结果。函数在 `Python` 中通过 `def` 关键字定义，并使用 `return` 关键字返回结果。函数的使用可以提高代码的重用性、使代码更加模块化，并有助于减少代码的重复性。

**定义函数**

函数通过以下语法定义：

```python
def function_name(parameters):
    # 函数体
    return value
```

- `function_name` 是函数的名称。
- `parameters` 是函数可以接受的参数列表，参数之间用逗号分隔。
- `# 函数体` 是执行具体操作的代码块。
- `return` 是函数的返回语句，不是所有函数都需要返回语句。如果没有返回语句，函数默认返回 `None`。

**示例**

下面是一个简单的函数示例，该函数计算两个数的和：

```python
def add(a, b):
    return a + b

result = add(3, 4)  # 调用函数，传递参数3和4
print(result)  # 输出 7
```

**参数类型**

Python 函数的参数可以是**任意类型**，包括数字、字符串、列表、字典等，甚至可以是其他函数。Python 支持几种不同的参数类型：

- **位置参数**：最基本的参数类型，调用者需要按照函数定义中的顺序提供参数。
- **关键字参数**（Keyword arguments）：允许函数调用者指定为某些参数赋值，不必按顺序。
- **默认参数**：在定义函数时可以为参数提供默认值。如果调用时没有传递参数，将使用默认值。
- **可变参数**：如果你想让函数接受任意数量的参数，可以使用 `*args`（接受任意数量的位置参数）和 `**kwargs`（接受任意数量的关键字参数）。

示例：可变参数和关键字参数

```python
def greet(*names): #names为元组类型
    for name in names:
        print("Hello", name)

greet("Alice", "Bob", "Charlie")  # 输出 Hello Alice, Hello Bob, Hello Charlie

def profile(**details): #details为字典类型
    for key, value in details.items():
        print(f"{key}: {value}")

profile(name="Alice", age=25, job="Engineer")  # 输出 name: Alice, age: 25, job: Engineer
```

**递归函数**

`Python` 也支持递归函数，即**一个函数调用自身**。递归是一种强大的编程技术，可以解决特定类型的问题，如遍历树结构、解决分治问题等。

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 输出 120
```

总之，`Python` 中的函数是编写可维护和高效代码的关键工具。它们不仅有助于减少重复代码，还可以通过将复杂问题分解为更小、更易管理的部分来简化问题。

### Python作用域

在 `Python` 中，作用域定义了一个变量的可见性和生命周期。根据变量被定义的位置，它可能在不同的区域内被访问。`Python` 主要有四种类型的作用域：

+ **局部作用域（Local Scope）**

+ **全局作用域（Global Scope）**

+ **嵌套作用域（Enclosing Scope）**

+ **内置作用域（Built-in Scope）**

**局部作用域**

`局部作用域`是在函数内部创建的作用域。在这个作用域中定义的变量，只能在定义它的函数内部被访问。当函数调用结束后，`局部作用域`也会消失，**因此在函数外部无法访问这些变量**。

```python
def my_function():
    local_var = 5
    print(local_var)  # 在函数内部访问

my_function()
# print(local_var)  # 这将抛出一个错误，因为 local_var 在函数外部是不可见的
```

**全局作用域**

`全局作用域`是在模块级别定义的作用域。在这个作用域中定义的变量，可以在**整个模块内的任何位置被访问**，包括函数内部**。如果你需要在一个函数内修改全局变量，需要使用 `global` 关键字**。

```python
global_var = 10  # 全局变量

def my_function():
    global global_var
    global_var = 20  # 修改全局变量

print(global_var)  # 输出 10
my_function()
print(global_var)  # 输出 20
```

**嵌套作用域**

`嵌套作用域`是在一个函数内部定义另一个函数时创建的变量。在这种情况下，内部函数可以访问其外部函数的变量。

```python
def outer():
    outer_var = "外部变量"
    
    def inner():
        print(outer_var)  # 访问外部函数的变量

    inner()

outer()
```

**内置作用域**

`Python` 内置了一些特殊的作用域，被称为“内置作用域”。这些作用域包含了内置的变量、函数和其他特殊方法。

在Python中，内置作用域可以通过内置函数`globals()`和`locals()`来访问。`globals()`函数返回一个字典，该字典包含当前模块的全局作用域中的所有变量。`locals()`函数返回一个字典，该字典包含当前作用域中的所有变量。

以下是一些示例代码：

**访问全局作用域**：

```python
def print_globals():
    global_vars = globals()
    for name, val in global_vars.items():
        print(f"{name}: {val}")
 
print_globals()
#输出:
#__name__: __main__
#__doc__: None
#__package__: None
#__loader__: <class '_frozen_importlib.BuiltinImporter'>
#__spec__: None
#__annotations__: {}
#__builtins__: <module 'builtins' (built-in)>
#greet: <function greet at 0x0000022880FED4C0>
#profile: <function profile at 0x000002288293E160>
#print_globals: <function print_globals at 0x000002288293E1F0>
```

**作用域链**

当一个变量被引用时，`Python 解释器`会遵循`LEGB 规则`来查找这个变量：

- **L, Local** — 首先在局部作用域中查找。
- **E, Enclosing** — 如果在局部作用域找不到，接着在嵌套的作用域中查找，即在外围函数的局部作用域中查找。
- **G, Global** — 如果在嵌套作用域中仍找不到，接着在全局作用域中查找。
- **B, Built-in** — 如果在全局作用域中仍找不到，最后在内置作、用域中查找。

了解这些作用域和规则对于编写清晰、高效且易于维护的 `Python` 代码至关重要。

### Python模块

在 `Python` 中，模块是一种将代码组织成包含函数、类和变量以及可执行代码的文件。模块的主要目的是帮助组织代码并提供代码重用性，同时也能够提高代码的可管理性和可维护性。每个 `Python` 文件都可以被当作一个模块，可以通过 `import` 语句导入其他 `Python` 文件（模块）。

**创建和使用模块**

要创建一个模块，只需将相关的代码保存在一个 `.py` 文件中。例如，你可以创建一个名为 `mymodule.py` 的文件，其中包含一些函数和变量：

```python
# mymodule.py

def greet(name):
    print("Hello, " + name + "!")

favorite_language = "Python"
```

在其他 `Python` 文件中，你可以使用 `import` 语句来导入这个模块，并使用其中定义的函数和变量：

```python
# main.py

import mymodule

mymodule.greet("Alice")  # 输出 "Hello, Alice!"
print("Favorite Language:", mymodule.favorite_language)  # 输出 "Favorite Language: Python"
```

**模块的命名空间**

当你导入一个模块时，Python 会创建一个名为模块名的`命名空间`，在这个`命名空间`里，你可以访问模块中定义的所有**公共属性**。这种方式有助于避免名字冲突，因为每个模块都是自己的私有作用域。

**导入模块的不同方式**

除了上面的导入方式，`Python` 还提供了其他几种导入模块的方法：

1. **导入特定的属性**：

   ```python
   from mymodule import greet
   greet("Bob")  # 直接使用 greet 函数
   ```

2. **使用别名导入模块**：

   ```python
   import mymodule as mm
   mm.greet("Carol")
   ```

3. **导入模块中的所有内容**：

   ```python
   from mymodule import *
   greet("Dave")
   print(favorite_language)
   ```

> 注意：使用 `from module import *` 可能会导致不可预见的命名冲突，因此在大型项目中通常不推荐使用。

**模块的搜索路径**

当你尝试导入一个模块时，`Python` 解释器会在一系列位置搜索这个模块：

- 当前目录
- 环境变量 PYTHONPATH 所列的每个目录
- 标准库的目录
- 任何第三方的库目录（通常安装在 Python 的 `site-packages` 目录下）

如果模块在搜索路径中找到，它将被导入。如果没有找到，`Python` 将抛出一个 `ModuleNotFoundError`。

**模块初始化代码**

模块可以包含初始化代码，这些代码通常用于设置模块级别的配置或初始化状态。这些代码只在模块第一次被导入时执行一次。

假设你有一个模块 `config.py`，它负责应用程序的配置管理。你可以在模块级别定义初始化代码来加载配置文件，并设置一些基本的应用参数：

```python
# config.py

import os
import json

# 模块级变量，用来存储配置
configuration = {}

def load_config():
    with open('config.json', 'r') as f:
        configuration.update(json.load(f))

# 初始化代码，加载配置文件
load_config()

print("Configuration loaded:", configuration)
```

在这个例子中，函数 `load_config` 被定义用来加载一个 JSON 格式的配置文件，并存储在全局字典 `configuration` 中。这个函数在模块代码中被调用，因此**任何首次**导入此模块的地方都会看到打印的 "Configuration loaded" 信息，并且配置数据在模块的**任何其他部分**都可以使用。

### Python类

`Python` 中的类是一种组织代码的结构，它允许程序员将数据（属性）和功能（方法）封装在一起。这种封装提供了对象的概念，可以模拟现实世界中的行为和属性。`Python` 的类支持继承、多态和封装，是一种面向对象编程（`OOP`）的实现。

**基本概念**

- **类（Class）**：定义了一组对象共有的属性和方法的模板。例如，狗可以是一个类，具有属性如品种、大小和年龄，以及方法如吠叫和摇尾巴。
- **实例（Instance）**：根据类定义创建的具体对象。例如，你家的宠物狗是狗类的一个实例。
- **属性（Attribute）**：属于类的变量，可以是数据或状态。实例属性特定于每个对象实例，类属性由类的所有实例共享。
- **方法（Method）**：属于类的函数，定义了对象的行为。

**类定义和实例化**

一个简单的 `Python` 类定义如下：

```python
class Dog:
    # 类属性
    species = "Canis familiaris"

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性

    # 一个方法
    def describe(self):
        return f"{self.name} is {self.age} years old."

    # 另一个方法
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

这个类有一个类属性 `species`，两个实例属性 `name` 和 `age`，以及两个方法 `describe` 和 `speak`。

要创建这个类的实例，你可以这样做：

```python
my_dog = Dog("Rex", 5)
print(my_dog.describe())  # 输出: Rex is 5 years old.
print(my_dog.speak("Woof"))  # 输出: Rex says Woof
```

**特殊方法**

`Python` 类也支持特殊方法，这些方法以双下划线（`__`）开始和结束。这些方法有特殊的意义，例如：

- `__init__()`：构造器，当一个新对象被创建时调用。
- `__str__()`：当使用 `print()` 函数或 `str()` 函数时调用。
- `__repr__()`：官方字符串表示，用于调试和其他开发者使用。

例如，添加 `__str__` 和 `__repr__` 到 `Dog` 类：

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Dog({self.name}, {self.age})"
```

现在当你打印对象或在开发环境中查看对象时，可以看到更友好或更明确的信息。

**继承**

`Python` 支持类的继承，允许从一个父类继承方法和属性到子类。这是扩展或修改现有代码的一种强大方式。

```python
class Bulldog(Dog):  # 继承Dog类
    def speak(self):
        return f"{self.name} says Woof with a deep voice"
```

在这个例子中，`Bulldog` 类**继承**了 `Dog` 类，并**重载**了 `speak` 方法以反映斗牛犬不同的叫声。

小结

`Python` 中的类是面向对象编程的核心，提供了一种强大的方式来模拟现实世界的复杂性和层次结构。通过继承和多态，可以创建可维护、可扩展和可重用的代码。

### Python文件操作

在 `Python` 中处理文件是一项常见的任务，无论是读取数据文件、写入日志，还是管理系统文件。`Python` 提供了几种方式来读写文件，最基本的是使用内置的 `open()` 函数。

**打开文件**

`open()` 函数用于打开一个文件，并返回一个文件对象。基本语法如下：

```python
file_object = open(file_name, mode)
```

其中 `file_name` 是包括路径的文件名，`mode` 是打开文件的模式。常见的模式包括：

- `'r'`：读取模式（默认）。
- `'w'`：写入模式，先清空文件再写入。如果文件不存在，创建新文件。
- `'x'`：排他性创建，如果文件已存在，则失败。
- `'a'`：追加模式，写入数据时会追加到文件末尾。如果文件不存在，创建新文件。
- `'b'`：二进制模式。
- `'t'`：文本模式（默认）。
- `'+'`：更新（读写）模式。

**读取文件**

打开文件后，可以使用多种方法读取内容：

```python
# 使用 open() 和 read() 读取整个文件
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 逐行读取
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

**写入文件**

写入文件同样简单，使用 `write()` 方法或 `writelines()` 方法：

```python
# 使用 write() 写入文件
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")

# 使用 writelines() 写入多行
lines = ["First line\n", "Second line\n"]
with open('output.txt', 'a') as file:
    file.writelines(lines)
```

**文件和异常处理**

在处理文件时，应注意异常处理，确保文件操作不会导致程序意外崩溃，并且文件能正常关闭：

```python
try:
    with open('somefile.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("文件未找到")
except Exception as e:
    print(f"发生错误: {e}")
```
**其他文件操作**

除了基本的读写操作，`Python` 还提供了其他用于处理文件的功能，如 `os` 和 `shpassutil` 模块，可以用来删除文件、创建目录、改变工作目录、检查文件属性等。

```python
import os

# 获取当前工作目录
print(os.getcwd())

# 列出目录内容
print(os.listdir('.'))

# 重命名文件
os.rename('old_name.txt', 'new_name.txt')

# 删除文件
os.remove('old_name.txt')
```

这些基本的文件操作是 `Python` 编程中非常核心的部分，能够有效地帮助管理和处理文件数据。

### Python异常处理

在 `Pytho` 中，异常处理是一种结构化的错误处理方式，它允许程序在发生错误时优雅地恢复。`Python` 使用 `try`、`except`、`else`、`finally` 块来处理异常。

**基本异常处理**

以下是 `Python` 中异常处理的基本结构：

```python
try:
    # 尝试执行的代码
    result = 10 / 0
except ZeroDivisionError:
    # 如果在 try 块中发生了 ZeroDivisionError 异常，执行这块
    print("除数不能为零")
except Exception as e:
    # 处理 try 块中发生的其他异常
    print(f"发生了一个错误: {e}")
else:
    # 如果没有异常发生，执行这块
    print("一切正常")
finally:
    # 无论是否发生异常，都会执行这块代码
    print("清理操作")
```

**异常类型**

`Python` 中的异常是从 `BaseException` 类派生出来的。常见的一些**内置异常类型**包括：

- `Exception`：常规错误的基类
- `ArithmeticError`：数学运算错误的基类
- `BufferError`：与缓冲区操作有关的问题
- `LookupError`：无效数据查询的基类，例如索引和键
- `FileNotFoundError`：访问不存在的文件时引发
- `ValueError`：当函数接收到有正确类型但不合适的值时引发
- `TypeError`：当操作或函数应用于不适当类型的对象时引发

**自定义异常**

为了创建和抛出自定义异常，你可以继承 `Exception` 类：

```python
class MyError(Exception):
    """自定义异常类"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError("Oops!")
except MyError as e:
    print(f'Caught an error: {e}')
```

**异常的传递**

如果一个异常在当前的 `try` 块中没有被捕获（即没有相应的 `except` 子句），它将被传递到上一层的 `try` 块中。如果在最外层也没有被捕获，那么程序将终止，并显示一个错误消息。

**使用断言**

除了异常处理，`Python` 还允许使用 `assert` 语句进行调试。当 `assert` 后面的条件为 `False` 时，将引发一个 `AssertionError`：

```python
def get_age(age):
    assert age > 0, "年龄必须大于零"
    print(f"你的年龄是：{age}")

get_age(-1)  # 将引发 AssertionError
```

### Python标准库

**常用标准库**

| 模块名称   | 描述                                                 |
| ---------- | ---------------------------------------------------- |
| `os`       | 提供操作系统级别的接口，如文件、目录以及路径等操作。 |
| `sys`      | 用于访问与 Python 解释器紧密相关的变量和函数。       |
| `math`     | 提供数学运算函数，如三角函数、对数等。               |
| `random`   | 生成随机数和进行随机选择。                           |
| `datetime` | 处理日期和时间，支持日期、时间的创建、操作及格式化。 |
| `json`     | 用于处理JSON数据格式的编码和解码。                   |
| `re`       | 支持正则表达式的各种功能，进行字符串搜索和替换等。   |
| `http`     | 用于处理HTTP会话，构建请求和解析响应。               |
| `logging`  | 实现灵活的日志记录系统。                             |
| `argparse` | 创建命令行界面，解析运行脚本时指定的命令行参数。     |

**简单说明**

**`os`**

模块提供了许多与操作系统交互的函数。你可以使用这个模块来读取或写入文件，处理路径，以及管理目录和文件。例如，`os.path` 子模块提供了跨平台的路径操作功能。

- `os.listdir()`：列出目录中的内容。
- `os.mkdir()`：创建新目录。
- `os.path.join()`：安全地拼接文件路径。

**`sys`**

模块提供了对一些与 Python 解释器强相关的变量和功能的访问，包括标准输入输出的处理和程序的退出。

- `sys.argv`：命令行参数列表。
- `sys.exit()`：退出程序，可指定返回值。
- `sys.path`：Python 模块的搜索路径，可以修改以影响模块加载。

**`math`**

提供了标准的数学运算，包括三角函数、对数和其他常见的数学计算。

- `math.sqrt()`：计算平方根。
- `math.sin()`, `math.cos()`, `math.tan()`：三角函数。

**`random`**

用于生成伪随机数，适用于模拟和其他随机化任务。

- `random.randint()`：生成一个指定范围的随机整数。
- `random.choice()`：从序列中随机选取一个元素。

**`datetime`**

处理日期和时间的标准库，支持日期和时间的运算。

- `datetime.datetime.now()`：获取当前日期和时间。
- `datetime.timedelta()`：计算时间间隔。

**`json`**

模块提供了 JSON 字符串的解析和生成，是与 Web 数据交换格式交互的重要工具。

- `json.loads()`：将 JSON 字符串解码转换成 Python 对象。
- `json.dumps()`：将 Python 对象编码成 JSON 字符串。

**`re`**

提供正则表达式的强大处理能力，适用于复杂的字符串操作和模式匹配。

- `re.search()`：在一个字符串中搜索匹配正则表达式的第一个位置。
- `re.findall()`：找出字符串中所有正则表达式的匹配项。

**`http`**

主要用于处理 HTTP 请求和响应，适合开发 Web 客户端。

- `http.client.HTTPConnection()`：创建 HTTP 连接。

**`logging`**

为应用程序提供了灵活的日志记录系统，支持多种日志级别，以及日志记录到多种目的地。

- `logging.debug()`, `logging.info()`, `logging.warning()`, `logging.error()`, `logging.critical()`：这些方法用于记录不同级别的日志信息。
- `logging.basicConfig()`：配置基本的日志系统，设置日志级别和输出格式。

**`argparse`**

主要用于解析命令行参数的库。它使得编写用户友好的命令行程序变得简单，可以定义必须的参数和可选的开关，并自动生成帮助和使用消息。

**创建解析器**：

``` python
import argparse
parser = argparse.ArgumentParser(description='Example Application')
```

**添加参数**：

```python
parser.add_argument('-v', '--verbose', help='increase output verbosity', 						action='store_true')
parser.add_argument('filename', help='the file to be processed')
```
这里 `-v` 或 `--verbose` 是一个可选参数，而 `filename` 是一个位置参数。

**解析参数**：

```python
args = parser.parse_args()
if args.verbose:
	print("Verbose mode on")
print("Processing file:", args.filename)
```

**示例**

以下是一个简单的例子，假设你正在编写一个脚本来计算两个数的和：

```python
import argparse

def add_numbers(num1, num2):
    return num1 + num2

def main():
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("num1", type=int, help="The first number")
    parser.add_argument("num2", type=int, help="The second number")
    args = parser.parse_args()
    
    result = add_numbers(args.num1, args.num2)
    print("The sum of {} and {} is {}".format(args.num1, args.num2, result))

if __name__ == "__main__":
    main()
```

在这个例子中，我们首先导入了`argparse`库。然后定义了一个`add_numbers`函数，用于计算两个数的和。接着是`main`函数，其中我们首先创建了一个`ArgumentParser`对象，指定了程序的描述。然后使用`add_argument`方法添加了两个位置参数，分别是要相加的两个数。最后使用`parse_args`方法解析命令行参数，并调用`add_numbers`函数计算结果并打印出来。

你可以在命令行中运行这个脚本，并提供两个数字作为参数，例如：

```shell
python script.py 10 20
```

这将输出：

```shell
The sum of 10 and 20 is 30
```



## Python高阶

### Python装饰器

`Python` 中的装饰器是一种非常有用的特性，它允许用户修改函数或类的行为而不需要改变其结构。装饰器在很多框架中广泛使用，用于增加函数功能而保持代码的清晰和简洁。

**装饰器的基本概念**

装饰器本质上是一个函数，它接受一个函数作为参数并返回一个新的函数。装饰器可以在不修改原有函数代码的情况下增加额外的功能。

**创建装饰器**

创建一个装饰器通常涉及定义一个接受函数作为参数的函数，并返回另一个函数。返回的函数通常会增加一些功能，然后执行原始函数。

**示例：一个简单的装饰器**

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

在这个例子中，`my_decorator` 是一个装饰器，它在被装饰的函数 `say_hello()` 前后添加了一些功能。使用 `@my_decorator` 语法，我们应用了装饰器。

**装饰器的高级用法**

1. **带参数的装饰器**：有时你可能想让装饰器支持参数。这可以通过使用另一个函数来处理这些参数来实现。

   ```python
   def repeat(num_times):
       def decorator_repeat(func):
           def wrapper(*args, **kwargs):
               for _ in range(num_times):
                   result = func(*args, **kwargs)
               return result
           return wrapper
       return decorator_repeat
   
   @repeat(num_times=4)
   def greet(name):
       print(f"Hello {name}")
   
   greet("Alice")
   ```

2. **使用 functools.wraps**：使用装饰器时，你可能会发现被装饰的函数的 `__name__` 和 `__doc__` 等属性“丢失”了。为了解决这个问题，可以使用 `functools` 模块中的 `wraps` 工具。

   ```python
   from functools import wraps
   
   def my_decorator(func):
       @wraps(func)
       def wrapper(*args, **kwargs):
           """A wrapper function"""
           # Do something before
           result = func(*args, **kwargs)
           # Do something after
           return result
       return wrapper
   
   @my_decorator
   def say_hello():
       """Greet someone."""
       print("Hello!")
   
   print(say_hello.__name__)  # 输出 'say_hello'
   print(say_hello.__doc__)   # 输出 'Greet someone.'
   ```

### Python实现单例模式

在`Python`中实现单例模式的目的是确保一个类只有一个实例，并且提供一个全局访问点来获取该实例。单例模式常用于数据库连接、配置设置等场景，其中多个实例可能导致的冲突或资源过度使用应当被避免。下面介绍几种在`Python`中实现单例模式的常见方法：

1. **使用模块**

`Python`的模块在第一次导入时会被初始化，之后再次导入时会使用同一个实例，因此模块自身就是一个单例。这是实现单例的最简单方法。

2. **使用装饰器**

可以创建一个装饰器，用于装饰类以确保只创建一个实例：

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.connection = "Connection established"

db1 = Database()
db2 = Database()
print(db1 is db2)  # 输出 True
```

> 在使用装饰器实现单例模式的示例中，`instances` 是一个局部变量，但它具有类似全局变量的行为。这种行为的原因在于它被定义在装饰器 `singleton` 的闭包中，因此它对于每个装饰的类都是唯一且持久的。这使得 `instances` 在装饰器函数内部为所有调用保持状态，跨多次使用装饰器的调用保持了类的实例。
>
> Python 中的闭包允许内部函数引用外部函数的变量。在这种情况下，`get_instance` 函数是 `singleton` 的内部函数，并且它访问外部函数 `singleton` 中定义的 `instances` 变量。即便 `singleton` 函数执行完成后，`instances` 变量依然因为闭包的存在而被保留，这使得每次类被实例化时都可以访问同一个 `instances` 字典。
>
> 这种模式确保了无论类在何处或何时被实例化，装饰器都能返回同一个实例，符合单例模式的要求。

3. **使用类变量和特殊方法**

这种方法利用类本身来存储它的唯一实例，并在需要时创建它。

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    # 以下是类的其他方法
    def __init__(self):
        self.value = "Some data"

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # 输出 True
```

4. **使用基类**

创建一个基类，其他需要成为单例的类继承这个基类。

```python
class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBase, cls).__new__(cls)
        return cls._instances[cls]

class Logger(SingletonBase):
    pass

class Config(SingletonBase):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # 输出 True

config1 = Config()
config2 = Config()
print(config1 is config2)  # 输出 True
```

5. 使用元类

元类是创建类的“类”。可以利用元类来确保某个类只有一个实例。

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Database Connection"

db1 = Database()
db2 = Database()
print(db1 is db2)  # 输出 True
```

### Python调用C代码

在 `Python` 中调用 `C` 代码是一个常见的做法，尤其是当你需要执行一些性能敏感的操作时。`Python` 提供了几种方式来实现与 `C` 语言的集成，主要包括以下几种方法：

1. **使用 `ctypes` 模块**

`ctypes` 是 `Python` 的一个标准库，它允许从 `Python` 中调用 `C` 库的函数，并处理简单的数据类型转换。使用 `ctypes` 不需要编写额外的 `C` 代码来包装库函数，但你需要确保手动处理数据类型和转换的正确性。

**示例**： 假设你有一个 `C` 的动态库（`example.so` 或 `example.dll`），其中有一个函数定义如下：

```c
// C code
int add(int a, int b) {
    return a + b;
}
```

你可以这样从 `Python` 中调用它：

```python
from ctypes import CDLL, c_int

# 加载动态链接库
lib = CDLL('./example.so')

# 设置函数参数类型
lib.add.argtypes = [c_int, c_int]

# 设置返回类型
lib.add.restype = c_int

# 调用函数
result = lib.add(10, 20)
print(result)  # 输出 30
```

2. **使用 Python/C API**

`Python/C API` 允许你编写 `C` 扩展模块来扩展 Python。这种方式相比 `ctypes` 更复杂，但提供了更高的灵活性和更好的性能，因为它允许直接与 Python 解释器交互。

你需要写一些 `C` 代码来创建新的 `Python` 类型，或者定义新的 `Python` 函数。然后，使用 `Python` 的构建工具（如 `setuptools`）编译这些 `C` 代码为 `Python` 模块。

**示例**： `C` 代码 (`add_module.c`):

```c
#include <Python.h>

static PyObject* py_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    return PyLong_FromLong(a + b);
}

static PyMethodDef AddMethods[] = {
    {"add", py_add, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef addmodule = {
    PyModuleDef_HEAD_INIT,
    "add_module",
    NULL,
    -1,
    AddMethods
};

PyMODINIT_FUNC PyInit_add_module(void) {
    return PyModule_Create(&addmodule);
}
```

使用 `Python` 的构建工具编译这个模块，然后就可以像使用普通 `Python` 模块一样使用它了。

3. 使用 `Cython`

`Cython` 是一个流行的 `Python` 库，它旨在成为 `Python` 和 `C` 的一个桥梁。`Cython` 允许你在 `Python` 代码中使用 `C` 语言的语法，并提供了将 `Python` 代码编译成 `C` 代码的能力。这通常用于提高性能，同时保持编写代码的灵活性。

`Cython` 的工作流程包括编写 `.pyd` 文件，然后使用 `Cython` 编译它们为 C 文件，再进一步编译为机器码。

**示例**： 创建一个 `add.pyd` 文件：

```
def add(int a, int b):
    return a + b
```

使用 `Cython` 工具编译 `.pyd` 文件，并在 `Python` 中导入使用。

这些方法各有利弊，你可以根据具体的应用场景和性能需求选择最适合的方法。

### C调用Python代码

使用 C Foreign Function Interface (`CFFI`) 库调用 `Python` 代码是一种在 `C` 与 `Python` 之间建立桥梁的流行方法。`CFFI` 提供了一种机制，允许 `C` 程序调用 `Python` 代码，也允许 `Python` 代码调用 `C` 库。`CFFI` 是比较现代的方法，相比传统的 `Python` `C` `API`，它更加简洁和灵活。

**安装 CFFI**

首先，你需要安装 CFFI 库。如果还没有安装，可以通过 pip 安装：

```bash
pip install cffi
```

**示例：使用 CFFI 在 C 中调用 Python 代码**

**步骤 1**: 定义 Python 模块

假设我们有一个简单的 `Python` 函数，我们希望从 `C` 代码中调用它。首先，我们定义这个函数和一个接口以供 `C` 使用。

```python
from cffi import FFI

ffi = FFI()

# 定义将暴露给 C 的函数
@ffi.callback("int(int,int)")
def add(x, y):
    print(f"Called from C with parameters {x} and {y}")
    return x + y

# python调用c库中的注册函数(此部分参考"python调用c")
lib.register_callback_add(add) 
```

**步骤 2**: 编写 `C` 代码

现在，你可以在 C 程序中使用这个共享库来调用 `my_python_function` 函数。

```c
static int(*g_register_callback_add)(int, int) = NULL;

int register_callback_add(int(*callback)(int, int))
{
    if (callback != NULL) {
        g_register_callback_add = callback;
    }
}
```

使用 `CFFI` 可以让 `C` 与 `Python` 的交互更加灵活，同时避免了直接使用 `Python` `C` `API` 时的复杂性。

### Python Lambda

`Python` 中的 `lambda` 函数是一种小型的匿名函数，它仅包含一个表达式，不可以包含多个语句或注释。`Lambda` 函数可以用来编写简单的、一次性的、没有名称的函数，在很多场景下非常有用，尤其是在需要一个简单功能的地方，比如在排序或过滤数据时。

**基本语法**

`Lambda` 函数的基本语法如下：

```python
lambda arguments: expression
```

这里：

- `arguments` 是传递给 lambda 函数的参数，可以有多个，用逗号分隔。
- `expression` 是一个表达式，它基于输入的参数计算并返回一个值。Lambda 函数不支持多个表达式或语句，也不支持显式的 `return` 语句；它自动返回表达式的结果。

**示例**

**示例 1**: 单参数 `Lambda` 函数

```python
double = lambda x: x * 2
print(double(5))  # 输出: 10
```

这个 `lambda` 函数接受一个参数 `x` 并返回 `x` 的两倍。

**示例 2**: 多参数 `Lambda` 函数

```python
add = lambda x, y: x + y
print(add(5, 3))  # 输出: 8
```

这个 `lambda` 函数接受两个参数 `x` 和 `y`，并返回它们的和。

**示例 3**: 在高阶函数中使用` Lambda`

`Lambda` 函数经常与高阶函数（如 `map()`, `filter()`, `sorted()` 等）一起使用。

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]
```

这里，`map()` 函数接受一个函数和一个列表，将函数应用于列表中的每个元素。我们使用 `lambda` 函数来定义应用的函数。

使用场景和注意事项

1. **简洁性**：`Lambda` 函数由于其简洁性，非常适合需要简单函数的场景，尤其是只用一次的函数。
2. **功能限制**：由于 `lambda` 只能写一个表达式，所以功能上比较受限。复杂的逻辑应该使用标准的函数定义方式，这样代码更易于理解和维护。
3. **可读性**：过度使用 `lambda` 函数可能会降低代码的可读性。合理使用是关键，尤其是在其他开发者也需要阅读或维护你的代码时。

`Lambda` 函数提供了 `Python` 编程中一个强大而灵活的工具，但应当在不影响代码可读性的前提下恰当使用。

### Python处理csv文件

`Python` 处理 `CSV` 文件通常使用标凑库中的 `csv` 模块，该模块提供了读写 `CSV` 文件的功能。对于更复杂的数据处理需求，许多开发者还会使用 `pandas` 库，因为它提供了更加强大且便捷的数据操作方式。这里我将分别介绍如何使用 `csv` 模块和 `pandas` 库来处理 `CSV` 文件。

**读取 `CSV` 文件**

使用 `csv` 模块的 `reader` 函数可以轻松读取 `CSV` 文件：

```python
import csv

# 打开 CSV 文件
with open('example.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # row 是一个列表，包含了 CSV 文件中的每一行
```

**写入 `CSV` 文件**

使用 `csv` 模块的 `writer` 函数可以写入 `CSV` 文件：

```python
import csv

# 数据列表
data = [
    ['Name', 'Age'],
    ['Alice', 24],
    ['Bob', 19]
]

# 写入 CSV 文件
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # 写入多行
```

**使用 `pandas` 库**

`pandas` 是一个强大的数据处理库，非常适合进行复杂的数据分析和处理。处理 `CSV` 文件时，`pandas` 提供了非常方便的功能。

**读取 `CSV` 文件**

```python
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('example.csv')
print(df)
```

**写入 `CSV` 文件**

```python
import pandas as pd

# 创建 DataFrame
data = {
    'Name': ['Alice', 'Bob'],
    'Age': [24, 19]
}
df = pd.DataFrame(data)

# 写入 CSV 文件
df.to_csv('output.csv', index=False)  # index=False 表示不保存行索引到文件
```

**注意事项**

1. **文件路径**：确保在读写文件时提供正确的文件路径，否则可能会遇到文件找不到的错误。
2. **编码问题**：在处理非英文内容的 `CSV` 文件时，可能需要指定文件的编码（如 `encoding='utf-8'`）。
3. **数据类型**：特别是使用 `pandas` 时，注意检查导入的数据类型是否符合预期，有时可能需要对数据类型进行转换。

这些基本介绍应该可以帮助你开始使用 `Python` 处理 `CSV` 文件。根据具体需求选择使用 `csv` 模块或 `pandas` 库。`pandas` 尤其适合处理大型数据集和进行复杂的数据转换和分析。

### Python Matplotlib

`matplotlib` 是 `Python` 中一个非常流行的绘图库，常用于数据可视化。它支持多种图表类型，如线图、条形图、散点图、饼图等。`matplotlib` 提供了大量的函数和工具，使得创建复杂的图表变得可能，且能够高度自定义。

**基本使用**

要开始使用 `matplotlib`，通常首先从 `pyplot` 模块开始，它提供了一个类似于 `MATLAB` 的接口。

**安装**

如果你还没有安装 `matplotlib`，可以通过 `pip` 安装：

```bash
pip install matplotlib
```

**创建一个简单的线图**

下面是一个简单的例子，展示如何绘制一个基本的线图：

```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建图形
plt.plot(x, y)

# 添加标题和标签
plt.title('Example Line Chart')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# 显示图形
plt.show()
```

**多种图表**

`matplotlib` 可以创建多种类型的图表。这里是一些常见类型的示例：

**条形图**

```python
import matplotlib.pyplot as plt

# 数据
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [15, 30, 7, 22]

# 创建条形图
plt.bar(categories, values)

# 添加标题和标签
plt.title('Example Bar Chart')
plt.xlabel('Fruits')
plt.ylabel('Quantities')

# 显示图形
plt.show()
```

**散点图**

```python
import matplotlib.pyplot as plt

# 数据
x = [5, 20, 15, 25, 10]
y = [25, 15, 20, 10, 30]

# 创建散点图
plt.scatter(x, y)

# 添加标题和标签
plt.title('Example Scatter Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# 显示图形
plt.show()
```

**自定义和配置**

`matplotlib` 的一个强大之处在于它提供了丰富的配置选项，包括颜色、标记、线型等。这使得你可以精细控制图表的外观：

```python
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建图形，自定义线条的颜色和形式
plt.plot(x, y, color='red', linestyle='--', marker='o')

# 添加网格
plt.grid(True)

# 添加标题和标签
plt.title('Customized Line Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
```

**高级用法**

随着你对 `matplotlib` 的熟悉度提高，你可以探索更多高级功能，例如子图、动画和`3D`图形等。`matplotlib` 还允许你深度定制图表，比如通过 `rcParams` 调整图表的全局样式，或者使用 `Figure` 和 `Axes` 对象进行更复杂的图形构建。

### Python Pandas

`pandas` 是 `Python` 中一个非常流行且强大的数据处理和分析库。它提供了快速、灵活和表达力强的数据结构，旨在使数据操作和分析工作变得简单直观。`pandas` 主要用于对表格数据进行处理，是基于 `NumPy` 的一个扩展。

**主要数据结构**

`pandas` 有两个核心的数据结构：`DataFrame` 和 `Series`。

- **Series**：一维数据结构，类似于 `Python` 的列表或 `NumPy` 的数组，但每个元素都有一个标签（或索引）。
- **DataFrame**：二维数据结构，类似于 `Excel` 的工作表，或 `SQL` 表，可以看作是多个 `Series` 的集合。

**安装**

如果你还没有安装 `pandas`，可以通过以下命令安装：

```bash
pip install pandas
```

**基本使用**

**创建数据**

`pandas` 可以从多种数据源创建 `DataFrame`，例如字典、列表、`CSV` 文件、`SQL` 数据库等。

```python
import pandas as pd

# 使用字典创建 DataFrame
data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)
```

**数据访问**

访问 `DataFrame` 中的数据可以通过列名、行标签或位置索引。

```python
# 获取一列数据
ages = df['Age']

# 获取一行数据
alice = df.loc[0]  # 使用行标签
alice_by_index = df.iloc[0]  # 使用位置索引
```

**数据操作**

`pandas` 提供了丰富的方法用于数据操作，包括筛选、排序、分组、合并等。

```python
# 筛选
adults = df[df['Age'] > 30]

# 排序
sorted_df = df.sort_values(by='Age')

# 分组
grouped = df.groupby('City').mean()

# 合并
other_data = pd.DataFrame({
  'Name': ['Dave', 'Eve'],
  'Age': [40, 22],
  'City': ['Berlin', 'Madrid']
})
combined_df = pd.concat([df, other_data])
```

**数据分析**

`pandas` 非常适合进行各种统计分析：

- 计算描述性统计量（如均值、中位数、标准差等）。
- 执行聚合操作和数据透视。
- 处理时间序列数据。

```python
# 描述性统计
statistics = df.describe()

# 数据透视表
pivot = pd.pivot_table(df, values='Age', index='City', aggfunc='mean')
```

**数据输入/输出**

`pandas` 支持多种格式的数据读取和写入，包括 `CSV`、`Excel`、`JSON`、`SQL` 数据库等。

```
python# 读取 CSV
df_from_csv = pd.read_csv('data.csv')

# 写入 Excel
df.to_excel('output.xlsx')
```

**总结**

`pandas` 是数据科学领域非常重要的工具之一，它的强大功能和灵活性使得数据处理、清洗、探索和分析变得高效而直观。无论是在学术研究、金融分析还是商业智能领域，`pandas` 都是数据分析师和科学家们不可或缺的工具。

### Python Numpy

`NumPy` 是 `Python` 中的一个核心科学计算库，它提供了一个高性能的多维数组对象以及用于处理这些数组的工具。`NumPy` 数组不仅速度快，内存效率也高于 `Python` 原生的列表。除了数组，它还提供了矩阵运算和广泛的数学函数库。`NumPy` 是许多其他科学计算库的基础，比如 `SciPy`、`Pandas` 和 `scikit-learn`。

**安装**

安装 `NumPy` 推荐使用 `pip`：

```bash
pip install numpy
```

**核心功能**

1. **多维数组（`ndarray`）**

`NumPy` 的主要对象是同质多维数组，也就是所有元素类型相同的`n`维数组。这可以极大地加快运算速度，因为相较于 `Python` 列表，数组在内存中是连续存储的。

```python
import numpy as np

# 创建一个3x3的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
```

2. **数组索引和切片**

`NumPy` 提供了多种索引方式，包括基础索引、布尔索引和花式索引。

```python
# 获取数组的一个部分
print(arr[0, :])  # 获取第一行
print(arr[:, 1])  # 获取第二列
```

3. **广播机制**

广播（`Broadcasting`）是 `NumPy` 的一种强大机制，允许不同形状的数组进行算术运算。较小的数组会“广播”到较大数组的大小，以便形状兼容。

```python
# 数组与标量的运算
print(arr + 1)  # 每个元素都加1
```

4. **数学函数和运算**

`NumPy` 提供了大量的数学函数，这些函数可以直接作用于数组级别，执行效率非常高。

```python
# 线性代数运算
print(np.dot(arr, arr))  # 矩阵乘法

# 统计函数
print(np.mean(arr))  # 求平均值
```

5. **形状操作**

你可以改变数组的形状而不改变其数据。

```python
# 重塑数组
new_arr = arr.reshape((1, 9))
print(new_arr)
```

6. **数据类型**

`NumPy` 支持比 `Python` 列表更多的数据类型，你可以在创建数组时选择数据类型。

```python
arr_int = np.array([1, 2, 3], dtype=np.int32)  # 使用32位整数
arr_float = np.array([1.1, 2.2, 3.3], dtype=np.float64)  # 使用64位浮点数
```

**总结**

`NumPy` 是 `Python` 数据科学和科学计算的基础库之一，它的多维数组和广泛的数学函数是处理大规模数据的强大工具。无论是在数据分析、机器学习还是更广泛的科学计算领域，`NumPy` 都是不可或缺的一个工具。

### Python Scipy

`SciPy` 是 `Python` 中使用广泛的一个开源科学计算库，用于数学、科学和工程领域。它建立在 `NumPy` 的基础上，提供了大量的操作和算法，专门用于处理科学计算中的常见问题。`SciPy` 包含的子模块涵盖了统计、优化、积分、线性代数、傅立叶变换、信号和图像处理等多个领域。

安装

安装 `SciPy` 的推荐方式是使用 `pip`：

```bash
pip install scipy
```

**主要模块和功能**

1. **优化 (`scipy.optimize`)**

提供了函数最小化（或最大化）以及根求解算法。非常适合需要进行模型拟合或寻找数学函数最优解的任务。

```python
from scipy.optimize import minimize

def func(x):
    return (x - 3) ** 2

result = minimize(func, x0=0)  # x0 是初始猜测值
print(result.x)  # 最优解
```

2. **积分 (`scipy.integrate`)**

用于计算数学函数的定积分和常微分方程（ODE）的求解。

```python
from scipy.integrate import quad

# 计算定积分
result, _ = quad(lambda x: x ** 2, 0, 1)  # 积分 x^2 从 0 到 1
print(result)  # 结果
```

3. **插值 (`scipy.interpolate`)**

提供了许多对数据进行插值计算的工具，能够帮助创建平滑的数据点序列。

```python
import numpy as np
from scipy.interpolate import interp1d

x = np.arange(0, 10)
y = np.exp(-x/3.0)
f = interp1d(x, y)

new_x = np.linspace(0, 9, 30)
new_y = f(new_x)  # 新的平滑数据
```

4. **线性代数 (`scipy.linalg`)**

包含了所有 `numpy.linalg` 的功能外，还加入了其它高级功能和更优化的算法。

```python
from scipy.linalg import lu

# LU 分解
P, L, U = lu([[1, 2], [3, 4]])
print(L)
print(U)
```

5. **信号处理 (`scipy.signal`)**

用于信号处理的工具，例如滤波器设计、频谱分析和信号处理等。

```python
from scipy.signal import find_peaks

x = np.array([0, 1, 1.5, 2, 1])
peaks, _ = find_peaks(x)
print(peaks)  # 输出峰值的位置
```

6. **统计 (`scipy.stats`)**

提供了大量的统计工具和连续或离散分布的功能。可以进行描述性统计、概率分布分析、检验等。

```python
from scipy.stats import norm

# 正态分布
rv = norm(loc=0, scale=1)  # 均值0，标准差1
print(rv.pdf(0))  # x=0处的概率密度函数值
```

**总结**

`SciPy` 是科学计算中非常核心的库之一，配合 `NumPy` 和 `matplotlib`，可以构建完整的科学计算环境。它的多样性和强大功能使得在多个科学计算领域内，无论是学术研究还是工程应用，`SciPy` 都扮演着非常重要的角色。











