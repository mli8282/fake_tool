import streamlit as st
import time
import random

st.set_page_config(page_title="Smart Tool", layout="wide")

# ===== 样式 =====
st.markdown("""
<style>
.main {
    background-color: #f5f0ff;
}
.card {
    background: linear-gradient(135deg, #c084fc, #9333ea);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 18px;
    margin: 10px;
}
button {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ===== 状态 =====
if "page" not in st.session_state:
    st.session_state.page = "menu"

if "logs" not in st.session_state:
    st.session_state.logs = []

def go(p):
    st.session_state.page = p

def back():
    st.session_state.page = "menu"

def add_log(text):
    st.session_state.logs.append(f"[{time.strftime('%H:%M:%S')}] {text}")

# ===== 布局 =====
left, right = st.columns([2,1])

# ===== 首页 =====
if st.session_state.page == "menu":
    with left:
        st.title("💜 Smart Tool")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🛡 过检测"):
                go("check")
            if st.button("⚙️ 基本刷入"):
                go("flash")

        with col2:
            if st.button("🎮 开启外挂"):
                go("hack")
            if st.button("📱 应用管理"):
                go("apps")

        with col3:
            if st.button("📉 降低版本"):
                go("downgrade")

# ===== 过检测 =====
elif st.session_state.page == "check":
    with left:
        st.subheader("环境检测")

        if st.button("开始检测"):
            progress = st.progress(0)
            text = st.empty()

            for i in range(101):
                time.sleep(0.02)
                progress.progress(i)
                text.text(f"检测中... {i}%")

                if i % 10 == 0:
                    add_log(f"扫描模块 {i}%")

            st.success("环境安全 ✅")

        st.button("返回", on_click=back)

# ===== 外挂 =====
elif st.session_state.page == "hack":
    with left:
        st.subheader("模块加载（模拟）")

        game = st.selectbox("选择游戏", ["无畏契约", "第五人格", "我的世界"])

        if st.button("启动"):
            progress = st.progress(0)
            text = st.empty()

            steps = [
                "加载模块...",
                "初始化环境...",
                "连接进程...",
                "写入配置...",
                "完成"
            ]

            for i in range(101):
                time.sleep(0.02)
                progress.progress(i)

                if i < 20:
                    text.text(steps[0])
                elif i < 40:
                    text.text(steps[1])
                elif i < 60:
                    text.text(steps[2])
                elif i < 90:
                    text.text(steps[3])
                else:
                    text.text(steps[4])

                if i % 15 == 0:
                    add_log(f"{game} 模块进度 {i}%")

            st.success(f"{game} 启动成功 ✅")

        st.button("返回", on_click=back)

# ===== 降版本 =====
elif st.session_state.page == "downgrade":
    with left:
        st.subheader("系统操作")

        version = st.selectbox("版本", [f"iOS {i}" for i in range(10,18)])

        if st.button("开始"):
            progress = st.progress(0)

            for i in range(101):
                time.sleep(0.02)
                progress.progress(i)

                if i % 10 == 0:
                    add_log(f"写入系统组件 {i}%")

            st.success("更改成功 ✅")

        st.button("返回", on_click=back)

# ===== 应用管理 =====
elif st.session_state.page == "apps":
    with left:
        st.subheader("应用管理")

        apps = st.multiselect("选择应用", ["微信", "QQ", "抖音", "Minecraft"])

        if st.button("执行"):
            for app in apps:
                add_log(f"处理应用 {app}")
                st.write(f"✔ {app} 完成")

        st.button("返回", on_click=back)

# ===== 刷入 =====
elif st.session_state.page == "flash":
    with left:
        st.subheader("基础刷入")

        if st.button("开始刷入"):
            progress = st.progress(0)

            for i in range(101):
                time.sleep(0.02)
                progress.progress(i)

                if i % 10 == 0:
                    add_log(f"刷入模块 {i}%")

            st.success("刷入完成 ✅")

        st.button("返回", on_click=back)

# ===== 右侧日志 =====
with right:
    st.subheader("📟 系统日志")

    log_box = st.empty()

    if st.session_state.logs:
        log_box.text("\n".join(st.session_state.logs[-20:]))
    else:
        log_box.text("暂无日志")
