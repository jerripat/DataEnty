import tkinter as tk
from tkinter import messagebox, ttk

window = tk.Tk()
window.title("Data Entry Form")
window.geometry("700x500")

frame = tk.Frame(window, width=500, height=300, borderwidth=3, relief="solid")
frame.pack(padx=20, pady=20)

user_info_frame = tk.LabelFrame(
    frame,
    text="User Information",
    bg="lightgray",
    font=("Arial", 12, "bold")
)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tk.Label(user_info_frame, text="First Name:", bg="lightgray", font=("Arial", 10, "bold"))
first_name_label.grid(row=0, column=0, padx=5, pady=5)
first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0, padx=5, pady=5)

last_name_label = tk.Label(user_info_frame, text="Last Name:", bg="lightgray", font=("Arial", 10, "bold"))
last_name_label.grid(row=0, column=1, padx=5, pady=5)
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

title_label = tk.Label(user_info_frame, text="Title:", bg="lightgray",font=("Arial", 10, "bold"))
title_label.grid(row=0, column=2, padx=5, pady=5)

title_options = ["", "Mr.", "Mrs.", "Ms."]

title_combo = ttk.Combobox(
    user_info_frame,
    values=title_options,
    state="readonly",
    style="WhiteReadonly.TCombobox"
)
title_combo.grid(row=1, column=2, padx=5, pady=5)
title_combo.current(0)

age_label = tk.Label(user_info_frame, text="Age:", bg="lightgray", font=("Arial", 10, "bold"))
age_label.grid(row=2, column=0, padx=5, pady=5)
age_entry = tk.Spinbox(user_info_frame, from_=1, to=19, width=10)
age_entry.grid(row=3, column=0, padx=5, pady=5)

nationality_label = tk.Label(user_info_frame, text="Nationality:", bg="lightgray", font=("Arial", 10, "bold"))
nationality_label.grid(row=2, column=1, padx=5, pady=5)

nationality_options = [
    "", "American", "British", "Canadian", "Chinese", "Danish", "Dutch",
    "French", "German", "Indian", "Irish", "Italian", "Japanese", "Korean",
    "Mexican", "Norwegian", "Russian", "Scottish", "Spanish", "Swedish",
    "Thai", "Vietnamese"
]

style = ttk.Style()
style.map(
    "WhiteReadonly.TCombobox",
    fieldbackground=[("readonly", "white")],
    background=[("readonly", "white")],
    foreground=[("readonly", "black")]
)

