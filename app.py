import streamlit as st
import time

st.set_page_config(page_title="Ultimate Smart Tool Right Output", layout="wide")

# ===== 样式 =====
st.markdown("""
<style>
body {background-color: #0b1a38; color: white;}
.card-button {
    background: linear-gradient(135deg, #1f3c88, #1a73e8);
    padding: 50px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 28px;
    margin: 20px 0;
    width: 100%;
}
.card-button:hover {
    transform: scale(1.05);
    transition: 0.2s;
}
button.stButton>button {width: 100%; height: 100%;}
.progress-text {color:white; font-size:16px;}
</style>
""", unsafe_allow_html=True)

# ===== 页面状态 =====
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
left, right = st.columns([2,3])

# ===== 首页大按钮 =====
if st.session_state.page == "menu":
    with left:
        st.title("💜 Ultimate Smart Tool Right Output")
        modules = [
            ("🛡 过检测", "check"),
            ("🎮 开启外挂", "hack"),
            ("📉 降低版本", "downgrade"),
            ("⚙️ 基本刷入", "flash"),
            ("📱 应用管理", "apps")
        ]
        for name, page_id in modules:
            if st.button(name, key=page_id):
                go(page_id)

# ===== 功能函数 =====
def run_progress(name, steps=101, slow=0.02):
    with right:
        progress_placeholder = st.empty()
        for i in range(steps):
            value = min(i,100)
            progress_placeholder.progress(value)
            add_log(f"{name} {value}%")
            time.sleep(slow)

def page_check():
    with left:
        st.subheader("环境检测")
        if st.button("开始检测"):
            run_progress("检测模块")
            add_log("环境安全 ✅")
        st.button("返回", on_click=back)

def page_hack():
    with left:
        st.subheader("外挂模块（模拟）")
        game = st.selectbox("选择游戏", ["无畏契约", "第五人格", "我的世界"])
        if st.button("启动"):
            steps = ["加载模块","初始化环境","连接游戏进程","注入配置","完成"]
            with right:
                progress_placeholder = st.empty()
            for i in range(101):
                value = min(i,100)
                step = steps[min(i//20, 4)]
                add_log(f"{game} - {step} {value}%")
                with right:
                    progress_placeholder.progress(value)
                time.sleep(0.02)
            add_log(f"{game} 启动成功 ✅")
        st.button("返回", on_click=back)

def page_downgrade():
    with left:
        st.subheader("系统调整")
        version = st.selectbox("版本", [f"iOS {i}" for i in range(10,18)])
        if st.button("开始"):
            run_progress(f"写入 {version} 系统组件")
            add_log("更改成功 ✅")
        st.button("返回", on_click=back)

def page_flash():
    with left:
        st.subheader("基础刷入")
        option = st.selectbox("刷入方案", ["标准刷入","高级刷入","兼容模式"])
        if st.button("开始刷入"):
            run_progress(f"刷入方案 {option}")
            add_log("刷入完成 ✅")
        st.button("返回", on_click=back)

def page_apps():
    with left:
        st.subheader("应用管理")
        apps = st.multiselect("选择应用", ["微信","QQ","抖音","Minecraft","王者荣耀","原神"])
        if st.button("执行"):
            for a in apps:
                add_log(f"处理应用 {a} ✅")
        st.button("返回", on_click=back)

# ===== 页面映射 =====
page_map = {
    "check": page_check,
    "hack": page_hack,
    "downgrade": page_downgrade,
    "flash": page_flash,
    "apps": page_apps
}

if st.session_state.page in page_map:
    page_map[st.session_state.page]()

# ===== 右侧输出 =====
with right:
    st.subheader("📟 输出结果")
    output_box = st.empty()
    if st.session_state.logs:
        output_box.text("\n".join(st.session_state.logs[-100:]))
    else:
        output_box.text("暂无输出")
