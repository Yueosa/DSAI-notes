import streamlit as st

tab_image, tab_video, tab_audio = st.tabs(["图片展示", "视频展示", "音频展示"])

with tab_image:
    st.header("🖼️ 图片展示")
    url = st.text_input("输入URL")
    if url:
        st.image(url, caption="从URL来的图片", width=700)
    
    st.write("或者从本地上传")
    image_file = st.file_uploader("选择一张图片", type=["png", "jpg", "webp"])
    if image_file:
        st.image(image_file, caption="本地上传的图片", width=700)
    else:
        st.success("快上传点什么喵... ...")

with tab_audio:
    st.header("🎼 音频展示")
    st.write("从本地上传")
    audio_file = st.file_uploader("选择一个音频", type=["mp3", "wav", "ogg"])
    if audio_file:
        st.audio(audio_file, format="audio/mp3")
    else:
        st.success("快上传点什么喵... ...")

with tab_video:
    st.header("🎥 视频播放")

    video_file = st.file_uploader("选择一个视频文件", type=["mp4", "webm", "mov"])
    if video_file:
        st.video(video_file)
    else:
        st.success("快上传点什么喵... ...")