nationality_combo = ttk.Combobox(
    user_info_frame,
    values=nationality_options,
    state="readonly",
    style="WhiteReadonly.TCombobox"
)
nationality_combo.grid(row=3, column=1, padx=5, pady=5)
nationality_combo.current(0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = tk.LabelFrame(frame, text="Courses", bg="lightgray", font=("Arial", 12, "bold"))
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(courses_frame, text="Registered Courses:", bg="lightgray", font=("Arial", 10, "bold"))
registered_label.grid(row=0, column=0, padx=5, pady=5)

registered_var = tk.BooleanVar()
registered_check = tk.Checkbutton(
    courses_frame,
    text="Currently Registered",
    variable=registered_var,
    bg="lightgray"
)
registered_check.grid(row=1, column=0, padx=5, pady=5)

num_courses_label = tk.Label(courses_frame, text="Number of Courses:", bg="lightgray", font=("Arial", 10, "bold"))
num_courses_label.grid(row=0, column=1, padx=5, pady=5)
num_courses_spinbox = tk.Spinbox(courses_frame, from_=0, to=10, width=10)
num_courses_spinbox.grid(row=1, column=1, padx=5, pady=5)

numsemesters_label = tk.Label(courses_frame, text="Semesters:", bg="lightgray", font=("Arial", 10, "bold"))
numsemesters_label.grid(row=0, column=2, padx=5, pady=5)
numsemesters_spinbox = tk.Spinbox(courses_frame, from_=1, to=5, width=10)
numsemesters_spinbox.grid(row=1, column=2, padx=5, pady=5)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tk.LabelFrame(frame, text="Terms and Conditions", bg="lightgray", font=("Arial", 12, "bold"))
terms_frame.grid(row=2, column=0, sticky="news",padx=20, pady=10)

terms_var = tk.BooleanVar()
terms_check = tk.Checkbutton(
    terms_frame,
    text="I agree to the terms and conditions",
    variable=terms_var,
    bg="lightgray"
)
terms_check.grid(row=0, column=0, padx=5, pady=5)

import sqlite3
from tkinter import messagebox

def register_data():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    selected_title = title_combo.get().strip()
    age = age_entry.get().strip()
    nationality = nationality_combo.get().strip()
    registered = registered_var.get()
    num_courses = num_courses_spinbox.get().strip()
    num_semesters = numsemesters_spinbox.get().strip()
    terms_agreed = terms_var.get()

    # Validation
    if not first_name or not last_name:
        messagebox.showerror("Input Error", "First name and last name are required.")
        return

    if not age.isdigit():
        messagebox.showerror("Input Error", "Age must be a number.")
        return

    if not num_courses.isdigit():
        messagebox.showerror("Input Error", "Number of courses must be a number.")
        return

    if not num_semesters.isdigit():
        messagebox.showerror("Input Error", "Number of semesters must be a number.")
        return

    if not terms_agreed:
        messagebox.showerror("Terms Error", "You must agree to the terms.")
        return

    try:
        conn = sqlite3.connect("Students.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            selected_title TEXT,
            age INTEGER,
            nationality TEXT,
            registered INTEGER,
            num_courses INTEGER,
            num_semesters INTEGER,
            terms_agreed INTEGER
        )
        """)

        cursor.execute("""
        INSERT INTO students (
            first_name, last_name, selected_title, age, nationality,
            registered, num_courses, num_semesters, terms_agreed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            first_name,
            last_name,
            selected_title,
            int(age),
            nationality,
            registered,
            int(num_courses),
            int(num_semesters),
            terms_agreed
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Student data registered successfully.")

        # Optional: clear form after successful insert
        first_name_entry.delete(0, "end")
        last_name_entry.delete(0, "end")
        title_combo.set("")
        age_entry.delete(0, "end")
        nationality_combo.set("")
        registered_var.set(0)
        num_courses_spinbox.delete(0, "end")
        num_courses_spinbox.insert(0, "0")
        numsemesters_spinbox.delete(0, "end")
        numsemesters_spinbox.insert(0, "0")
        terms_var.set(0)

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

# def submit_data():
#     first_name = first_name_entry.get().strip()
#     last_name = last_name_entry.get().strip()
#     selected_title = title_combo.get().strip()
#     age = age_entry.get().strip()
#     nationality = nationality_combo.get().strip()
#     registered = registered_var.get()
#     num_courses = num_courses_spinbox.get().strip()
#     num_semesters = numsemesters_spinbox.get().strip()
#     terms_agreed = terms_var.get()
#
#     if not first_name or not last_name or not selected_title or not age or not nationality:
#         messagebox.showerror("Error", "Please fill in all user information fields.")
#         return

    # if not terms_agreed:
    #     messagebox.showerror("Error", "You must agree to the terms and conditions.")
    #     return

    messagebox.showinfo(
        "Success",
        f"Submitted successfully!\n\n"
        f"Name: {selected_title} {first_name} {last_name}\n"
        f"Age: {age}\n"
        f"Nationality: {nationality}\n"
        f"Registered: {'Yes' if registered else 'No'}\n"
        f"Courses: {num_courses}\n"
        f"Semesters: {num_semesters}"
    )

button = tk.Button(frame, text="Submit", command=register_data)
button.grid(row=3, column=0, padx=5, pady=10, columnspan=3)

window.mainloop()