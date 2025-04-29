import streamlit as st
import json
from datetime import datetime
import os
import uuid

DATA_PATH: str = "messages.json"


if not os.path.exists(DATA_PATH):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)


def load_messages():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_messages(new_msg):
    messages = load_messages()
    messages.append(new_msg)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)


def del_messages(id):
    message_list: list = load_messages()
    for i in message_list:
        if i["id"] == id:
            message_list.remove(i)
    with open(DATA_PATH, "w", encoding="utf-8")as f:
        json.dump(message_list, f, ensure_ascii=False, indent=4)


def name_list():
    name_list = load_messages()
    search_list = {msg["name"] for msg in name_list}
    return search_list



st.title("📮 迷你留言板系统")

with st.expander("编写留言"):
    name = st.text_input("你的名字: ")
    message = st.text_area("你想说的话:  ")

    if st.button("📬 提交留言"):
        if name.strip() and message.strip():
            id = str(uuid.uuid4())
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_messages({"id": id, "name": name, "message": message, "timestamp": timestamp})
            st.success("留言已提交, 刷新查看~")
        else:
            st.success("请填写完整的内容再提交哦~")

with st.expander("搜索留言"):
    ...
st.sidebar.write(f"**查看发言人**")
search_list = name_list()
for i in search_list:
    st.sidebar.markdown(
                f"""
                <div style='
                    background-color: #f0f2f6;
                    padding: 10px;
                    border-radius: 10px;
                    box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
                    margin-bottom: 5px;
                '>
                <strong>{i}</strong>
                </div>
                """,
                unsafe_allow_html=True
            )


with st.expander("历史记录"):
    st.markdown("---")
    st.subheader("📜 历史留言")

    for msg in reversed(load_messages()):
        col_text, col_btn = st.columns([9, 1])

        with col_text:
            st.markdown(
                f"""
                <div style='
                    background-color: #f0f2f6;
                    padding: 10px;
                    border-radius: 10px;
                    box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
                    margin-bottom: 5px;
                '>
                <strong>{msg['name']}</strong> 说：{msg['message']}<br>
                <span style='font-size: 12px; color: gray;'>🕒 {msg['timestamp']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col_btn:
            if st.button("🗑️", key=f"del_{msg['id']}"):
                del_messages(msg['id'])
                st.success("留言已删除~")
                st.rerun()

