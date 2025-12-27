import streamlit as st
import pandas as pd

# Title
st.title("🎓 Student Management System")

# Session state for storing data
if "students" not in st.session_state:
    st.session_state.students = []

# Sidebar menu
menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "View Students", "Search Student"]
)

# Add Student
if menu == "Add Student":
    st.header("➕ Add New Student")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    marks = st.number_input("Marks", 0, 100)

    if st.button("Add Student"):
        student = {
            "Name": name,
            "Roll": roll,
            "Marks": marks
        }
        st.session_state.students.append(student)
        st.success("Student added successfully!")

# View Students
elif menu == "View Students":
    st.header("📋 All Students")

    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)
        st.dataframe(df)
        st.info(f"Total Students: {len(df)}")
    else:
        st.warning("No students added yet.")

# Search Student
elif menu == "Search Student":
    st.header("🔍 Search Student")

    roll_search = st.text_input("Enter Roll Number")

    if st.button("Search"):
        found = False
        for s in st.session_state.students:
            if s["Roll"] == roll_search:
                st.success("Student Found!")
                st.write(s)
                found = True
                break
        if not found:
            st.error("Student not found")

