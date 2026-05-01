import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")
conn.commit()


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    cursor.execute(
        "INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
        (name, age, course, marks)
    )
    conn.commit()
    print("✅ Student added successfully!")



def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}, Marks: {student[4]}")



def search_student():
    student_id = int(input("Enter student ID to search: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        print(f"\nFound: ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}, Marks: {student[4]}")
    else:
        print("❌ Student not found.")



def update_marks():
    student_id = int(input("Enter student ID to update marks: "))
    new_marks = float(input("Enter new marks: "))

    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Marks updated successfully!")
    else:
        print("❌ Student not found.")



def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Student deleted successfully!")
    else:
        print("❌ Student not found.")



def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("❌ Invalid choice. Try again.")



menu()

# Close DB
conn.close()
