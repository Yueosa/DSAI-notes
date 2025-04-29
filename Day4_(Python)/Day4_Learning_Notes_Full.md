# 🧠 Python 学习笔记 · Day 4 · 2025年4月25日

> 本文记录了我在第四天的学习内容，涵盖 Python 中的推导式、高阶函数、数据结构（栈/队列）、生成器与迭代器等核心知识点，带有详细示例与我的理解总结，供日后复习与参考使用。

---

## ✅ 一、列表推导式（List Comprehension）

### 📌 基本语法

```python
[表达式 for 变量 in 可迭代对象 if 条件]
```

等价于：

```python
result = []
for 变量 in 可迭代对象:
    if 条件:
        result.append(表达式)
```

### ✅ 示例：

```python
nums = [1, -3, 4, 0, -5, 9]
positive_nums = [x for x in nums if x > 0]
print(positive_nums)  # [1, 4, 9]
```

### 💡 我的理解：

- 推导式语法是 `for` 开头，然后 `if` 条件，再到前面的表达式。
- 表达式部分是“输出”的内容，本质上等价于 `append()` 操作。
- 可读性强、写法紧凑，是 Pythonic 编程风格的重要体现。
> 列表推导式本质是一种 `for + if + append()` 的语法糖，执行顺序是先 `for` 再 `if`，最后表达式收集结果。表达式部分看起来像 `result = x`，但实际上等价于 `result.append(x)`。

---

## ✅ 二、嵌套推导式与多条件过滤

### 📌 示例：九九乘法表（只输出下三角）

```python
table = [f"{i} * {j} = {i * j}" for i in range(1, 10) for j in range(1, 10) if j <= i]
```

### 💡 我的理解：

- 多个 `for` 会嵌套执行，**执行顺序：先外层，后内层，再执行 if 判断与表达式**。
- 嵌套 `for` 不宜太多层，否则影响可读性。

---

## ✅ 三、字典 / 集合 推导式

### 🧱 字典推导式

```python
s = 'hello'
s_dict = {ch: s.count(ch) for ch in set(s)}
print(s_dict)  # {'h':1, 'e':1, 'l':2, 'o':1}
```

- `set(s)` 用于去重，避免重复统计
- `.count()` 用于统计字符频率

### 🧱 集合推导式

```python
nums = [1, 2, 3, 3, 2, 4]
unique_evens = {x for x in nums if x % 2 == 0}
print(unique_evens)  # {2, 4}
```

- 集合自动去重、无序，不能使用下标访问。

---

## ✅ 四、字符串常用方法

### 🔹 `str.count(sub)`

统计某字符在字符串中出现的次数：

```python
"hello".count("l")  # 2
```
>这个方法在任何支持的可迭代对象上都可以用,用来统计sub出现的次数,返回一个int数

### 🔹 `str.capitalize()`

返回首字母大写的新字符串：

```python
"hello".capitalize()  # "Hello"
```

### 💡 我的理解：

- 字符串是一个“不可变字符列表”，可以看但不能改。
- `.capitalize()` 是对字符串的“重构”，不会修改原值。
- Python 字符串很多方法都返回新值，这是函数式设计的体现。

---

## ✅ 五、lambda 表达式与高阶函数

### 📌 lambda 基础语法：

```python
lambda 参数: 表达式
```

### ✅ 示例：平方列表中的每个数

```python
nums = [1, 2, 3]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9]
```

---

### 📌 filter 示例：筛选偶数

```python
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]
```

### 💡 我的理解：

- `lambda` 是匿名函数，常与 `map()` / `filter()` 一起用。
- 非常适合传递“一次性逻辑”。
- 本质上它也是函数，只不过没有名字。

---

## ✅ 六、栈（Stack）结构

### 📌 定义：先进后出（LIFO）

### ✅ 基本操作：

| 方法 | 说明 |
|------|------|
| `push(x)` | 入栈 |
| `pop()` | 出栈 |
| `peek()` | 查看栈顶元素（不移除） |
| `is_empty()` | 判断是否为空 |

### ✅ 示例结构（使用 list 模拟）：

```python
stack = []
stack.append("A")
stack.append("B")
print(stack.pop())  # B
```

### 💡 我的理解：

- 栈适合用于“撤销”、“回退”类型的场景。
- 练习中，我用它来保存任务历史记录，实现了任务完成轨迹。

---

## ✅ 七、队列（Queue）结构

### 📌 定义：先进先出（FIFO）

使用 `collections.deque` 结构实现更高效：

```python
from collections import deque
q = deque()
q.append("任务1")
print(q.popleft())  # "任务1"
```

### ✅ 基本方法：

| 方法 | 说明 |
|------|------|
| `append(x)` | 入队（末尾） |
| `popleft()` | 出队（开头） |
| `peek()` | 查看队首 |

### 💡 我的理解：

- `deque` 是双端队列，底层结构不是 list，而是类似双向链表。
- 它避免了 `.pop(0)` 带来的 O(n) 性能损耗，非常适合做消息队列。

---

## ✅ 八、生成器（Generator）与迭代器（Iterator）

### 📌 概念区分：

| 名词 | 定义 | 特性 |
|------|------|------|
| 迭代器 | 拥有 `__iter__()` 和 `__next__()` 的对象 | 一次性、惰性加载 |
| 生成器 | 一种快速创建迭代器的语法糖 | `(x for x in ...)` 或 `yield` |

---

### ✅ 示例：生成器表达式

```python
gen = (x * 2 for x in range(3))
print(next(gen))  # 0
print(next(gen))  # 2
```

---

### ✅ 示例：生成器函数

```python
def gen_nums():
    for i in range(3):
        yield i

g = gen_nums()
print(next(g))  # 0
```

---

### 💡 我的理解：

- 迭代器就是一个“单向只读流”，取过就没了，节省内存。
- 生成器是快速定义这类流的工具。
- 它们常用于数据流处理、大规模文件读取、网络数据处理等场景。

---

