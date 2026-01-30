import streamlit as st

# ===============================
# 1. PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="SMS Admin Panel",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================
# 2. PROFESSIONAL LIGHT THEME CSS
# ===============================
st.markdown("""
<style>
/* App Background */
.stApp {
    background-color: #f3f4f6;
    color: #1f2937;
    font-family: "Segoe UI", Arial, sans-serif;
}

/* Page Title */
h1 {
    color: #111827;
    font-weight: 700;
    text-align: left;
    margin-top: 20px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 44px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
    color: #ffffff;
    background-color: #2563eb;
    border: none;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background-color: #1e40af;
}

/* Logout Button (Secondary) */
.stButton > button.logout {
    background-color: #6b7280 !important;
}

.stButton > button.logout:hover {
    background-color: #4b5563 !important;
}

/* Columns spacing */
div[data-testid="column"] {
    gap: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 3. STRUCTURAL LAYOUT
# ===============================
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    # -------------------------------
    # Row 1: Logout Button
    # -------------------------------
    col_log, col_empty = st.columns([1, 5])
    with col_log:
        if st.button("Log out", key="logout"):
            st.session_state.logged_in = False
            st.switch_page("app.py")

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------
    # Row 2: Page Title
    # -------------------------------
    st.title("Admin Panel Functionalities")
    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------
    # Row 3: Action Buttons
    # -------------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Add Student"):
            st.switch_page("pages/Exadd.py")

    with col2:
        if st.button("View Students"):
            st.switch_page("pages/Exview.py")

    with col3:
        if st.button("Attendance"):
            st.switch_page("pages/Exattendence.py")

    with col4:
        if st.button("Delete Student"):
            st.switch_page("pages/Exdelete.py")
