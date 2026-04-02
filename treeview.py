import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Students Information")
root.geometry("1000x500")

# Data
data = [
    ["Liam", "Anderson", 28, "Canadian"],
    ["Emma", "Brown", 34, "British"],
    ["Noah", "Clark", 22, "American"],
    ["Olivia", "Davis", 30, "Australian"],
    ["William", "Evans", 41, "Irish"],
    ["Ava", "Foster", 26, "New Zealander"],
    ["James", "Garcia", 37, "Mexican"],
    ["Sophia", "Harris", 29, "South African"],
    ["Benjamin", "Ivanov", 45, "Russian"],
    ["Isabella", "Johnson", 31, "American"],
    ["Lucas", "Kim", 24, "South Korean"],
    ["Mia", "Lopez", 33, "Spanish"],
    ["Henry", "Martinez", 27, "Argentinian"],
    ["Charlotte", "Nguyen", 36, "Vietnamese"],
    ["Alexander", "Olsen", 39, "Norwegian"],
    ["Amelia", "Patel", 23, "Indian"],
    ["Daniel", "Quinn", 44, "Scottish"],
    ["Harper", "Roberts", 32, "Welsh"],
    ["Matthew", "Silva", 38, "Brazilian"],
    ["Evelyn", "Taylor", 25, "American"],
    ["Joseph", "Usman", 40, "Nigerian"],
    ["Abigail", "Valdez", 21, "Colombian"],
    ["Samuel", "White", 35, "American"],
    ["Ella", "Xu", 28, "Chinese"],
    ["David", "Young", 42, "American"],
]

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview",
    font=("Arial", 14),
    background="#D3D3D3",
    foreground="black",
    rowheight=20,
    fieldbackground="#D3D3D3"
)
style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
style.map("Treeview", background=[("selected", "#347083")])

# Frame
tree_frame = ttk.Frame(root)
tree_frame.pack(pady=20, fill="both", expand=True)

# Scrollbar
tree_scroll = Scrollbar(tree_frame, orient=VERTICAL)
tree_scroll.pack(side=RIGHT, fill=Y)

# Treeview
my_tree = ttk.Treeview(
    tree_frame,
    yscrollcommand=tree_scroll.set,
    selectmode="extended",
    columns=("First Name", "Last Name", "Age", "Nationality"),
    show="headings"
)
my_tree.pack(fill="both", expand=True)

tree_scroll.config(command=my_tree.yview)

# Columns
my_tree.column("First Name", anchor="w", width=150)
my_tree.column("Last Name", anchor="w", width=150)
my_tree.column("Age", anchor="center", width=80)
my_tree.column("Nationality", anchor="center", width=180)

# Headings
my_tree.heading("First Name", text="First Name")
my_tree.heading("Last Name", text="Last Name")
my_tree.heading("Age", text="Age")
my_tree.heading("Nationality", text="Nationality")

# Row colors
my_tree.tag_configure("evenrow", background="lightblue")
my_tree.tag_configure("oddrow", background="white")

# Insert data
for index, row in enumerate(data):
    tag = "evenrow" if index % 2 == 0 else "oddrow"
    my_tree.insert("", "end", values=row, tags=(tag,))

root.mainloop()