# 🎓 Student-Management-System

A professional, high-performance administrative dashboard designed for educational institutions. This system features a sleek **Cyber Dark** user interface with neon cyan accents, offering a modern alternative to traditional management software.

## 🚀 Features

- **Secure Admin Login:** Protected entry point for authorized administrators via `app.py`.
- **Student Onboarding:** Add new student profiles with unique Roll Numbers.
- **Real-time Search:** Filter student records by Roll Number using optimized SQL queries.
- **Attendance Management:** Track daily attendance (Present/Absent) with integrated date pickers.
- **Interactive Dashboard:** Accessible via `Exfunctionality.py` to navigate all modules.
- **Persistent Storage:** Built on a robust SQLite3 backend for data integrity.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Styling:** Custom CSS3 (Cyber Dark Theme)
- **Backend:** Python 3.x
- **Database:** SQLite3
- **Data Handling:** Pandas

## 📂 Project Structure

- `app.py`: The primary login interface and entry point.
- `db.py`: Contains all logic for SQL operations and database initialization.
- `pages/Exfunctionality.py`: The central hub for all admin features.
- `pages/Exadd.py`: Interface for adding new student records.
- `pages/Exview.py`: Interface for viewing and searching records.
- `pages/Exattendance.py`: System for logging and viewing attendance.
- `pages/Exdelete.py`: Interface for removing student records.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kritikmakkar-dev/Student-Management-System.git](https://github.com/kritikmakkar-dev/Student-Management-System.git)
   cd Student-Management-System
2. Install dependencies:
Bash
pip install streamlit pandas

3. Run the application:

Bash
streamlit run app.py

Default Credentials
Username: admin
Password: admin
