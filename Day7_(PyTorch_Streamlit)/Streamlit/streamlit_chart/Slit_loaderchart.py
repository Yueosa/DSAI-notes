import streamlit as st
import pandas as pd

st.title("📊 多列对比图表演示")

uploaded_file = st.file_uploader("上传一个 CSV 文件", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

    if numeric_cols:
        st.subheader("📌 多列选择并绘图")

        # 多选框：选出你想画的列
        selected_columns = st.multiselect("选择要展示的列：", numeric_cols, default=numeric_cols[:2])

        if selected_columns:
            chart_type = st.radio("选择图表类型：", ["折线图", "柱状图", "区域图"])
            st.write("你选择了：", selected_columns)

            if chart_type == "折线图":
                st.line_chart(df[selected_columns])
            elif chart_type == "柱状图":
                st.bar_chart(df[selected_columns])
            elif chart_type == "区域图":
                st.area_chart(df[selected_columns])
        else:
            st.warning("请至少选择一个列来进行绘图~")
    else:
        st.warning("⚠️ 没有数值列可用于绘图。")

"演示 多列对比图表"