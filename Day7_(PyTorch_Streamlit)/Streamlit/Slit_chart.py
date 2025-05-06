import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Streamlit 可视化练习 - 折线图")

# 创建模拟数据
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# 展示表格
st.write("这是模拟数据：", df)

# 画折线图
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
