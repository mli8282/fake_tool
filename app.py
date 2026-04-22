import streamlit as st
import time

st.set_page_config(page_title="系统工具", layout="centered")
st.title("🛠 系统工具")

# 定义页面状态
if 'page' not in st.session_state:
    st.session_state.page = 'menu'

# 返回菜单按钮
def back_to_menu():
    st.session_state.page = 'menu'

# ===== 主菜单 =====
if st.session_state.page == 'menu':
    st.subheader("请选择功能")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("过检测"):
            st.session_state.page = 'check'
    with col2:
        if st.button("开启外挂"):
            st.session_state.page = 'hack'
    with col3:
        if st.button("降低版本"):
            st.session_state.page = 'downgrade'

# ===== 功能1：过检测 =====
elif st.session_state.page == 'check':
    st.subheader("环境检测中...")
    progress = st.progress(0)
    for i in range(101):
        time.sleep(0.01)  # 更顺滑
        progress.progress(i)
    st.success("环境安全 ✅")
    st.button("返回菜单", on_click=back_to_menu)

# ===== 功能2：开启外挂 =====
elif st.session_state.page == 'hack':
    st.subheader("选择游戏")
    game = st.selectbox("游戏列表", ["无畏契约", "第五人格", "我的世界"])
    toggle = st.checkbox("开启")
    if toggle:
        st.success(f"{game} 开启成功 ✅")
    else:
        st.info("未开启")
    st.button("返回菜单", on_click=back_to_menu)

# ===== 功能3：降低版本 =====
elif st.session_state.page == 'downgrade':
    st.subheader("选择 iOS 版本")
    version = st.selectbox("版本", [f"iOS {i}" for i in range(10, 18)])
    if st.button("开始更改"):
        progress = st.progress(0)
        for i in range(101):
            time.sleep(0.01)
            progress.progress(i)
        st.success(f"{version} 更改成功 ✅")
    st.button("返回菜单", on_click=back_to_menu)
