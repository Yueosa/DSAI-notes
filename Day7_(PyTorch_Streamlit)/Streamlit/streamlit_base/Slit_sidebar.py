import streamlit as st

# 侧边栏导航
page = st.sidebar.selectbox(
    "选择页面",
    ["主页", "活在17岁的魔法"]
)

# 根据选择显示页面内容
if page == "主页":
    st.header("🏠 主页")
    st.write("欢迎来到主页")
elif page == "活在17岁的魔法":
    st.sidebar.title("🎛️ 控制面板")
    st.header("🩷 我的信息")
    name = st.sidebar.text_input("请输入你的昵称：")
    age = st.sidebar.slider("选择你的年龄", 0, 100)
    if age >= 18:
        st.write(f"你好, {name}, 你怎么死了")
    else:
        st.write(f"你好，{name}，你今年 {age} 岁！")

"演示 侧边栏"