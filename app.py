import streamlit as st
import time

# 页面标题
st.set_page_config(page_title="Marvin零度", layout="centered")
st.title("🛠 Marvin零度")

# 左侧菜单
menu = st.sidebar.radio("选择功能", ["过检测", "开启外挂", "降低版本"])

# ===== 功能1：过检测 =====
if menu == "过检测":
    st.subheader("环境检测中...")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)
    st.success("环境安全 ✅")

# ===== 功能2：开启外挂 =====
elif menu == "开启外挂":
    st.subheader("选择游戏")
    game = st.selectbox("游戏列表", ["无畏契约", "第五人格", "我的世界"])
    toggle = st.checkbox("开启")
    if toggle:
        st.success(f"{game} 开启成功 ✅")
    else:
        st.info("未开启")

# ===== 功能3：降低版本 =====
elif menu == "降低版本":
    st.subheader("选择 iOS 版本")
    version = st.selectbox("版本", [f"iOS {i}" for i in range(10, 18)])
    if st.button("开始更改"):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)
        st.success(f"{version} 更改成功 ✅")
