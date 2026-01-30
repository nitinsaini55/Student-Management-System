import streamlit as st
import db as d
import pandas as pd
from datetime import date

# ===============================
# 1. PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="Attendance Management",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================
# 2. PROFESSIONAL CSS THEME
# ===============================
st.markdown("""
<style>
/* App Background */
.stApp {
    background-color: #f3f4f6;
    color: #1f2937;
    font-family: "Segoe UI", Arial, sans-serif;
}

/* Headings */
h1, h2, h3 {
    color: #111827;
    font-weight: 600;
}

/* Inputs, Selectbox, Date */
.stTextInput input,
.stSelectbox div[data-baseweb="select"],
.stDateInput div {
    background-color: #ffffff !important;
    color: #111827 !important;
    border-radius: 6px !important;
    border: 1px solid #d1d5db !important;
    font-size: 14px;
}

.stTextInput input:focus {
    border-color: #2563eb !important;
    box-shadow: none !important;
}

/* Radio buttons */
div[data-testid="stRadio"] label {
    color: #1f2937 !important;
    font-weight: 500;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 44px;
    background-color: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1e40af;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
}

/* Alerts */
.stAlert {
    background-color: #ffffff !important;
    border: 1px solid #d1d5db !important;
    border-radius: 6px;
    color: #111827 !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 3. LAYOUT
# ===============================
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    st.title("Attendance Management")
    st.divider()

    # ===============================
    # DATA FETCH
    # ===============================
    students = d.view_a()

    if not students:
        st.info("No students available in the database.")
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")
        st.stop()

    # ===============================
    # MARK ATTENDANCE
    # ===============================
    st.subheader("Mark Attendance")

    col_a, col_b = st.columns(2)

    with col_a:
        student = st.selectbox(
            "Select Student",
            students,
            format_func=lambda x: f"{x[0]} (Roll: {x[1]})"
        )
        att_date = st.date_input("Date", date.today())

    with col_b:
        status = st.radio("Status", ["Present", "Absent"], horizontal=True)
        st.write("")
        if st.button("Save Attendance"):
            d.add_attendance(student[1], status, att_date)
            st.success(f"Attendance saved for {student[0]}.")

    st.divider()

    # ===============================
    # VIEW RECORDS
    # ===============================
    st.subheader("Attendance Records")

    records = d.record()

    if records:
        df = pd.DataFrame(
            records,
            columns=["Roll No", "Date", "Status"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No attendance records found.")

    # ===============================
    # BACK BUTTON
    # ===============================
    col_back, _ = st.columns([1, 3])
    with col_back:
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")
