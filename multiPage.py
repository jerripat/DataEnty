import tkinter as tk

root = tk.Tk()
root.title("Students Information")
root.geometry("500x400")


def openNewWindow():

    openNewWindow()


options_frame = tk.Frame(root, bg='#c3c3c3')
home_btn = tk.Button(options_frame, text="Home", bd=0, fg='#158aff', bg='#c3c3c3', width=10, command='')
home_btn.place(x=10, y=50)
roster_btn = tk.Button(options_frame, text="Roster", bd=0, fg='#008CBA', bg='#c3c3c3', width=10, command='')
roster_btn.place(x=10, y=100)
menu_btn = tk.Button(options_frame, text="Menu", bd=0, fg='#008CBA', bg='#c3c3c3', width=10, command='')
menu_btn.place(x=10, y=150)
courses_btn = tk.Button(options_frame, text="Courses", bd=0, fg='#008CBA', bg='#c3c3c3', width=10,
                        command='openNewWindow')
courses_btn.place(x=10, y=200)
options_frame.pack(side=tk.LEFT, fill=tk.Y)
options_frame.pack_propagate(False)
options_frame.configure(width=125, height=400)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=400, height=500)

root.mainloop()
