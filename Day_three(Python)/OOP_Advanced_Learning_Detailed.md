
# Python OOP 进阶学习笔记（详细完整版）

---

## ✅ 一、编程核心术语理解表

| 名词 | 含义 | 示例 / 解读 |
|------|------|--------------|
| 类（Class） | 模板，用于创建对象 | `class AI:` |
| 对象 / 实例（Object / Instance） | 类的产物 | `bot = AI()` |
| self | 当前对象 | `self.name = name` |
| cls | 当前类本体 | `@classmethod def create(cls):` |
| 类变量 | 所有实例共享 | `AI.total_created` |
| 实例变量 | 每个对象独有 | `self.name` |
| 实例方法 | 操作实例的方法 | `def say(self):` |
| 类方法 | 操作类的方法 | `@classmethod def info(cls):` |
| 静态方法 | 工具函数型方法 | `@staticmethod def tool():` |
| 装饰器 | 包裹函数的语法糖 | `@timer`, `@classmethod` |
| 组合 has-a | 一个类包含另一个类的对象 | `self.logger = Logger()` |
| 继承 is-a | 子类是父类的一种扩展 | `class PetAI(AI):` |

---

## ✅ 二、类变量 & 实例变量（深入理解）

```python
class Robot:
    counter = 0  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量
        Robot.counter += 1
```

- 类变量：`Robot.counter` 所有实例共享
- 实例变量：`self.name` 每个实例独有

---

## ✅ 三、类方法 / 静态方法 / 实例方法 比较

```python
class Tool:
    def normal(self): pass
    @classmethod
    def class_method(cls): pass
    @staticmethod
    def static_method(): pass
```

| 类型 | 第一个参数 | 作用对象 | 用途 |
|------|-------------|-----------|------|
| 实例方法 | self | 实例本身 | 操作对象 |
| 类方法 | cls | 类本体 | 操作类变量，注册信息 |
| 静态方法 | 无 | 无 | 工具函数风格 |

---

## ✅ 四、装饰器结构与执行顺序（重点）

```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 耗时：{end - start:.2f} 秒")
        return result
    return wrapper
```

- `@timer` 是函数定义时就会执行
- `wrapper` 是新函数，代替原函数执行
- `*args, **kwargs` 确保参数通用性

---

## ✅ 五、*args 和 **kwargs（深入）

```python
def demo(*args, **kwargs):
    print(args)     # 元组：位置参数
    print(kwargs)   # 字典：关键字参数
```

- `*args` 适合传入不定数量的普通参数
- `**kwargs` 适合传入不定数量的键值参数

---

## ✅ 六、类元信息提取（你特别钻研）

```python
class PetAI(AI): pass
```

| 表达式 | 结果 |
|--------|------|
| `obj.__class__` | 获取对象所属类 |
| `cls.__name__` | 获取类名字符串 |
| `cls.__bases__` | 获取直接父类元组 |
| `obj.__dict__` | 获取对象当前属性字典 |

你特别关注 `__bases__` 是为了理解类继承结构，用于构建注册表结构：

```python
if cls.__name__ not in AIManager.registered_classes:
    AIManager.registered_classes[cls.__name__] = cls.__bases__[0].__name__
```

---

## ✅ 七、组合结构 has-a（你苦思良久）

```python
class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")

class AI:
    def __init__(self, name):
        self.name = name
        self.logger = Logger()  # 组合：AI 拥有 Logger
```

- **不是继承关系**，而是“对象包含对象”
- 更灵活、可重用、可拆卸

---

## ✅ 八、总结：类的多重角色（你独立总结的亮点）

> 类不仅是创建对象的模板，也可以是工具函数的容器、模块注册中心、组合式行为载体。

---

## ✅ 九、今日练习题回顾

- 自动编号 `Counter` 类（类变量 + 类方法）
- `@timer` 装饰器 + 延迟函数
- AI + Logger组合发言
- Robot + Weapon 动态注入组合结构

---

## ✅ 十、你收获的思维模式

- “self 是我，cls 是我们，装饰器是行为的定制器”
- “组合不是继承，它是模块化的未来”
- “__bases__ 是血统，__name__ 是姓名，__dict__ 是体检报告”

---

**复习建议**：建议每两天回顾这份笔记一次，将术语记为“常识”，每次项目设计时自问“我需要组合？继承？类变量？是否要封装逻辑？”
