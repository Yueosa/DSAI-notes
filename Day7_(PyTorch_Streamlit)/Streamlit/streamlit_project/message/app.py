import streamlit as st
import json
from datetime import datetime
import os
import uuid

DATA_PATH: str = "messages.json"
ADMIN_PASSWORD = "123456"  # ⚠️ 修改为你的管理员密码

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
    message_list = load_messages()
    message_list = [msg for msg in message_list if msg["id"] != id]
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(message_list, f, ensure_ascii=False, indent=4)


def name_list():
    name_list = load_messages()
    search_list = {msg["name"] for msg in name_list}
    return search_list


st.set_page_config(page_title="留言板系统", layout="wide")
st.title("📮 迷你留言板系统")

# 🔒 设置管理员登录状态
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False

# 用于存储删除操作的状态
if "delete_msg" not in st.session_state:
    st.session_state["delete_msg"] = None

# 侧边栏：管理员登录区域
with st.sidebar:
    st.subheader("管理员登录")
    admin_input = st.text_input("输入管理员密码：", type="password")

    if st.button("登录"):
        st.session_state["is_admin"] = admin_input == ADMIN_PASSWORD
        if st.session_state["is_admin"]:
            st.success("登录成功")
        else:
            st.error("密码错误")

    if st.session_state["is_admin"]:
        st.info("管理员模式：开启 ✅")
    else:
        st.warning("管理员模式：关闭 ❌")

st.markdown("---")

# ✅ 留言区
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
            st.warning("请填写完整的内容再提交哦~")

st.markdown("---")
st.subheader("📜 历史留言")

# ✅ 显示删除成功信息
if st.session_state["delete_msg"]:
    st.success(st.session_state["delete_msg"])
    st.session_state["delete_msg"] = None

# ✅ 展示历史留言
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
                margin-bottom: 10px;
            '>
            <strong>{msg['name']}</strong> 说：{msg['message']}<br>
            <span style='font-size: 12px; color: gray;'>🕒 {msg['timestamp']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_btn:
        if st.session_state["is_admin"]:
            if st.button("🗑️", key=f"del_{msg['id']}"):
                del_messages(msg['id'])
                st.session_state["delete_msg"] = "留言已删除"
                st.rerun()
                