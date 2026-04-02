import sqlite3

conn = sqlite3.connect("Students.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
conn.close()

with open("students.txt", "w", encoding="utf-8") as f:
    f.write(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Title':<10}{'Age':<5}{'Nationality':<15}{'Registered':<12}{'Courses':<10}{'Semesters':<12}{'Agreed':<8}\n")
    f.write("-" * 110 + "\n")

    for row in rows:
        f.write(f"{row[0]:<5}{row[1]:<15}{row[2]:<15}{row[3]:<10}{row[4]:<5}{row[5]:<15}{row[6]:<12}{row[7]:<10}{row[8]:<12}{row[9]:<8}\n")