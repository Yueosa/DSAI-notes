# Streamlit
## 是一个很简单的pyhton库, 用几行代码就能创建一个网页应用

---

### 常用组件

| 类型 | 方法 | 说明 |
| --- | --- | ---| 
| 文本展示 | `.title()` `.write()` `.header()` `.subheader()` `.text()` `.markdown()` `.caption()` `.code()` `.latex()` | 显示标题, 内容, 富文本 |
| 消息提示 | `.success()` `.warning()` `.error()` `.info()` | 用于打印消息 |
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
#### 动态容器`.container()`
    创建一块可以随时追加更新的页面块, 不刷新整个页面
    语法是 st.container() 实例化, 之后直接用 container.write() 等方法追加内容
#### 临时占位符`.empty()`
    创建一块可以随时覆盖更新的页面块, 不刷新整个页面
    语法是 st.empty() 实例化, 之后直接用 empty.write() 等方法覆盖更新
---

### 进阶 | 数据可视化
| 图表类型 | 对应函数 | 适合什么用 |
| - | - | - |
| 折线图 | `.line_chart()` | 展示之间变化趋势, 如温度、价格等 |
| 柱状图 | `.bar_chart()` | 分类比较, 如各班成绩、销售数量 |
| 区域图 | `.area_chart()` | 堆叠变化, 如流量组成、比例变化 |
| 自定义图 | `.pyplot()` `.altair_chart()` | 用 matplotlib、Altair 等画复杂图 |

    接受DataFrame、Series 或 二维 numpy 数组

---

### 进阶 | 文件上传 | 数据处理

| 功能 | 方法 |
| - | - |
| 上传文件 | `.file_uploader()` |
| 读取CSV、TXT | `pandas.read_csv()` `.read_table()` |
| 显示表格 | `.dataframe()` `.table()` |
| 预览数据形状/列名/缺失值 | `.shape` `.columns` `.isna().sum()` |

---

### 进阶 | 状态管理 | 多页面

#### 状态管理`.session_state`
    是一个全局字典对象
    用来保存跨页面和多次交互的状态

#### 页面切换`.tabs()`
    创建共存的多标签页面
    多标签页面并行存在, 不会刷新页面

---

### 文件展示(图片/音频/视频)

#### 图片展示`.image()`
    接受参数 path(位置参数), caption, width等等
    也可以上传展示:
```python
uploader_file = st.file_uploader("选择一张图片", type=["png", "jpg", "jpeg"])
if uploader_file:
    st.image(uploader_file, caption="上传的图片", width=300)
else:
    st.info("请上传正确格式的图片")
```

#### 音频展示`.audio()`
```python
audio_file = st.file_uploader("选择一个音频文件", type=["mp3", "wav", "ogg"])
if audio_file:
    st.audio(audio_file, format="audio/mp3")
else:
    st.info("请上传正确格式的音频")
```

#### 视频展示`.video()`
```python
video_file = st.file_uploader("选择一个视频文件", type=["mp4", "webm", "mov"])
if video_file:
    st.video(video_file)
else:
    st.info("请选择正确格式的视频")
```

---

### 表单提交

#### `.from()`
    将多个输入控件组合在一起, 实现一次性提交
```python
with st.from("message_from"):
    username = st.text_input("你的名字")
    age = st.number_input("年龄", min_value=0, max_value=100)
    bio = st.text_area("个人简介")

    submitted = st.from_submit_button("提交")
if submitted:
    st.success(f"{usernmae}-{age}-{bio}")
```

