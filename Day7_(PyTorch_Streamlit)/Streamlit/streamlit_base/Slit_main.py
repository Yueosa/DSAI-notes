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

"演示 输入 和 按钮"