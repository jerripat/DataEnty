import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Main Window")
window.geometry("500x500")


def openNewWindow():
    window.withdraw()  # hide main window

    new = tk.Toplevel(window)
    new.title("Second Window")
    new.geometry("300x300")
    new.config(bg="lightblue")

    tk.Label(
        new,
        text="This is the second window",
        font=("Helvetica", 16, "bold"),
        bg="lightblue"
    ).pack(pady=20)

    def close_second():
        new.destroy()
        window.deiconify()  # show main window again
        window.lift()
        window.focus_force()

    tk.Button(new, text="Quit", command=close_second).pack(pady=20)

    new.protocol("WM_DELETE_WINDOW", close_second)


tk.Button(window, text="Open New Window", command=openNewWindow).pack(pady=30)
my_menu = Menu(window)
window.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Students", command=openNewWindow)
file_menu.add_command(label="Exit", command=window.quit)

window.mainloop()
