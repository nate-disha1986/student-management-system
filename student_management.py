import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nate1919",
    database="student_db"
)

cursor = conn.cursor()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)

    cursor.execute(query, values)
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\nStudent Records:")
    for row in records:
        print(row)

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))
    conn.commit()
    print("Student deleted successfully!")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")

conn.close()