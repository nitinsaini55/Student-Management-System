import streamlit as st
import db as d

# 1. Page Configuration
st.set_page_config(
    page_title="SMS Admin Login",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Clean Light Professional CSS
st.markdown("""
<style>
/* ===== App Background ===== */
.stApp {
    background-color: #f8fafc;
    color: #0f172a;
    font-family: "Inter", "Segoe UI", sans-serif;
}

/* ===== Titles ===== */
h1 {
    color: #0f172a;
    font-weight: 600;
    letter-spacing: -0.4px;
}

h3 {
    color: #475569 !important;
    font-weight: 400 !important;
}

/* ===== Input Fields ===== */
.stTextInput input {
    background-color: #ffffff !important;
    color: #0f172a !important;
    border-radius: 6px !important;
    border: 1px solid #cbd5e1 !important;
    padding: 10px !important;
    font-size: 14px;
}

.stTextInput input::placeholder {
    color: #94a3b8 !important;
}

.stTextInput input:focus {
    border-color: #2563eb !important;
    box-shadow: none !important;
}

/* ===== Buttons ===== */
.stButton > button {
    width: 100%;
    height: 3em;
    border-radius: 6px;
    background-color: #2563eb;
    color: #ffffff;
    border: none;
    font-weight: 600;
    font-size: 14px;
    transition: background-color 0.2s ease;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}

/* ===== Alerts ===== */
.stAlert {
    background-color: #ffffff !important;
    border-radius: 6px;
    border: 1px solid #cbd5e1 !important;
    color: #0f172a !important;
}
</style>
""", unsafe_allow_html=True)

# 3. Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 4. UI
st.title("🎓 Student Management System")
st.subheader("Admin Login")

username = st.text_input("Username", placeholder="Enter username")
password = st.text_input("Password", type="password", placeholder="••••••••")

st.write("")

# 5. Login Logic
if st.button("Login"):
    admin_data = d.admin_login(username, password)

    if admin_data:
        st.session_state.logged_in = True
        st.success("Access granted. Redirecting...")
        st.switch_page("pages/Exfunctionality.py")
    else:
        st.error("Invalid username or password.")
