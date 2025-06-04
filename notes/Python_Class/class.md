# CPython 类的底层机制

---

### | 循环自举的类型系统

-   **Type 与 Object 的关系**：
    -   Type 是 Object 的子类：`issubclass(type, object) # True`
    -   Object 是 Type 的实例：`isinstance(object, type) # True`
    -   Type 自身：`type(type) is type` （自举结构）

### | 类的创建机制

以下两种方式完全等价：

**1. 常规类定义（语法糖）：**

```python
class AI(object, metaclass=type):
    def __init__(self, name: str) -> None:
        self.name: str = name
```

**2. 使用 type()直接创建：**

```python
def __init__(self, name: str) -> None:
    self.name: str = name

AI = type("AI", (object,), {"__init__": __init__})
```

### | 底层实现细节

1. **CPython 实现**：

    - PyType_Type (type)
    - PyBaseObject_Type (object)
    - type_new 负责内存分配、布局和继承链

2. **类型注解**：

```python
from typing import Type

object: type
type: type
```

### | 关键要点

-   Type 主导类的创建过程
-   Object 主导方法和属性的继承
-   Python 通过 object/type 的循环自举实现"一切皆对象"
-   这种设计支持灵活的元编程能力

---

> 注：这种设计使 Python 在保持简洁性的同时获得了强大的面向对象特性。
