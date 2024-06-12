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



## Python基础知识

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

### Python作用域 (局部作用域, 全局作用域, 嵌套作用域, 内置作用域)



### Python模块



### Python类



### Python文件操作



### Python异常处理



### Python标准库



## Python高级知识

### Python面向对象



### Python装饰器



### Python利用模块实现单例




### Python调用C代码



### C调用Python代码



### Python Lambda



### Python Argparse



### Python处理csv文件



### Python对象引用



### Python Matplotlib



### Python Pandas



### Python Scipy



### Python Numpy











