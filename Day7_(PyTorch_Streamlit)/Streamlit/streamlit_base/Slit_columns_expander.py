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


st.title("📦 动态容器 - st.container() 示例")

container = st.container()

container.write("这是容器中的初始内容")

st.write("这是页面其他内容")

if st.button("更新容器内容"):
    container.write("容器内容已更新！")


st.title("🔄 覆盖式显示 - st.empty() 示例")

placeholder = st.empty()

placeholder.write("初始内容：这是第一条信息")

if st.button("更新内容"):
    placeholder.write("覆盖后的内容：这是新的信息")

"演示 分栏, 可折叠区域, 动态容器 和 临时占位符"