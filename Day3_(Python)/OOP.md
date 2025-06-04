# Python OOP

> 关于 **类(class)** 的本质研究请见 `../notes/Python_Class`

---

## ✅ 术语表

| 名词                             | 含义                     | 示例 / 解读                     |
| -------------------------------- | ------------------------ | ------------------------------- |
| 类（Class）                      | 模板，用于创建对象       | `class AI:`                     |
| 对象 / 实例（Object / Instance） | 类的产物                 | `bot = AI()`                    |
| self                             | 当前对象                 | `self.name = name`              |
| cls                              | 当前类本体               | `@classmethod def create(cls):` |
| 类变量                           | 所有实例共享             | `AI.total_created`              |
| 实例变量                         | 每个对象独有             | `self.name`                     |
| 实例方法                         | 操作实例的方法           | `def say(self):`                |
| 类方法                           | 操作类的方法             | `@classmethod def info(cls):`   |
| 静态方法                         | 工具函数型方法           | `@staticmethod def tool():`     |
| 装饰器                           | 包裹函数的语法糖         | `@timer`, `@classmethod`        |
| 组合 has-a                       | 一个类包含另一个类的对象 | `self.logger = Logger()`        |
| 继承 is-a                        | 子类是父类的一种扩展     | `class PetAI(AI):`              |

---

## ✅ 二、类变量 & 实例变量

```python
class Robot:
    counter = 0  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量
        Robot.counter += 1
```

-   类变量：`Robot.counter` 所有实例共享
    -   是一个动态引用，所有实例访问类变量时，本质上是到类里查找
-   实例变量：`self.name` 每个实例独有
    -   实例赋值变量与类变量同名时会屏蔽类变量

#### 访问类变量

```python
class Foo:
    x = 1

a = Foo()
a.x = 2

"直接访问"
print(Foo.x) # 1

"获取类"
print(type(a).x) # type(a) = <class '__main__.Foo'>

"用class属性"
print(a.__class__.x) # a.__class__ = <class '__main__.Foo'>

"在实例内部访问"
print(self.__class__.x)
print(type(self).x)

"遍历MRO链-应对多重继承"
for cls in a.__class__.__mro__:
    if 'x' in cls.__dict__:
        print(cls.__dict__['x'])
        break
```

---

## ✅ 三、类方法 / 静态方法 / 实例方法 比较

```python
class Tool:
    "实例方法"
    def normal(self): pass

    "类方法"
    @classmethod
    def class_method(cls): pass

    "静态方法"
    @staticmethod
    def static_method(): pass
```

| 类型     | 第一个参数 | 作用对象 | 用途                 |
| -------- | ---------- | -------- | -------------------- |
| 实例方法 | `self`     | 实例本身 | 操作对象             |
| 类方法   | `cls`      | 类本体   | 操作类变量，注册信息 |
| 静态方法 | 无         | 无       | 工具函数风格         |

---

## ✅ 四、装饰器结构

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

-   `@timer` 是函数定义时就会执行
-   `wrapper` 是新函数，代替原函数执行
-   `*args, **kwargs` 确保参数通用性

---

## ✅ 五、\*args 和 \*\*kwargs

```python
def demo(*args, **kwargs):
    print(args)     # 元组：位置参数
    print(kwargs)   # 字典：关键字参数
```

-   `*args` 适合传入不定数量的普通参数
-   `**kwargs` 适合传入不定数量的键值参数

---

## ✅ 六、类元信息提取

```python
class Animal:
    type = "动物"

    def __init__(self):
        self.age = 0

class PetAI(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

# 创建实例
pet = PetAI("小白")

# 类元信息获取示例
print(pet.__class__)        # <class '__main__.PetAI'>
print(PetAI.__name__)       # 'PetAI'
print(PetAI.__bases__)      # (<class '__main__.Animal'>,)
print(pet.__dict__)         # {'name': '小白', 'age': 0}
print(PetAI.__mro__)        # (<class '__main__.PetAI'>, <class '__main__.Animal'>, <class 'object'>)
```

---

## ✅ 七、组合结构 has-a

```python
class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")

class Storage:
    def save(self, data):
        print(f"[SAVE] {data}")

class AI:
    def __init__(self, name):
        self.name = name
        self.logger = Logger()     # 组合：记录日志功能
        self.storage = Storage()   # 组合：数据存储功能

    def process(self, data):
        self.logger.log(f"处理数据: {data}")
        result = f"AI {self.name} 处理了 {data}"
        self.storage.save(result)
        return result

# 使用示例
bot = AI("小智")
bot.process("用户输入")
```

-   **不是继承关系**，而是"对象包含对象"
-   更灵活、可重用、可拆卸
-   每个组件都专注于自己的功能

## ✅ 八、继承结构 is-a

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}：汪汪！"

class Cat(Animal):
    def speak(self):
        return f"{self.name}：喵～"

class Robot:
    def charge(self):
        print("充电中...")

class RobotDog(Dog, Robot):  # 多重继承
    def speak(self):
        return f"机器狗{self.name}：汪汪！beep!"

# 使用示例
animals = [
    Dog("小黑"),
    Cat("咪咪"),
    RobotDog("铁头")
]

for animal in animals:
    print(animal.speak())

# 多重继承特性
robo_dog = RobotDog("铁头")
robo_dog.charge()  # 来自Robot类
```

-   继承表示"是一种"关系：狗是动物的一种
-   支持方法重写：每种动物都有自己的叫声
-   支持多重继承：机器狗既是狗也是机器
