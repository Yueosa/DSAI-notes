import streamlit as st
import pandas as pd

st.title("📊 数据上传与可视化分析工具")

# 1. 文件上传
uploaded_file = st.file_uploader("请选择一个 CSV 文件", type=["csv"])

# 2. 文件成功上传
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 文件上传成功！")

    # 3. 数据预览
    st.subheader("📋 数据预览")
    st.dataframe(df)

    # 4. 数据摘要
    st.subheader("📏 数据摘要")
    st.write(f"数据维度：{df.shape[0]} 行 × {df.shape[1]} 列")
    st.write("列名：", df.columns.tolist())

    st.write("🧼 缺失值统计：")
    st.write(df.isna().sum())

    # 5. 数值列自动筛选
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if numeric_cols:
        st.subheader("📈 选择一个数值列进行可视化：")
        selected_col = st.selectbox("请选择列：", numeric_cols)

        # 6. 可视化图表选择
        chart_type = st.radio("选择图表类型", ["折线图", "柱状图", "区域图"])

        if chart_type == "折线图":
            st.line_chart(df[selected_col])
        elif chart_type == "柱状图":
            st.bar_chart(df[selected_col])
        elif chart_type == "区域图":
            st.area_chart(df[selected_col])

    else:
        st.warning("⚠️ 没有找到可用于可视化的数值列。")
else:
    st.info("👈 请先上传一个 CSV 文件~")
