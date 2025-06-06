# 🌟 Python 深度学习笔记 - 2025-04-26

---

## ✅ 今日完成内容概览

### 1. 堆与优先级队列（PriorityQueue）

- 🧠 **深入源码探索**：阅读了 `heapq` 模块中 `heappush` 和 `_siftdown` 的底层实现。
  - 理解了最小堆如何通过不断交换节点，维护根节点最小的结构特性。
  - 明确了为什么插入元素用 `(priority, index, item)` 的元组形式，index 解决了同优先级元素的顺序问题。

- 🛠️ **自主封装**：
  - 编写了 `Tool` 类进行 `_bubble_up` 操作，手动实现了小型堆的维护。
  - `Weiba` 类中管理了任务列表，实现了 push / pop / peek / is_empty / size 功能。

- ❓ **深入提问与理解**：
  - 思考 `heapq` 返回值和内部堆结构的维护方式。
  - 分析 `Any` 类型在 heapq 参数声明中的意义（泛型处理的合理性）。
  - 手动推导 pop 应该取堆顶元素的正确思路（而不仅仅是 list.pop()）。

---

### 2. 函数进阶：`*args` 和 `**kwargs`

- 🧠 **灵活参数传递机制**：
  - `*args`：打包位置参数为元组。
  - `**kwargs`：打包关键字参数为字典。
  - 掌握了函数定义参数的顺序规范：固定参数 → *args → 默认参数 → **kwargs。

- ❓ **独立思考**：
  - 理解列表推导式中 `for` 和 `if` 的执行顺序（先for后if，再收集表达式值）。
  - 把 `lambda` 临时函数和 JS 中闭包思想做了类比，初步理解闭包意义。

---

### 3. 闭包（Closure）与作用域深入

- 🧠 **掌握闭包本质**：
  - 闭包是“函数 + 外部变量环境”的组合。
  - 内部函数持有外层函数的局部变量，即使外层函数早已执行完毕。

- 🔥 **作用域关键字**：
  - `global`：函数内部声明修改**全局变量**。
  - `nonlocal`：内部函数声明修改**外层局部变量**。

- ❓ **深入提问与扩展**：
  - 记起 Java 的作用域控制，提出 Python 作用域与 Java 作用域管理的差异。
  - 进一步明确：Python 里只有函数/类/模块建立新作用域，`if/for/while` 不建立作用域！

- 📌 **总结**：
  - 作用域穿透仅有 `global` 和 `nonlocal`。
  - Python 是动态作用域链查找，块语句不会切断作用域。

---

### 4. 文件操作（with open）与上下文管理器

- 🧠 **标准模式掌握**：
  - 使用 `with open(file, mode, encoding)` 进行文件读写，自动管理资源释放。
  - `"r"` 读取模式、`"w"` 写入模式（覆盖）、`"a"` 追加模式（文件末尾添加内容）。

- 🔥 **深入 with 原理**：
  - `with` 语法实际上调用了对象的 `__enter__()` 和 `__exit__()` 方法。
  - `open` 返回的文件对象实现了上下文协议，自动保证异常发生时也能正常关闭文件。

- ❓ **提出并发现笔误**：
  - 指出之前讲解中的 `file.append()` 是错误描述，应为 `file.write()` 配合 `'a'` 模式追加内容。

- 📜 **实战项目**：
  - 写情书保存系统：`Sakura.txt` 文件追加写入。
  - 小型记事本系统：`my_notes.txt` 支持追加与读取命令交互。

---

### 5. JSON 文件操作

- 🧠 **掌握 JSON 模块使用**：
  - `json.dump(data, file, ensure_ascii=False, indent=4)`：保存结构化数据。
  - `json.load(file)`：读取 JSON 文件内容转为 Python 对象。

- 📜 **实战项目**：
  - 编写 `JsonHandler` 类，实现个人信息存取管理器。
  - 使用生成器 (`yield`) 循环切换读写模式，体验懒加载与流式数据处理。

- ❓ **错误修正**：
  - 识别出文件名写错（'josn' -> 'json'），强调细节规范的重要性。

---
