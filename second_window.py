import tkinter as tk

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
        window.deiconify()   # show main window again
        window.lift()
        window.focus_force()

    tk.Button(new, text="Quit", command=close_second).pack(pady=20)

    new.protocol("WM_DELETE_WINDOW", close_second)

tk.Button(window, text="Open New Window", command=openNewWindow).pack(pady=30)

window.mainloop()