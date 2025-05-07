import streamlit as st

st.sidebar.title("🎛️ 控制面板")
name = st.sidebar.text_input("请输入你的昵称：")
age = st.sidebar.slider("选择你的年龄", 0, 100)

st.write(f"你好，{name}，你今年 {age} 岁！")

"演示 侧边栏"