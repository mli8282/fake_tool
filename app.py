import streamlit as st
import time

st.set_page_config(page_title="Ultimate Smart Tool Right Output Only", layout="wide")

# ===== 样式 =====
st.markdown("""
<style>
body {background-color: #0b1a38; color: white;}
.card-button {
    background: linear-gradient(135deg, #1f3c88, #1a73e8);
    padding: 60px;
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
</style>
""", unsafe_allow_html=True)

# ===== 页面状态 =====
if "page" not in st.session_state:
    st.session_state.page = "menu"

def go(page):
    st.session_state.page = page

# ===== 布局 =====
left, right = st.columns([2,3])

# ===== 左侧按钮 =====
if st.session_state.page == "menu":
    with left:
        st.title("💜 Ultimate Smart Tool")
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
def run_progress(name, slow=0.02):
    progress_placeholder = right.empty()
    for i in range(101):
        value = min(i,100)
        progress_placeholder.progress(value)
        right.text(f"{name} {value}%")
        time.sleep(slow)

# ===== 模块页面 =====
def page_check():
    if st.session_state.page != "check":
        return
    with right:
        st.subheader("环境检测")
        if st.button("开始检测"):
            run_progress("检测模块")
            st.text("环境安全 ✅")
        if st.button("返回"):
            st.session_state.page = "menu"

def page_hack():
    if st.session_state.page != "hack":
        return
    with right:
        st.subheader("外挂模块（模拟）")
        game = st.selectbox("选择游戏", ["无畏契约","第五人格","我的世界"])
        if st.button("启动"):
            steps = ["加载模块","初始化环境","连接进程","注入配置","完成"]
            progress_placeholder = st.empty()
            for i in range(101):
                value = min(i,100)
                step_name = steps[min(i//20,4)]
                progress_placeholder.progress(value)
                st.text(f"{game} - {step_name} {value}%")
                time.sleep(0.02)
            st.text(f"{game} 启动成功 ✅")
        if st.button("返回"):
            st.session_state.page = "menu"

def page_downgrade():
    if st.session_state.page != "downgrade":
        return
    with right:
        st.subheader("系统调整")
        version = st.selectbox("版本", [f"iOS {i}" for i in range(10,18)])
        if st.button("开始"):
            run_progress(f"写入 {version} 系统组件")
            st.text("更改成功 ✅")
        if st.button("返回"):
            st.session_state.page = "menu"

def page_flash():
    if st.session_state.page != "flash":
        return
    with right:
        st.subheader("基础刷入")
        option = st.selectbox("刷入方案", ["标准刷入","高级刷入","兼容模式"])
        if st.button("开始刷入"):
            run_progress(f"刷入方案 {option}")
            st.text("刷入完成 ✅")
        if st.button("返回"):
            st.session_state.page = "menu"

def page_apps():
    if st.session_state.page != "apps":
        return
    with right:
        st.subheader("应用管理")
        apps = st.multiselect("选择应用", ["微信","QQ","抖音","Minecraft","王者荣耀","原神"])
        if st.button("执行"):
            for a in apps:
                st.text(f"处理应用 {a} ✅")
        if st.button("返回"):
            st.session_state.page = "menu"

# ===== 页面映射 =====
page_map = {
    "check": page_check,
    "hack": page_hack,
    "downgrade": page_downgrade,
    "flash": page_flash,
    "apps": page_apps
}

for func in page_map.values():
    func()
