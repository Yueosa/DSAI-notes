import streamlit as st

st.title("小型参数模板")

col1, col2, col3 = st.columns(3)


a = st.sidebar.number_input("输入第一个数字:")


b = st.sidebar.number_input("输入第二个数字:")

with col1:
    if st.button("加法"):
        st.write(a, "+", b, "=", a + b)

with col2:
    if st.button("减法"):
        st.write(a, "-", b, "=", a - b)

with col3:
    if st.button("乘法"):
        st.write(a, "*", b, "=", a * b)

with st.expander("展开查看更多信息:"):
    st.write("其实什么都没有, 只是写着玩")
