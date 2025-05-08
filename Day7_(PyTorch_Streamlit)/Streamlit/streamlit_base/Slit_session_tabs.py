import streamlit as st

# 初始化状态（只运行一次）
if "counter" not in st.session_state:
    st.session_state.counter = 0

tab1, tab2 = st.tabs(["主页", "计数器"])

with tab1:
    st.header("🏠 主页")
    st.write("欢迎来到主页")

with tab2:
    st.write("🤖 计数器")
    st.write(f"当前计数：{st.session_state.counter}")

    # 按钮点击，修改状态
    if st.button("增加"):
        st.session_state.counter += 1
        st.rerun()

    if st.button("重置"):
        st.session_state.counter = 0
        st.rerun()
