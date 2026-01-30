import streamlit as st
import db as d
import pandas as pd

# ===============================
# 1. PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="View Students",
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

/* Search Input */
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

/* DataFrame Styling */
[data-testid="stDataFrame"] {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
}

/* Info/Alert Boxes */
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
    st.subheader("Student List")
    st.divider()

    # -------------------------------
    # Search Section
    # -------------------------------
    search = st.text_input("Search by Roll No", placeholder="Enter roll number to filter...")

    # -------------------------------
    # Data Fetching
    # -------------------------------
    data = d.view_a()
    if search:
        data = d.view(search)

    # -------------------------------
    # Display Data
    # -------------------------------
    if data:
        df = pd.DataFrame(
            data,
            columns=["Name", "Roll", "Department", "Year"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No student records found.")

    # -------------------------------
    # Navigation
    # -------------------------------
    col_back, col_spacer = st.columns([1, 3])
    with col_back:
        if st.button("Back"):
            st.switch_page("pages/Exfunctionality.py")
