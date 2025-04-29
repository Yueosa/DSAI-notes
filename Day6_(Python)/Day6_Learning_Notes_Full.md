# Day 6 学习总结

📅 **日期**：2025年4月27日  
📚 **主题**：Deque、函数式编程深入、流式数据清洗、小型数据清洗模块封装

## 一、Deque（双端队列）

### 核心要点
* `append()` / `appendleft()`：从右/左端添加元素
* `pop()` / `popleft()`：从右/左端移除元素
* `rotate(n)`：元素旋转
  - n > 0：右旋 (元素向右滑动)
  - n < 0：左旋
* `maxlen`：限制队列长度，超过会自动删除最旧元素

### 个人理解
> Deque 可以算是一种"顺序可以自由移动的队列"，适合任务队管理、滑动窗口计算、小型系统日志等场景

## 二、函数式编程深入：流式处理

### 核心要点
* `map(func, iterable)`：将 func 应用于 iterable 每个元素
* `filter(func, iterable)`：保留返回 True 的元素
* 全部是惰性处理（未立即返回），需要通过 for、list()、next() 才真正执行

### 个人理解
> yield、map、filter 这些都是单向性的流式处理，不是一次性输出，而是在需要时才一步步生成
- `list(generator)` 是强制把流合成一个结果，之后生成器就被消耗了
- 每一次 `next()` 都是真正的「命令」，控制流式前进

## 三、Iterator 与 Iterable 分清

### 核心要点
* Iterable：有 `__iter__()` 的，可以被 for 遍历
* Iterator：有 `__iter__()` 和 `__next__()` 的，可以被 next() 控制
* range、list、dict 等是 Iterable，需要通过 iter() 转成 Iterator 才能 next()
```python
from collections.abc import Iterable, Iterator
if isinstance(item, Iterable):
    print(item, '是可迭代对象')
elif isinstance(item, Iterator):
    print(item, '是迭代器')
else:
    print('什么都不是哦')
```


### 个人理解
> 能 for 是 Iterable，能 next 是 Iterator
- 生成器、map、filter 是天然的 Iterator，不需要转换
- 流式思维：将进程按需分段交付，而不是一次性全量处理，优化内存和性能

## 四、小型数据清洗模块封装

### 核心要点
* 为了增强系统性和可复用性，将 filter 和 map 的模型封装成类
* `__init__`：传入清洗规则和转换规则（函数）
* `clean(data)`：进行流式清洗，添加 yield，一步步输出

### 个人理解
> 写死在类里的规则是固定模型，选择外部传入规则是可扩展模型，面向处理系统的思维！
- 开发时，要按需选择是写死（简单项目），还是可提供外部调用（复杂应用）

## 📝 综合评价

1. 已经能理解流式处理、惰性处理、单向性系统的核心思想
2. 已经熟悉 Python 中的 Iterable 和 Iterator 区别，开始担当系统设计者的思维
3. Deque / 生成器 / map、filter 的综合应用已经能简单清洗数据流，有力量进入更复杂的设计

> 今天第6天学习完结！青春不辛，努力不虚实！（握拳）✨
