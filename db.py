import sqlite3

# 1. DATABASE INITIALIZATION
# This runs every time the app starts to ensure tables exist
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    # Admin Table
    c.execute("""CREATE TABLE IF NOT EXISTS admin(U_Name TEXT, Pass TEXT)""")
    # Students Table
    c.execute("""CREATE TABLE IF NOT EXISTS students (
                name TEXT, roll TEXT UNIQUE, department TEXT, year INTEGER)""")
    # Attendance Table
    c.execute("""CREATE TABLE IF NOT EXISTS attendance (
                student_roll TEXT, date TEXT, status TEXT)""")
    
    # Check if default admin exists, if not, add them
    c.execute("SELECT * FROM admin WHERE U_Name='admin'")
    if not c.fetchone():
        c.execute("INSERT INTO admin (U_Name, Pass) VALUES (?, ?)", ("admin", "admin"))
    
    conn.commit()
    conn.close()

# Call initialization immediately
init_db()

# 2. FUNCTIONAL LOGIC
def admin_login(U_Name, Pass):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM admin WHERE U_Name=? AND Pass=?", (U_Name, Pass))
    data = c.fetchone()
    conn.close()
    return data

def add(name, roll, dept, year):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("INSERT INTO students(name, roll, department, year) VALUES (?,?,?,?)",
              (name, roll, dept, year))
    conn.commit()
    conn.close()
    
def view(s):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    # FIX: Added trailing comma (s,) to create a proper tuple
    c.execute("SELECT * FROM students WHERE roll=?", (s,))
    data = c.fetchall()
    conn.close()
    return data

def view_a():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    data = c.fetchall()
    conn.close()
    return data

def delete(s):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE roll = ?", (s,))
    conn.commit()
    conn.close()

def add_attendance(student_roll, status, att_date):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("INSERT INTO attendance(student_roll, date, status) VALUES (?,?,?)",
              (student_roll, str(att_date), status))
    conn.commit()
    conn.close()

def record():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM attendance")
    data = c.fetchall()
    conn.close()
    return data
