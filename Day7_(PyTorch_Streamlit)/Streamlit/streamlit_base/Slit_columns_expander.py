import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 输入")
    name = st.text_input("名字")

with col2:
    st.subheader("📤 输出")
    if name:
        st.success(f"你好，{name}！")

with st.expander("📂 查看更多信息"):
    st.write("这里是一些额外的说明文字")
    st.code("print('Hello Streamlit')", language='python')

"演示 分栏 和 可折叠区域"