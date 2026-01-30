import streamlit as st
import db as d
import pandas as pd

# ===============================
# 1. PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="Delete Student",
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

/* Headings */
h1, h2, h3 {
    color: #111827;
    font-weight: 600;
}

/* Input Field */
.stTextInput input {
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

/* Standard Buttons */
.stButton > button {
    width: 100%;
    height: 44px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
}

/* Primary (Blue) Button */
.stButton > button:nth-child(2) {
    background-color: #2563eb;
    color: #ffffff;
    border: none;
}

.stButton > button:nth-child(2):hover {
    background-color: #1e40af;
}

/* Delete Button (Red) */
.stButton > button:nth-child(1) {
    background-color: #f87171;
    color: #ffffff;
    border: none;
}

.stButton > button:nth-child(1):hover {
    background-color: #dc2626;
}

/* DataFrame Styling */
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
# 3. STRUCTURAL LAYOUT
# ===============================
left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:
    st.subheader("Delete Student")
    st.divider()

    # ===============================
    # INPUT
    # ===============================
    roll = st.text_input("Enter Roll No to Delete", placeholder="e.g. 101")

    # ===============================
    # DATA TABLE
    # ===============================
    data = d.view_a()
    if data:
        df = pd.DataFrame(
            data,
            columns=["Name", "Roll", "Department", "Year"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No student records found")

    st.write("<br>", unsafe_allow_html=True)

    # ===============================
    # ACTION BUTTONS
    # ===============================
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Delete"):
            if roll:
                if d.view(roll):
                    d.delete(roll)
                    st.success(f"Student with Roll {roll} deleted successfully")
                    st.experimental_rerun()
                else:
                    st.error("Roll Number not found")
            else:
                st.warning("Please enter a Roll Number")

    with col2:
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")
