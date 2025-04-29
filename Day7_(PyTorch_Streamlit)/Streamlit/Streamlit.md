# Streamlit
## 是一个很简单的pyhton库, 用几行代码就能创建一个网页应用

---

### 常用组件

| 类型 | 方法 | 说明 |
| --- | --- | ---| 
| 文本展示 | `.title()` `.write()` `.markdown()` | 显示标题, 内容, 富文本 |
| 输入框 | `.text_input()` `.text_area()` | 用户输入内容(文本) |
| 按钮 | `.button()` | 用户点击触发事件 |
| 单选, 多选 | `.radio()` `.checkbox()` `.selectbox()` | 做选项选择 |
| 数值类输入 | `.slider()` `.number_input()` | 选数值区间或指定值 |
| 文件上传 | `.file_uploader()` | 上传图片, CSV, TXT |
| 图表展示 | `.line_chart()` `.bar_chart()` `.pyplot()` | 可视化数据 |

>Streamlit中只要用户有交互动作, 就会从头开始运行python脚本

#### 示例代码
```python
import streamlit as st
import random

st.title("🎭 我是谁？Streamlit 自我介绍机")

# 文字输入
name = st.text_input("请输入你的名字：")

# 随机生成标签池
labels = [
    "未来的全栈工程师 💻",
    "深藏不露的算法大牛 🧠",
    "热爱创造的艺术灵魂 🎨",
    "只会写 bug 的人类调参器 🐞",
    "不会卷但很会睡觉 🛌",
    "神秘的学习机器 🤖"
]

# 按钮触发
if st.button("生成我的头衔！"):
    if name.strip():
        tag = random.choice(labels)
        st.success(f"{name}，你是一位「{tag}」！")
    else:
        st.warning("请先输入你的名字！")

```

---

### 页面布局 | 交互控制

#### 侧边栏`.sidebar`
    可以把内容放到左边的可展开侧边栏上
    语法是 streamlit.sidebar.组件()
#### 多栏结构`.columns()`
    将内容水平排列
    语法是使用 col1, col2 = st.columns(2) 创建多栏
    with col1 向分栏加入组件
#### 可折叠区域`.expander()`
    让一些内容默认隐藏, 需要点击展开
    语法是 with streamlit.expander()