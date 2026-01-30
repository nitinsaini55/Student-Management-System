import streamlit as st
import db as d

# ===============================
# PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="Add Student",
    page_icon="➕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

left_margin, center_content, right_margin = st.columns([1, 4, 1])

with center_content:

    # ===============================
    # TITLE
    # ===============================
    st.markdown(
        "<h1 style='text-align:center; font-size: 44px; font-weight: 600; color: #111827; margin-bottom: 1.5rem;'>Add Student</h1>",
        unsafe_allow_html=True
    )

    # ===============================
    # PROFESSIONAL CSS
    # ===============================
    st.markdown("""
    <style>
    /* App Background */
    .stApp {
        background-color: #f3f4f6;
        color: #1f2937;
        font-family: "Segoe UI", Arial, sans-serif;
    }

    /* Form Container */
    form {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
    }

    /* Inputs & Selectbox */
    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] {
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

    /* Buttons */
    .stButton > button {
        width: 100%;
        height: 44px;
        background-color: #2563eb;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        font-size: 14px;
    }

    .stButton > button:hover {
        background-color: #1e40af;
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
    # FORM
    # ===============================
    with st.form("add_student_form", clear_on_submit=True):

        name = st.text_input("Name", placeholder="Enter full name")
        roll = st.text_input("Roll No", placeholder="e.g. 101")
        dept = st.text_input("Department", placeholder="e.g. Computer Science")
        year = st.selectbox("Year", [1, 2, 3, 4])

        submitted = st.form_submit_button("Add Student")

        if submitted:
            if name and roll:
                try:
                    d.add(name, roll, dept, year)
                    st.success(f"Student '{name}' added successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Name and Roll No are required.")

    # ===============================
    # BACK BUTTON
    # ===============================
    if st.button("Back"):
        st.switch_page("pages/Exfunctionality.py")
