
# 🐍 Python 学习笔记（基础语法篇）

## ✅ 学习目标
掌握 Python 的基础语法、数据结构、函数设计与常见内建方法，为数据处理、模型训练等上层任务打好语言基础。

---

## 📌 基础语法掌握

### 🔹 变量与类型
```python
name = "Alice"    # str
age = 18          # int
score = 92.5      # float
is_ready = True   # bool
```
使用 `type(x)` 查看变量类型。

---

### 🔹 输入输出
```python
name = input("请输入姓名：")
print("你好,", name)
```

#### `f""` 字符串格式化（推荐）
```python
f"你好，{name}，你今年 {age} 岁了！"
```
等价于：
```python
"你好，{}，你今年 {} 岁了！".format(name, age)
```

#### 保留小数位写法：
```python
f"{score:.2f}"  # 保留2位小数
```

---

### 🔹 条件语句
```python
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

---

### 🔹 循环结构

#### `for` 遍历
```python
fruits = ["🍎", "🍌", "🍓"]
for fruit in fruits:
    print(fruit)
```

#### `enumerate()` 推荐：同时获得索引和值
```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

#### `while` 循环
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

---

## 📦 数据结构

### 🔸 列表 List

创建、操作、删除：
```python
fruits = ["🍎", "🍌", "🍓"] # 定义列表
fruits.append("🍇") # 朝列表最后加入
fruits.insert(1, "🍍") # 朝指定位置插入(插入到索引1, 其他元素往后挪一位)
fruits.pop() # 删除并返回最后一个值
fruits.pop(0) # 删除并返回第一个值
```

#### ✅ 列表推导式（新技能）
```python
nums = [3, -5, 7, -2]
nums = [i for i in nums if i > 0]  # 保留正数
```

#### ✅ 删除元素（推荐倒序或推导式）
```python
# 错误写法：边遍历边删除
for i in nums:
    if i <= 0:
        nums.remove(i)  # 可能漏删

# 正确写法：倒序删
for i in range(len(nums)-1, -1, -1):
    if nums[i] <= 0:
        nums.pop(i)
```

---

### 🔸 字典 Dict

```python
student = {"name": "小明", "age": 18}
student["score"] = 95      # 添加
del student["age"]         # 删除

for k, v in student.items():
    print(k, v)
```

#### 字典取值方法：
- `.keys()`：所有键
- `.values()`：所有值
- `.items()`：键值对元组

⚠️ 字典**没有下标**，不能用 `dict[0]`

---

## 🧠 函数定义与类型注解

```python
def greet(name: str) -> str:
    return f"你好，{name}"
```

```python
from typing import List, Tuple

def get_top_scores(scores: List[int]) -> int:
    return max(scores)

def get_pos_data() -> Tuple[List[int], List[int]]:
    return [1,2], [3,4]
```

- `-> int`：返回值是整数
- `-> tuple[list, list]`：返回多个列表
- 注解不强制，但推荐，尤其是工程项目中

---

## ✅ 新技能总结

| 技能 | 说明 |
|------|------|
| `f"{x:.2f}"` | 字符串格式化（格式糖） |
| `.isdigit()` | 判断字符串是否全为数字 |
| `.strip()` | 去除字符串首尾空格 |
| `enumerate()` | 同时获取索引和值 |
| `del dict[key]` | 删除字典项 |
| 列表推导式 | 精简写法创建新列表 |
| `.items()` | 遍历字典键值对 |

---
